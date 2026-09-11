import http.server
import socketserver

PORT = 8082

# This tells Python to serve files out of the current folder
Handler = http.server.SimpleHTTPRequestHandler

print(f"[-] INITIALIZING CYBER LOUNGE & JUICE BAR FRONTEND...")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"[+] SUCCESS: Cyber Lounge UI live on http://localhost:{PORT}")
    httpd.serve_forever()
