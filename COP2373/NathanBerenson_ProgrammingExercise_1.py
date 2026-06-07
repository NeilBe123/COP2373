
#This function uses a while statement and an accumulator to track the amount of tickets sold.
def selling_tickets():

#This variable starts out the amount of tickets needed
    ticket_amount = 10

#This variable starts out the number of buyers
    buyer = 0

#The while function only runs until ticket_amount runs out
    while 0 < ticket_amount <= 10:

    #This input asks the user for how many tickets they want and converts it into an integer with 'int'
        ticket = int(input("How many tickets would you like?: "))

    #Uses an if statement to prevent the user from buying more than one ticket
        if ticket > 4:

            print("You can only purchase 4 tickets.")

        else:
            #Removes the amount of tickets purchased with '-=' accumulator
            ticket_amount -= ticket

            #Adds to buyer count with '+='
            buyer += 1

            #Lets the user know how many tickets are still available
            print(f"There are {ticket_amount} tickets remaining")

    else:

        print("All the tickets have been sold")

    #Returns the accumulator function 'buyers' to be used in a new function
    return buyer

#This function runs the previous function and prints out the amount of buyers
def buyers():

    #Receives the buyer variable from the function and transfers it into this new function
    buyer = selling_tickets()

    print(f"There are {buyer} buyers")

#Activates the buyers() function
buyers()
