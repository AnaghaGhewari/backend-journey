# MULTIPLE ROUTES WITH 404 HANDLING
from http.server import HTTPServer, BaseHTTPRequestHandler
import json 

class RouteHandler(BaseHTTPRequestHandler): # Creating a custom request handler
    def send_json(self, status : int, data:dict): #it defines the structure tof the functions that are to be used ahead

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/vitals":
         self.send_json(200,{"status":"ok","version":"1.0"})
        elif self.path == "/api/v1/vitals":
           self.send_json(200,[
              {"id":1, "heart_rate":88, "sleep_hours":5.5, "steps":42000},
              {"id":2, "heart_rate":72, "sleep_hours":7.0, "steps":8900},
              {"id":3, "heart_rate":95, "sleep_hours":4.0, "steps":2100},

           ])

        elif self.path == "/api/v1/risk/score":
           self.send_json(200,
              {
                 "risk_score": 0.73,
                 "level": "high",
                 "top_factor": ["low_sleep","elevated_hr"],
                 "generated_at": "2025-06-01T09:00:00"
              }
         )
        
        elif self.path == "/api/v1/users/me":
           self.send_json(200,{
              "id":"1",
              "name":"Rohan",
              "email":"123rohan@gmail.com"
           }
           )
        
        else:
           self.send_json(404,{"error":"Route not found","path": self.path})
    def log_message(self, format, *args): pass

HTTPServer(("localhost",8000),RouteHandler).serve_forever()
      