#Product names
products_list = [ 'Tea', 'Espresso', 'Cold Brew' 'Latte', 'Cappuccino', 'Hot Chocolate' ]
# Get user input for main menu option
# If user input is 0:
# Exist app

# #main_menu_function
def main_menu(): 
        main_menu_options = int(input('''
        1. Product Menu Options
        2. Exit App
        \nSelect your option:'''))  

        if main_menu_options == 1: 
            print(products_list)
            product_menu()

        elif main_menu_options == 0: 
            print("App exited")
            exit

        else:
            print("Invalid choice. Enter options 0-1")
            main_menu()

def product_menu():
    user_input = int(input(''' 
    0: To Return To The Main Menu")
    1: To View The Current Drinks list")
    2: To List And Replace A Drink")
    3: To Update The Existing Drinks List")
    4: To Delete A Drink")
    \n Please Select from the options above:'''))
    
    if user_input == 0:
        main_menu()

    elif user_input == 1:
        print (products_list)

    elif user_input == 2:
        new_product = input ("please enter new product's name:")
        products_list.append(new_product)
        print(f'product "{new_product}" successfully added.')

    elif user_input == 3:
        for value, product in enumerate(products_list):
            print(value, product)
            update_index = int(input('select product number to update:'))
            updated_product_name = input('please enter new product name:')
            products_list[update_index] = updated_product_name
            print (f'product updated to "{updated_product_name}".')

    elif user_input == 4:
        for value, product in enumerate(products_list):
            print(value,product)
            delete_index = int(input('select product number to delete:'))
            delete_item = products_list[delete_index]
            print (f' The New Product List {products_list}')

    else:
        print("Invalid choice. Enter options 0-4")
    product_menu()


print()
# main_menu()
product_menu()
main_menu_options = int(input("Enter your option:"))

print ("Thanks for using this app. Goodbye.")   




