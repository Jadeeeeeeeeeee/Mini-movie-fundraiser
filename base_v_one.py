#Functions go here

#Checks user has entered yes/no to a question
def yes_no(question):


  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"

#checks if the user's response s not blank
def not_blank(question):

  while True:
    response = input(question)

    if response == "":
      print("Sorry this can't be blank, please try again")
    else:
      return response

#Checks if the user has inputted an integer to a given question
def num_check(question):

  while True:

    try:
      response = int(input(question))
      return response

    
    except ValueError:
      print("Please enter an integer.")

#Mainroutine goes here

#Set the number of the max tickets to be sold

Max_Tickets = 3
tickets_sold = 0
#Ask the user if they want to see instructions 
instructions = yes_no("Do you want to read the instructions? ").lower()

if instructions == "yes":
  print("program continues")

print()

#loop sell tickets

while tickets_sold < Max_Tickets:
  name = not_blank("Enter your name (or 'xxx' to quit): ")

  if name == "xxx":
    break

  age = num_check("Age: ")

  if 12 <= age <= 120:
    pass

  elif age < 12:
    print("sorry you are too young for this movie")
    continue

  else:
    print("?? That looks like a typo, please try again.")
 
  tickets_sold += 1 

# Output number of tickets sold
if tickets_sold == Max_Tickets:
  print("Congratulations, you have sold all the tickets.")
else:
  print("You have sold {} ticket/s. There is {} ticket/s " "remaining".format(tickets_sold, Max_Tickets - tickets_sold))