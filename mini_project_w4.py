import csv
from Functions_w5 import read_csv_file, save_list, append_dict, update_dict, delete_index, enumerate_orders, whitespace
from pprint import pprint

orders_list = []
product_list = []
courier_list = []

order_status = ['Order Confirmed','Preparing','Dispatched', 'Delivered', 'Unable to Deliver', 'Cancelled']

orders_list = read_csv_file('order_list.csv', orders_list)
product_list = read_csv_file('product_list.csv', product_list)
courier_list = read_csv_file('courier_list.csv', courier_list)

def new_welcome():
    import time
    print("Hello, Welcome to Aliana's Shop")
    time.sleep(1.5)

def main_menu():
    print("""
        [0] - To Save And Exit 
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Options
    """)
    option = int(input("""\n\tEnter your option here: """))
    
    if option == 0:
        save_list('Product_list.csv', product_list)
        save_list('Courier_list.csv', courier_list)
        save_list('Order_list.csv', orders_list)
        whitespace()
        print('\tThanks for visiting! Goodbye')
        whitespace()
        exit()
    
    elif option == 1:
        product_menu()   
        
    elif option == 2:
        courier_menu()
    
    elif option == 3:
        orders_details()
        
    else:
        print ('\t"Invalid choice. Enter options 0-1"')
        whitespace()
        main_menu() 

