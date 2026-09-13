import http.server, json, os, sys, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 카툰 폴더
EXT = {'.jpg','.jpeg','.png','.gif','.webp','.svg'}
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def do_GET(self):
        if self.path == '/':
            self.path = '/app/index.html'
        elif self.path == '/api/list':
            files = sorted(f for f in os.listdir(ROOT)
                           if os.path.splitext(f)[1].lower() in EXT and not f.startswith('.'))
            body = json.dumps(files, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()
    def log_message(self, *a): pass

print(f'http://localhost:{PORT}', flush=True)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()
