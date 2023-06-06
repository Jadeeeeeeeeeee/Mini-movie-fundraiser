#Set the number of the max tickets to be sold

Max_Tickets = 3

#loop sell tickets 
tickets_sold = 0

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