import csv
import time
from Functions_w5 import whitespace, read_csv_file, enumerate_orders, append_dict
from Functions_w5 import delete_product_from_db, delete_courier_from_db, save_list, delete_index
from Functions_w5 import write_into_courier_db, read_courier_from_db, read_product_from_db, write_into_product_db 
from Functions_w5 import update_into_product_db, update_dict, update_into_courier_db
from csv import DictWriter, DictReader
from pprint import pprint


product_list = []
courier_list = []
orders_list = []
order_status = ['Order Confirmed', 'Preparing','Dispatched', 'Delivered', 'Unable to Deliver', 'Cancelled']

product_list = read_csv_file('products_list.csv', product_list)
courier_list = read_csv_file('couriers_list.csv', courier_list)
orders_list = read_csv_file('orders_list.csv', orders_list)




def new_welcome():
    print("\033[93m\n\t    Hello \033[0m")
    time.sleep(0.75)
    print("\033[95m\n\t   Welcome \033[0m")
    time.sleep(0.75)
    print("\033[91m\n\t     To \033[0m")
    time.sleep(0.75)
    print("\033[94m\n\t   Aliana's \033[0m")
    time.sleep(0.75)
    print("\033[92m\n\t    Shop \033[0m")
    time.sleep(0.75)

def main_menu():
    print("\n\t Main Menu")
    print("""
        [0] - Save And Exit 
        [1] - Product 
        [2] - Courier 
        [3] - Order 
    """)
    
    main_menu_options = int(input("""\n\tEnter Your Option Here: """))

    if main_menu_options == 0:
        save_list('product_list.csv', product_list)
        save_list('courier_list.csv', courier_list)
        save_list('orders_list.csv', orders_list)
        whitespace()
        print('\tThanks For visiting! Goodbye.')
        whitespace()
        exit()
    
    elif main_menu_options == 1:
        product_menu()   
        
    elif main_menu_options == 2:
        courier_menu()
    
    elif main_menu_options == 3:
        orders_details()
        
    else:
        print (('\n\t"Invalid choice. Enter options 0-3"'))
        whitespace()
        main_menu()   
        

def neat_list(list_to_print):
    for item in list_to_print:
        output = ''
        for k,v in item.items():
            output+= f'{k}: {v}'
            output+='\n'
        print(output)


def product_menu():
    print("\n\t Product Menu")
    print('''
        [0] - Return to Main Menu
        [1] - View Menu
        [2] - Create A New Product
        [3] - Update Existing Product    
        [4] - Delete a Product''')
    whitespace()
    user_input = int(input("""\n\tEnter Your Choice Here: """))
        
        
    if user_input == 0:
        main_menu()
    
    elif user_input == 1:
        read_product_from_db()
        product_menu()
    
    elif user_input == 2:
        print('\n\tHere Is The Product Menu:')
        read_product_from_db()
        new_product = input('\n\tPlease Add A New Product To The List : ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))
        write_into_product_db(new_product, new_price)
        print('\n\tHere Is The New Product Menu:\n\t')
        read_product_from_db()
        product_menu()
        
    elif user_input == 3:
        print('Here Is The Product Menu: ')
        read_product_from_db()
        product_id = int(input('Choose The Product ID: '))
        new_product = input('Enter A Name For Your Product: ')
        new_price = (input('Enter A Price: '))
        update_into_product_db(new_product, new_price, product_id)
        print('Here Is The Updated Product Menu: ')
        read_product_from_db()
        product_menu()
        
    elif user_input == 4:
        print('\n\tHere Is The Product Menu:')
        read_product_from_db()
        deleted_input = int(input('\n\tSelect A Product To Delete: '))
        delete_product_from_db(deleted_input)
        print('\n\tHere Is The New Product Menu: ')
        read_product_from_db()
        product_menu()
    
    else:
        print(('\n\t"Invalid choice. Enter options 0-4"'))
        product_menu()

def courier_menu():
    print("\n\t Courier Menu")
    print('''
        [0] - Return to Main Menu
        [1] - Print Couriers List
        [2] - Create A New Courier
        [3] - Update Courier
        [4] - Delete Courier
        ''')
    
    user_input = int(input("""\n\tEnter Your Choice Here: """))
    
    if user_input == 0:    
        whitespace()
        print('Thanks For Visiting! Goodbye.')
        whitespace()
        main_menu()
    
    elif user_input == 1:
        read_courier_from_db()
        courier_menu()
    
    elif user_input == 2:
        print('\n\tHere Is The Courier List:\n\t')
        read_courier_from_db()
        new_courier = input('\n\tPlease Enter The Name Of The Courier : ')
        new_number = (float(input('\n\tPlease Enter Their Number: ')))
        write_into_courier_db(new_courier, new_number)
        print('\n\tHere Is The New Courier List: ')
        read_courier_from_db()
        courier_menu()
    
    elif user_input == 3:
        print('Here Is The Courier List: ')
        read_courier_from_db()
        courier_id = int(input('Choose Courier ID: '))
        new_courier = input('Enter A New Courier Name: ')
        new_number = (input('Enter A New Courier Number: '))
        update_into_courier_db(new_courier, new_number, courier_id)
        print('Here Is The Updated Menu: ')
        read_courier_from_db()
        courier_menu()
    
    elif user_input == 4:        
        read_courier_from_db()
        deleted_input = int(input('\n\tSelect a courier to delete: '))
        delete_courier_from_db(deleted_input)
        print('\n\tHere Is The New Product Menu: ')
        read_courier_from_db()
        courier_menu()
    
    else:
        print('\n\t"Invalid choice. Enter options 0-4"')
        courier_menu()

def orders_details():
    print("\n\t Order Menu")
    print('''
        [0] Return To Main Menu
        [1] View Order List
        [2] Create A New Order
        [3] Update A Specific Order Status
        [4] Update Existing Order 
        [5] Delete An Order''')
    
    user_input = int(input("""\n\tEnter Your Choice Here: """))
    
    if user_input == 0:
        main_menu()
    
    elif user_input == 1:
        neat_list(orders_list)
    
    elif user_input == 2:
        customer_name = input('\n\tPlease Enter Your Name: ')
        customer_address = input('\n\tPlease Enter Your Address: ')
        customer_phone_number = int(input('\n\tPlease Enter A Phone Number: \n\t'))
        
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
        enumerate_orders(order_status)
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
        print("Your Order No Longer Exists:\n\t")
        
        for key, value in enumerate(orders_list):
            print(f'Order Number - {key}{value}\n\t')
        orders_details()
    
    else:
        ('\n\t"Invalid choice. Enter options 0-5"')
        whitespace()
        orders_details()

new_welcome()
main_menu()