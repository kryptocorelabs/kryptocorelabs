"""Serve just the synthetic login page over HTTPS on IPv4 loopback."""
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import ssl


PAGE = Path(__file__).with_name("login.html").read_bytes()


class LoginPage(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/" or self.headers.get("Host") != "localhost:8443":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Security-Policy", "default-src 'none'; "
                         "script-src 'unsafe-inline'; style-src 'unsafe-inline'; form-action 'none'")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(PAGE)))
        self.end_headers()
        self.wfile.write(PAGE)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("key")
    args = parser.parse_args()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(args.certificate, args.key)
    with HTTPServer(("127.0.0.1", 8443), LoginPage) as server:
        server.socket = context.wrap_socket(server.socket, server_side=True)
        print("Demo sign-in: https://localhost:8443/", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()
