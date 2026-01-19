from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #print what client sent us
        print(f"\n--- Received Request ---")
        print(f"Path: {self.path}")
        print(f"Headers: {self.headers}")

        #send response
        self.send_response(200) #status code
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        #send actual content
        response = f"<h1>You requested: {self.path}</h1>"
        self.wfile.write(response.encode())

server = HTTPServer(('localhost', 8000), SimpleHandler)
print("Server running on http://localhost:8000")
server.serve_forever()