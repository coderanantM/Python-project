import pandas as pd
def show_menu(): 
    print("BSNL System Main Menu")
    print("=======================")
    print()
    print("1. Read Customer Details")
    print("2. Calculate Bill")
    print("3. report based on Customer number")
    print("4. Customer Report-Summary")
    print("5. Exit")
    
def read_customer_details():
    number_of_customers = int(input("Enter the number of customers: "))
    telephone_numbers = []
    no_of_calls = []
    from_dates = []
    to_dates = []
    
    for i in range(number_of_customers):
        print(f"\nCustomer {i+1} details:")
        telephone_number = input("Enter the telephone number: ")
        no_of_call = input("Enter the number of calls placed: ")
        from_date = input("Enter the from date: ")
        to_date = input("Enter the to date: ")
        
        telephone_numbers.append(telephone_number)
        no_of_calls.append(no_of_call)
        from_dates.append(from_date)
        to_dates.append(to_date)
        
        return telephone_numbers, no_of_calls, from_dates, to_dates
    
def calculate_bill(no_of_calls):
    if no_of_calls<50:
        print("No charges")
    elif no_of_calls >=51 and no_of_calls <=150:
        calculate = 1 * no_of_calls
        print("Your charges are: ", calculate)
    elif no_of_calls >=151 and no_of_calls <=250:
        calculate1 = 1.50 * no_of_calls
        print("Your charges are: ", calculate1)
    elif no_of_calls > 250:
        calculate2 = 3 * no_of_calls
        print("Your charges are: ", calculate2)
        