def product_menu():
    print('\n\tProduct options')
    print('''
        [0]: To Return To The Main Menu
        [1]: To View Drink List
        [2]: To Update Existing Drinks Menu
        [3]: To List & Replace A Drink
        [4]: To Delete A Drink''')
    
    user_input = int(input('\n\tSelect from the options above: '))
    
    if user_input == 0:
        main_menu()
    elif user_input == 1:
        print("\n\tHere's The Drink List\n\t")
        pprint(product_list)
        product_menu()
    elif user_input == 2:
        print('\n\tHere Ts The Drink List\n\t')
        pprint(product_list)
        new_product = input('\n\tPlease Add A New Drink To The List : ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))
        new_dict = {}
        new_dict['Name'] = new_product
        new_dict['Price'] = new_price
        headers = ['Name', 'Price']
        append_dict('Product_list.csv', new_dict, headers)
        print("\n\tYou've Added A Beverage To The List:", new_dict)
        product_menu()
        
    elif user_input == 3:  # Check is \n still needs to be here
        print('\n\tThe Beverage Selections Are: \n\t')
        enumerate_orders(product_list)
        number_input = float(
            input('\n\tChoose A Number To Replace With Another Beverage: '))
        new_variable = product_list[number_input]
        update_dict(new_variable)
        print("\n\tHere's The Updated Beverage List:\t\n")
        pprint(product_list)
        product_menu()
        
    elif user_input == 4:
        print('\n\tLets delete a beverage\n\t')
        enumerate_orders(product_list)
        deleted_input = int(
            input('\n\tSelected a beverage to be deleted by choosing a number: '))
        whitespace()
        delete_index(product_list, deleted_input)
        print("\n\tYour Chosen Beverage Has Been Deleted\n\t")
        enumerate_orders(product_list)
        product_menu()
        
    else:
        print('"Invalid choice. Enter options 0-4"')
        product_menu()

def courier_menu():
    print('''
        [0] - Return to Main Menu
        [1] - Print Couriers List
        [2] - Create New Courier
        [3] - Update Courier
        [4] - Delete Courier
        ''')
    
    user_input = int(input("""\\n\tEnter Your Choice Here: """))
    
    if user_input == 0:    
        whitespace()
        print('Thanks For Visiting! Goodbye.')
        whitespace()
        main_menu()
        
    elif user_input == 1:
        print("\n\tHere's The Courier's List\n\t")
        pprint(courier_list)
        courier_menu()
        
    elif user_input == 2:
        print("\n\tHere's The Courier's List\n\t")
        pprint(courier_list)
        courier_name = input('\n\tPlease Add A New Courier : ')
        courier_phone = int(input('\n\tPlease Enter A Phone Number: '))
        new_dict = {}
        new_dict['Name'] = courier_name
        new_dict['Phone Number'] = courier_phone
        headers = ['Name', 'Phone Number']
        append_dict('Courier_list.csv', new_dict, headers)
        print("\n\tYou've Added A Courier To The List\n\t")
        pprint(new_dict)
        courier_menu()
        
    elif user_input == 3:  # Check is\n still needs to be here
        print('\n\tThe Courier List is: ', '\n')
        enumerate_orders(courier_list)
        number_input = int(
            input('\n\tChoose A Courier To Replace: '))
        new_variable = courier_list[number_input]
        update_dict(new_variable)
        print("\n\tYou've updated The Courier's List:\n\t")
        pprint(courier_list)
        courier_menu()
        
    elif user_input == 4:
        print('\n\tLets Delete A Courier')
        enumerate_orders(courier_list)
        deleted_input = int(
            input('\n\tChoose A Courier To Be Deleted: '))
        delete_index(courier_list, deleted_input)
        print("\n\tYou've deleted a selection:\n\t")
        pprint(courier_list)
        courier_menu()
        
    else:
        print('\n\t"Invalid choice. Enter options 0-4"')
        courier_menu()

def orders_details():
    print('\n\tOrder Menu')
    print('''
        [0]: Return To The Main Menu
        [1]: View Order List
        [2]: Enter Order Details
        [3]: Update A Specific Order Status
        [4]: Update Existing Order
        [5]: Delete An Order''')
    
    user_input = int(input('\n\tSelect From The Options Above: '))
    
    if user_input == 0:
        main_menu()
        
    elif user_input == 1:
        print("\n\tHere's The Order's List:")
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        orders_details()
        
    elif user_input == 2:
        customer_name = input('\n\tPlease Enter Your Name : ')
        customer_address = input('\n\tPlease Enter Your Address: ')
        customer_phone_number = int(input('\n\tPlease Enter A Phone Number: \n\t'))
        
        enumerate_orders(product_list)
        product_choice = input('\n\tWhich Product Do You Want Added To Your Order: ')
        
        enumerate_orders(product_list)
        product_choice = input('Please Select Your Products: ')
    
        enumerate_orders(courier_list)
        courier_choice = int(input('Please Choose A Courier To Deliver Your Order:?  '))
        
        entry = {}
        entry['Customer Name'] = customer_name 
        entry ['Customer Address'] = customer_address
        entry ['Customer Phone Number'] = customer_phone_number
        entry ['Courier'] = courier_choice
        entry['Status'] = order_status[1]
        entry['Products'] = product_choice
        
        titles = ['Customer Name', 'Customer Address' 'Customer Phone Number','Courier', 'Status', 'Products']
        
        append_dict('orders.csv', entry, titles)
        
        print('Thank you for your order', entry)
        
        orders_details()
        
    elif user_input == 3:
        print('\nThe Orders List Is: ', '\n')
        
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        
        order_input = int(
        input('\n\tChoose An Order To Update: '))
        whitespace()
        enumerate_orders.details(order_status)
        status_input = int(input('\n\tChoose Status To Update: '))
        
        new_variable = orders_list[order_input]
        new_variable['Status'] = order_status[status_input]
        
        print("\nHere Is The New Updated Drink Menu: ", new_variable)
        orders_details()
    
    elif user_input == 4:
        print('\n\tLets Update Existing Order\n\t')
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        
        select_order = int(input('\n\tChoose An Order: '))
        chosen_order = orders_list[select_order]
        update_dict(chosen_order)
        print("\n\tYou've Updated The Order\n\t")
        
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        orders_details()
    
    elif user_input == 5:
        print('\nLets Delete An Order')
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        
        deleted_input = int(
            input('\nSelect An Order To Delete: '))
        delete_index(orders_list, deleted_input)
        print("You're Order No Longer Exists:\n\t")
        
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        orders_details()
    else:
        print("Invalid choice. Enter options 0-5")
        whitespace()
        orders_details()

new_welcome()
main_menu()