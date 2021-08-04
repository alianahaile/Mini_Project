import csv
from Functions import read_csv_file, save_list, append_dict, update_dict, delete_index, enumerate_orders, whitespace
from pprint import pprint

order_list = []
product_list = []
courier_list = []
order_status = ['Preparing', 'Quality checks','Driver on the way', 'Delivered']

order_list = read_csv_file('Order_list.csv', order_list)
product_list = read_csv_file('Product_list.csv', product_list)
courier_list = read_csv_file('Courier_list.csv', courier_list)


def main():
    print("\n\tMain Menu")
    print("""
        [0] - To save and exit
        [1] - Product options
        [2] - Courier options
        [3] - Order options""")
    option = int(input("""\n\tEnter your choice here: """))
    if option == 0:
        save_list('Order_list.csv', order_list)
        save_list('Product_list.csv', product_list)
        save_list('Courier_list.csv', courier_list)
        print('\n\tGoodbye')
        exit()
    elif option == 1:
        product()
    elif option == 2:
        courier()
    elif option == 3:
        order()
    else:
        print('Please input a valid input')
        main()
        


print('\n\tProduct options')
    print('''
        [0]: To Return To The Main Menu
        [1]: To View Beverage List
        [2]: To Update Existing Drinks Menu
        [3]: To List & Replace A Drink
        [4]: To Delete A Drink''')
    user_input = int(input('\n\tSelect from the options above: '))
    if user_input == 0:
        main()
    elif user_input == 1:
        print("\n\tHere's The Beverage List\n\t")
        pprint(product_list)
        product()
    elif user_input == 2:
        print('\n\tHere Ts The Beverage List\n\t')
        pprint(product_list)
        new_product = input('\n\tPlease Add A New Beverage To The List : ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))
        new_dict = {}
        new_dict['Name'] = new_product
        new_dict['Price'] = new_price
        headers = ['Name', 'Price']
        append_dict('Product_list.csv', new_dict, headers)
        print("\n\tYou've Added A Beverage To The List:", new_dict)
        product()
    elif user_input == 3:  # Check is \n still needs to be here
        print('\n\tThe Beverage Selections Are: \n\t')
        enumerate_orders(product_list)
        number_input = float(
            input('\n\tChoose A Number To Replace With Another Beverage: '))
        new_variable = product_list[number_input]
        update_dict(new_variable)
        print("\n\tHere's The Updated Beverage List:\t\n")
        pprint(product_list)
        product()
    elif user_input == 4:
        print('\n\tLets delete a beverage\n\t')
        enumerate_orders(product_list)
        deleted_input = int(
            input('\n\tSelected a beverage to be deleted by choosing a number: '))
        whitespace()
        delete_index(product_list, deleted_input)
        print("\n\tYour Chosen Beverage Has Been Deleted\n\t")
        enumerate_orders(product_list)
        product()
    else:
        print('Invalid selection')
        product()


