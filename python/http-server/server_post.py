from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

class PostHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <h1>Submit a Form</h1>
        <form method="POST" action="/submit">
            <label>Name: <input name="name" type="text"></label><br>
            <label>Message: <input name="message" type="text"></label><br>
            <button type="submit">Submit</button>
        </form>
        """
        self.wfile.write(html.encode())
    
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Parse the form data
        fields = parse_qs(post_data)
        print(f"Received: {fields}")
        
        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        name = fields.get('name', ['Unknown'])[0]
        message = fields.get('message', [''])[0]
        
        response = f"""
        <h1>Thank you, {name}!</h1>
        <p>Your message: {message}</p>
        <a href="/">Go back</a>
        """
        self.wfile.write(response.encode())

server = HTTPServer(('localhost', 8000), PostHandler)
print("Server with POST handling running on http://localhost:8000")
server.serve_forever()