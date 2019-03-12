import http.server
import socketserver

PORT = 8002

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")
        print('Request line:' + self.requestline)
        print('  Cmd:' + self.command)
        print('  Path:' + self.path)

        if self.path == '/':
            with open('index.html', 'r') as f:
                content = f.read()

        elif self.path == '/blue':
            with open('blue.html', 'r') as f:
                content = f.read()

        elif self.path == '/pink':
            with open('pink.html', 'r') as f:
                content = f.read()


        else:
            with open('error.html', 'r') as f:
                content = f.read()

        self.send_response(200)
        self.send_header('Content-Type','text/plain')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT,)

    httpd.serve_forever()
