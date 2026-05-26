#Building a mock server step by step

#STEP - 1: Simplest Possible Server

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        body = json.dumps({"message":"VitalGuard is live"})
        self.wfile.write(body.encode())

    def log_message(self, format, *args):
       pass
server = HTTPServer(("localhost",8000),SimpleHandler)   
print("Running -> http://localhost:8000")
server.serve_forever() 

