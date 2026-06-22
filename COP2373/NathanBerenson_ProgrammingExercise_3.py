from functools import reduce

#The user inputs their monthly expenses here
def info_input():
    #Asks the user for how many expenses
    ask_for_expense = int(input("How many expenses do you have?: "))
    
    #A list for the type and cost of the expense is created
    expense_type_list = []
    expense_amount_list = []

    #This loop is repeated for their value entered into 'ask_for_expense'
    for i in range(ask_for_expense):
            
            #asks for which expense they are putting the price for, and the expense price
            expense_type = input("What is your expense: ")
            expense_amount = float(input("How much is your expense: "))

            #appends the lists for later use
            expense_type_list.append(f"{expense_type}")
            expense_amount_list.append(f"{expense_amount}")

    #returns the completed lists
    return expense_type_list, expense_amount_list

def info_sort():

    #retrieves the lists from the previous function
    expense_type_list, expense_amount_list = info_input()

    #combines the lists together, the zip() is so the type and price are paired together
    list_of_lists = list(zip(expense_type_list, expense_amount_list))

    #uses teh lambda function to add up all the list prices
    sum_result = reduce(lambda x,y : x+y, expense_amount_list)
    
    #Takes the maximum and minimum value the expense amount
    highest = max(list_of_lists, key = lambda x:x)
    lowest = min(list_of_lists, key = lambda x:x)
    
    #prints out the expenses and their prices
    print(f"{list_of_lists}"
        f"\nTotal Cost: {sum_result}"
        f"\nHighest expense cost and type: {highest}"
        f"\nLowest expense cost and type: {lowest}")

info_sort()
