def calculate_amount(num_calls):
    if num_calls <= 50:
        return 0.00
    elif 51 <= num_calls <= 150:
        return num_calls - 50  # Rs. 1.00 per extra call beyond 50
    elif 151 <= num_calls <= 250:
        return 100 + (num_calls - 150) * 1.50
    else:
        return 100 + 150 + (num_calls - 250) * 3.00    

        
def generate_report(customer_data):
    print("Telephone Billing System")
    print("Customer ID : ", customer_data['Customer ID'], " Telephone Number: ", customer_data['Telephone Number'])
    print("From Date : ", customer_data['From Date'], " To Date : ", customer_data['To Date'])
    print("Number of Calls: ", customer_data['NoOfCalls'])
    print("No. of Calls Rate Amount")
    print(" 0 – 50 0.00 0.00")
    print("51 – 150 1.00 100.00")
    print("151 – 250 1.50 150.00")
    print("251 –", customer_data['NoOfCalls'], "3.00", calculate_amount(customer_data['NoOfCalls']), sep=' ')
    print("_" * 40)
    print("Total Amount :", calculate_amount(customer_data['NoOfCalls']))

def generate_summary_report(customer_details):
    print("Telephone Billing System")
    print("Customer ID Telephone Number No. of Calls Amount")
    
    total_amount = 0
    for customer in customer_details:
        amount = calculate_amount(customer['NoOfCalls'])
        total_amount += amount
        print(customer['Customer ID'], customer['Telephone Number'], customer['NoOfCalls'], f"{amount:.2f}", sep=' ')
    
    print("_" * 40)
    print("Total Amount :", f"{total_amount:.2f}")
    
def main():
    customer_details = []
    customer_id = 1000
    
    num_customers = int(input("Enter the number of customers: "))
    
    for _ in range(num_customers):
        telephone_number = int(input("Enter Telephone Number (7 digits): "))
        no_of_calls = int(input("Enter Number of Calls: "))
        from_date = input("Enter From Date: ")
        to_date = input("Enter To Date: ")
        
        customer_details.append({
            'Customer ID': customer_id,
            'Telephone Number': telephone_number,
            'NoOfCalls': no_of_calls,
            'From Date': from_date,
            'To Date': to_date
        })
        
        customer_id += 1
        
    choice = 0
    while choice != 6:
        print("BSNL System Main Menu")
        print("_" * 40)
        print()
        print("1. Read Customer Details")
        print("2. Calculate Bill")
        print("3. report based on Customer number")
        print("4. Customer Report-Summary")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 2:
            num_of_call = int(input("Enter number of calls: "))
            bill = calculate_amount(num_of_call)
            print("Total amount: ",bill)
            
        if choice == 3:
            customer_id = int(input("Enter Customer ID: "))
            found = False
            for customer_data in customer_details:
                if customer_data['Customer ID'] == customer_id:
                    generate_report(customer_data)
                    found = True
                    break
            if not found:
                print("Customer not found.")
                
        if choice == 4:
            generate_summary_report(customer_details)
            
        if choice == 5:
            print("You have come out of the program: ")
        else:
            print("You have entered an invalid choice!")
            
if __name__ == "__main__":
    main()


   