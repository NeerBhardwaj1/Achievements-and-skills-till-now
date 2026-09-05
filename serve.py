import http.server
import socketserver
import webbrowser
import os
import sys
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stderr = sys.stdout  # Unify stderr into stdout for complete logging

PORTS_TO_TRY = [3000, 8080, 8089, 5173]

class ResilientHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = http.server.SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '.js': 'application/javascript',
        '.css': 'text/css',
        '.pdf': 'application/pdf',
        '.ico': 'image/x-icon',
        '.svg': 'image/svg+xml',
    })

    def do_GET(self):
        # Handle any stray API polling from external tools gracefully
        if self.path.startswith('/api/'):
            try:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"status":"ok"}')
            except Exception:
                pass
            return
        try:
            return super().do_GET()
        except Exception:
            pass

    def do_POST(self):
        try:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        except Exception:
            pass

    def log_message(self, format, *args):
        try:
            sys.stdout.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))
            sys.stdout.flush()
        except Exception:
            pass

class ResilientTCPServer(socketserver.TCPServer):
    allow_reuse_address = True
    def handle_error(self, request, client_address):
        # Suppress socket reset noise
        pass

httpd = None
chosen_port = None

for port in PORTS_TO_TRY:
    try:
        server = ResilientTCPServer(('127.0.0.1', port), ResilientHandler)
        httpd = server
        chosen_port = port
        break
    except Exception:
        continue

if not httpd:
    print("Could not bind to local ports. Opening index.html directly...", flush=True)
    webbrowser.open("index.html")
    sys.exit(0)

print("=" * 64, flush=True)
print("  Neer Bhardwaj — Systems Architecture & Engineering Compendium", flush=True)
print(f"  Local Live Server running at: http://localhost:{chosen_port}", flush=True)
print("=" * 64, flush=True)

while True:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.", flush=True)
        break
    except BaseException as e:
        print(f"Connection reset handled: {e}", flush=True)
        time.sleep(0.1)
        continue
