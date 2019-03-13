import http.server
import socketserver
import termcolor

PORT = 8008

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        name = self.path.split('?')

        #--- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if name[0] == '/':
            f = open('form3.html', 'r')
            contents = f.read()
        elif name[0] == '/echo':
            name1 = name[1].split('=')
            if len(name1) == 2:
                name2 = name1[1].split('&')
                msg = name2[0]
                contents = """<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Echo message</title>
            </head>
            <body>"""
                contents += "<p>{}</p>".format(msg)
                contents += """<a href="/">[Main page]</a>
            </body>
            </html>"""
            elif len(name1) == 3:
                name2 = name1[1].split('&')
                msg = name2[0]
                contents = """<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Echo message</title>
            </head>
            <body>"""
                contents += "<p>{}</p>".format(msg.upper())
                contents += """<a href="/">[Main page]</a>
            </body>
            </html>"""

        else:
            f = open('error.html', 'r')
            contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        #--- Sending the body of the response message
        self.wfile.write(str.encode(contents))

#--- main program
with socketserver.TCPServer(('', PORT), TestHandler) as httpd:
    print('Serving at PORT: {}'.format(PORT))

    try:
       httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
print('The server is stopped')