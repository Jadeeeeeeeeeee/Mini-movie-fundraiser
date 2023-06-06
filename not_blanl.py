#functions go here

#checks if the user's response s not blank
def not_blank(question):

  while True:
    response = input(question)

    if response == "":
      print("Sorry this can't be blank, please try again")
    else:
      return response

#main routine goes here
while True:
  name = not_blank("Enter your name (or 'xxx' to quit)")
  if name == "xxx":
    break

print("we are done")
     