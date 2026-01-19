from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

# In-memory storage
todos = []
todo_id_counter = 1

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/':
            self.serve_frontend()
        elif parsed.path == '/api/todos':
            self.serve_todos()
        else:
            self.send_error(404)
    
    def do_POST(self):
        if self.path == '/api/todos':
            self.create_todo()
        else:
            self.send_error(404)
    
    def do_DELETE(self):
        if self.path.startswith('/api/todos/'):
            todo_id = int(self.path.split('/')[-1])
            self.delete_todo(todo_id)
        else:
            self.send_error(404)
    
    def serve_frontend(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>TODO List</title></head>
        <body>
            <h1>My TODO List</h1>
            <input id="todoInput" type="text" placeholder="New todo...">
            <button onclick="addTodo()">Add</button>
            <ul id="todoList"></ul>
            
            <script>
                async function loadTodos() {
                    const res = await fetch('/api/todos');
                    const todos = await res.json();
                    const list = document.getElementById('todoList');
                    list.innerHTML = todos.map(t => 
                        `<li>${t.text} <button onclick="deleteTodo(${t.id})">Delete</button></li>`
                    ).join('');
                }
                
                async function addTodo() {
                    const text = document.getElementById('todoInput').value;
                    await fetch('/api/todos', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({text})
                    });
                    document.getElementById('todoInput').value = '';
                    loadTodos();
                }
                
                async function deleteTodo(id) {
                    await fetch('/api/todos/' + id, {method: 'DELETE'});
                    loadTodos();
                }
                
                loadTodos();
            </script>
        </body>
        </html>
        """
        self.wfile.write(html.encode())
    
    def serve_todos(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(todos).encode())
    
    def create_todo(self):
        global todo_id_counter
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        new_todo = {
            'id': todo_id_counter,
            'text': data['text']
        }
        todos.append(new_todo)
        todo_id_counter += 1
        
        self.send_response(201)  # 201 = Created
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(new_todo).encode())
    
    def delete_todo(self, todo_id):
        global todos
        todos = [t for t in todos if t['id'] != todo_id]
        
        self.send_response(204)  # 204 = No Content
        self.end_headers()

server = HTTPServer(('localhost', 8000), TodoHandler)
print("TODO server running on http://localhost:8000")
server.serve_forever()