# server_routing.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RoutingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.serve_home()
        elif self.path == '/about':
            self.serve_about()
        elif self.path.startswith('/api/data'):
            self.serve_json()
        else:
            self.serve_404()
    
    def serve_home(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <h1>Home Page</h1>
        <p><a href="/about">About</a></p>
        <p><a href="/api/data">API Data</a></p>
        """
        self.wfile.write(html.encode())
    
    def serve_about(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>About Page</h1>")
    
    def serve_json(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {"message": "Hello from API", "status": "success"}
        self.wfile.write(json.dumps(data).encode())
    
    def serve_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>404 - Not Found</h1>")

server = HTTPServer(('localhost', 8000), RoutingHandler)
print("Server with routing running on http://localhost:8000")
server.serve_forever()