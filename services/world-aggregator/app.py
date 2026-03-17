from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class WorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("[AGGREGATOR] Buscando 'World' em cluster geodistribuído...")
        time.sleep(4)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"value": "World"}')

if __name__ == "__main__":
    print("World Data Aggregator rodando na porta 9003...")
    HTTPServer(('0.0.0.0', 9003), WorldHandler).serve_forever()
