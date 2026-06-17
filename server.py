"""Simple HTTP server that handles GET/POST/PUT/DELETE and simulates slow
responses."""
import time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

SLOW_PATHS = {'/topics/07-loading-indicators/response_loading-indicators.html'}
SLOW_DELAY = 4.0  # seconds


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split('?')[0] in SLOW_PATHS:
            time.sleep(SLOW_DELAY)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            with open('topics/07-loading-indicators/response_loading-indicators.html', 'rb') as f:
                self.wfile.write(f.read())
            return
        super().do_GET()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        self.rfile.read(length)
        self.do_GET()

    def do_PUT(self):
        length = int(self.headers.get('Content-Length', 0))
        self.rfile.read(length)
        self.do_GET()

    def do_DELETE(self):
        self.do_GET()

    def log_message(self, fmt, *args):
        print(f"  {args[0]} {args[1]}")


if __name__ == '__main__':
    port = 8765
    print(f"HTMX Explorer: http://localhost:{port}/index.html")
    ThreadingHTTPServer(('', port), Handler).serve_forever()
