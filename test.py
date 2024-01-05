first_name = input("Enter first name: ")
second_name = input("Enter second name: ")

def generate_username(first, second):
  usernames = []
  usernames.append(first + "." + second)
  usernames.append(second + "." + first)
  usernames.append(first[0] + "." + second)
  return usernames

print(generate_username(first_name, second_name))