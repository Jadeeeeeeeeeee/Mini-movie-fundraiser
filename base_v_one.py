#Functions go here

#Checks user has entered yes/no to a question
def yes_no(question):


  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"

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
  name = input("Please enter your name or 'xxx' to quit: ").lower()

  if name == "xxx":
    break
 
  tickets_sold += 1 

# Output number of tickets sold
if tickets_sold == Max_Tickets:
  print("Congratulations, you have sold all the tickets.")
else:
  print("You have sold {} ticket/s. There is {} ticket/s " "remaining".format(tickets_sold, Max_Tickets - tickets_sold))