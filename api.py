from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from test import Generator

class MyHandler(BaseHTTPRequestHandler):
  def response(self, responseCode, message):
    self.send_response(responseCode)
    self.send_header('Content-type', 'application/json')
    self.send_header('Access-Control-Allow-Origin', '*')  # Allow any origin for testing
    self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')  # Specify allowed methods
    self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Specify allowed headers
    self.end_headers()
    self.wfile.write(json.dumps(message, default=str).encode('utf-8'))

  def headerInfo(self):
    contentLength = int(self.headers['Content-Length'])
    getData = self.rfile.read(contentLength)
    data = json.loads(getData.decode('utf-8'))
    return data

  def do_OPTIONS(self):
    self.send_response(200, "OK")
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    self.end_headers()

  def do_POST(self):
    if self.path == '/get_input':
      data = self.headerInfo()
      first_name = data.get('FirstName')
      second_name = data.get('SecondName')
      usernames = obj.generate_username(first_name, second_name)
      message = {'status': 'success', 'usernames': usernames}
      self.response(200, message)

  def do_GET(self):
    if self.path == '/generate_usernames':
      message = {'status': 'success', 'message': 'Use POST request with /get_input to generate usernames'}
      self.response(200, message)

obj = Generator()

handler = MyHandler
server = HTTPServer(("localhost", 3036), handler)
print("Server started on port 3036")
server.serve_forever()