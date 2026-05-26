# This is what happens under the hood when ANY server receives a request:
#
# 1. Client connects to your IP + port (localhost:8000)
# 2. Client sends raw HTTP text:
#       GET /vitals HTTP/1.1
#       Host: localhost:8000
#
# 3. Your server reads that text
# 4. Your server decides what to do based on method + path
# 5. Your server writes back raw HTTP text:
#       HTTP/1.1 200 OK
#       Content-Type: application/json
#
#       {"heart_rate": 88}
import json

#---Let's start---
def do_self(self):
    if self.path =="/vitals":
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"heart_rate":88}).encode())

# Fast api does the same thing
#@app.get("/vitals")
def get_vitals():
    return{"heart_rate":88}





