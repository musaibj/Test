import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class Generator:
  @staticmethod
  def generate_username(first, second):
    usernames = []
    usernames.append(first + second)
    usernames.append(second + first)
    usernames.append(first + second[0])

    usernames.append(first + "." + second)
    usernames.append(second + "." + first)
    usernames.append(first[0] + "." + second)
    usernames.append(first + "." + second[0])
    usernames.append(second[0] + "." + first)

    usernames.append(second + "_" + first)
    usernames.append(first + "_" + second[0])
    usernames.append(first[0] + "_" + second)
    usernames.append(first + "_" + second)
    usernames.append(second[0] + "_" + first)
    return usernames

  @staticmethod
  def get_input(x, y):
    first_name = x
    second_name = y
    return first_name, second_name

class MyHandler(BaseHTTPRequestHandler):
  def response(self, responseCode, message):
    self.send_response(responseCode)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(message, default=str).encode('utf-8'))

  def headerInfo(self):
    contentLength = int(self.headers['Content-Length'])
    getData = self.rfile.read(contentLength)
    data = json.loads(getData.decode('utf-8'))
    return data

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

# Instantiate Generator class
obj = Generator()

# Instantiate MyHandler class
handler = MyHandler

# Create HTTP server
server = HTTPServer(("localhost", 3036), handler)
print("Server started on port 3036")

# Start the server
server.serve_forever()
