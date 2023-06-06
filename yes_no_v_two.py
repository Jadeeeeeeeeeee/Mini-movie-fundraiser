#Funcions go here 
def yes_no(question):


  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes_no.py"

#main routine goes here 

instructions = input("Would you like to read the instructions ").lower()

if instructions == "yes":
 print("Instructions go here")

elif instructions == "no":
 print("program continues")

else:
 print("Please answer either yes or no")

#main routine goes here 
instructions = yes_no("Do you want to read the instructions? ")

if instructions == "yes":
  print("instructions goes here")

print("we are done")