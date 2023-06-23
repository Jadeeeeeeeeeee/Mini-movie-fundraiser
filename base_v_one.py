#Functions go here


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

#Calculate the the price of the ticket base on  the age of the user
def calc_ticket_price(var_age):

  #ticket is $7.50 for users under 16
  if var_age < 16:
    price = 7.5

  #ticket is $10.50 for users between 16 and 64 
  elif var_age < 65:
    price = 10.5 

  #ticket price is $6.50 for seniors (65+)
  else:
    price = 6.5

  return price

#checks that users enter a valid response (eg yes/No
#cash/credit) based on a list of options
def string_checker(question, num_letters, valid_response):
  
  error =  "Please choose {} or {}".format(valid_response[0],valid_response[1])

  if num_letters == 1:
    short_version = 1 
  
  else:
    short_version = 2

  while True:
    response = input(question).lower()
    
    for item in valid_response:
      if response == item[:short_version] or response == item:
        return item 
        
    print(error)



#Mainroutine goes here

#Set the number of the max tickets to be sold

Max_Tickets = 3
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
#Ask the user if they want to see instructions 
instructions = string_checker("Do you want to read the instructions (yes/no):",1 ,yes_no_list)

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
    continue

  #calculate ticket cost
  ticket_cost= calc_ticket_price

  #get payment method
  pay_method = string_checker("Choose a payment method   (cash/credit):", 2, payment_list)

  
 
  tickets_sold += 1 

# Output number of tickets sold
if tickets_sold == Max_Tickets:
  print("Congratulations, you have sold all the tickets.")
else:
  print("You have sold {} ticket/s. There is {} ticket/s " "remaining".format(tickets_sold, Max_Tickets - tickets_sold))