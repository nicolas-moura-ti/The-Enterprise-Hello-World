from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("[FACTORY] Gerando objeto 'Hello' via AbstractFactoryBeanProxy...")
        time.sleep(3)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"value": "Hello"}')

if __name__ == "__main__":
    print("Hello String Factory rodando na porta 9002...")
    HTTPServer(('0.0.0.0', 9002), HelloHandler).serve_forever()
