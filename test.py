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