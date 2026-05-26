#Handle Post Requests (Reading Request Body)
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class PostHandler(BaseHTTPRequestHandler):
    def send_json(self, status:int, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def read_body(self)->dict:
        #Read Content-Length header to know how many bytes to read
        length = int(self.headers.get("Content-Length",0))
        if length == 0:
            return{}
        raw = self.rfile.read(length)

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return{}
        
    def do_POST(self):
        if self.path == "/api/v1/vitals":
            body = self.read_body()

            #Validate the required fields

            required = ["heart_rate", "sleep_hours", "steps"]
            missing = [f for f in required if f not in body]

            if missing:
                self.send_json(422,{
                    "error":"Missing required fields",
                    "missing":missing
                })
                return
            #Build the saved records
            record = {
                "id":1,
                "heart_rate":body["heart_rate"],
                "sleep_hours": body["sleep_hours"],
                "steps": body["steps"],
                "notes": body.get("notes"),
                "logged_at": datetime.now().isoformat()
            }

            self.send_json(201, record)  #201 Created

        elif self.path == "/api/v1/auth/login":
            body = self.read_body()
            if body.get("email") == "123rohan@gmail.com":
                self.send_json(200,{
                    "token":"fake_jwt_token_abc123",
                    "message":"Login successful"
                })
            else:
                self.senf_json(401,{"error":"Invalid Credentials"})

        else:
            self.send_json(404,{"error":"Route not found"})
    def log_message(self, format, *args): pass

HTTPServer(("localhost",8000), PostHandler).serve_forever(
    
)

