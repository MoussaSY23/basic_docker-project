from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<html><body><h1>Hello, Docker!</h1></body></html>"
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()