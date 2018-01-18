from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("This is some static content.", "utf8"))

        requested = self.path.strip('/')
        if requested:
            self.wfile.write(bytes("</br>You asked for '{}'".format(requested), "utf8"))


httpd = HTTPServer(('127.0.0.1', 8000), Handler)
httpd.serve_forever()
