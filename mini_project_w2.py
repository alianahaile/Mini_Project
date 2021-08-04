#products name
products_list = []
with open('products.txt') as load_products_file:
    for load_i in load_products_file.readlines():
        products_list.append(load_i.rstrip()) 

#couriers name
couriers_list = []
with open('couriers.txt') as load_couriers_file:
    for load_w in load_couriers_file.readlines():
        couriers_list.append(load_w.rstrip())

print ("'Thanks for visiting!. Goodbye.")  

#main_menu_function
def main_menu(): 
        main_menu_options = int(input('''
        [0] Exit
        [1] Product
        \nEnter your choice here:'''))  

        if main_menu_options == 1: 
            print(products_list)
            product_menu()

        elif main_menu_options == 0: 
            print("App exited")

        else:
            print("Invalid choice. Enter options 0-1")
            main_menu()

#product_menu_function
def product_menu():
    print('''
        [0] - Return to Main Menu
        [1] - View Menu
        [2] - Create New Product
        [3] - Update Existing Product    
        [4] - Delete a Product''')
    whitespace()
    user_input = int(input("""\n\tEnter your choice here: """))
    
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



#courier_menu_function
def courier_menu():
    print('''
        [0] - Return to Main Menu
        [1] - Print Couriers List
        [2] - Create New Courier
        [3] - Update Courier
        [4] - Delete Courier
        ''')
    
    user_input = int(input("""\\n\tEnter your choice here:"""))
    
    if user_input == 0:
        main_menu()

    elif user_input == 1:
        print (couriers_list)

    elif user_input == 2:
        new_courier = input ("please enter new courier's name:")
        couriers_list.append(new_courier)
        print(f'courier "{new_courier}" successfully added.')

    elif user_input == 3:
        for value, courier in enumerate(couriers_list):
            print(value, courier)
            update_index = int(input('select courier number to update:'))
            updated_courier_name = input('please enter new courier name:')
            couriers_list[update_index] = updated_courier_name
            print (f'courier updated to "{updated_courier_name}".')

    elif user_input == 4:
        for value, courier in enumerate(couriers_list):
            print(value,courier)
            delete_index = int(input('select courier number to delete:'))
            delete_item = couriers_list[delete_index]
            print (f' The New courier List {couriers_list}')

    else:
        print("Invalid choice. Enter options 0-4")
    courier_menu()


print()
main_menu()
product_menu()
courier_menu()
main_menu_options = int(input("Enter your option:"))

print ("Thanks for using this app. Goodbye.")  