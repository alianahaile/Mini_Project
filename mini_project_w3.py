import csv

product_list = []
with open('products.txt') as load_products_file:
    for load_i in load_products_file.readlines():
        product_list.append(load_i.rstrip())
        

courier_list = []
with open('couriers.txt') as load_couriers_file:
    for load_w in load_couriers_file.readlines():
        courier_list.append(load_w.rstrip())
        

with open('order_list.csv') as file1:
    orders_list = list(csv.DictReader(file1))
    print(orders_list)



#main_menu_function
def main_menu(): 
    print("""
        [0] Exit App                           
        [1] Product Options
        [2] Courier Options
        [3] Order Details
    """)
    main_menu_options = int(input('Enter your option here:'))
    
    if main_menu_options == 0:
        with open('Product_list.txt', 'w') as save_p_file:
            for save_i in product_list:
                save_p_file.write(save_i + '\n')

        with open('Courier_list.txt', 'w') as save_c_file:
            for save_w in courier_list:
                save_c_file.write(save_w + '\n')
        
        print("\n Thanks for Visiting! Goodbye.")
        print("")
        exit 
    
    elif main_menu_options == 1:
        product_menu()   
        
    elif main_menu_options == 2:
        courier_menu()
    
    elif main_menu_options == 3:
        orders_details()

orders_list = [{
    "customer name": "John",
    "customer address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer phone": "07887356474",
    "courier": [courier_list[2]],  #i don't get this 
    "status": [orders_list[0]],
},
    {
    "customer name": "Sanier",
    "customer address": "2, Elm Street, Manchester, M1 1AD",
    "customer phone": "07894876431",
    "courier": [courier_list[0]], #i don't get this 
    "status": [orders_list[1]],
}
]

def listing_orders(order):
    for key, value in enumerate(order):
        print(f'\nOrder number: {key} - {value}')

def orders_details():
    print('\n\tOrder Menu')
    print('''
        [0] Return To Main Menu
        [1] View Order List
        [2] Enter Order Details
        [3] Update A Specific Order Status
        [4] Update Existing Order 
        [5] Delete An Order''')
    
    user_input = int(input("""\\n\tEnter your choice here: """))
    
    if user_input == 0:
        return main_menu()
    elif user_input == 1:
        print(orders_list)
    elif user_input == 2:
        entry = {}
        customer_name = input('Enter you name: ')
        customer_address = input('Enter your address: ')
        phone_number = int(
            input('Enter your mobile number: '))
        for key, value in enumerate(courier_list):
            print(key, value)
        selected_courier = int(input('Select a courier for delivery: '))
        entry['Customer'] = customer_name
        entry['Customer address'] = customer_address
        entry['Customer phone'] = phone_number
        entry['courier'] = selected_courier
        entry['Status'] = order_status[0]
        orders_list.append(entry)
    elif user_input == 3:
        listing_orders(orders_list)
        order_index = int(input('\nPlease choose which order to adjust:  '))
        print('')
        for key, value in enumerate(order_status):
            print(key, value)
            status_input = int(
            input('\nChoose an order status to update on the order list: '))
        order_update = orders_list[order_index]
        order_update['status'] = order_status[status_input]
    elif user_input == 4:
        for key, value in enumerate(orders_list):
            print(key, value)
        order_index = int(
            input("\nPlease select the order you'd like to update: "))
        chosen_order = orders_list[order_index]
        for key, value in chosen_order.items():
            chosen_value = input(
                f'\n{key} Has value of {value}. Enter new value for {key}: ')
            if chosen_value == '':
                chosen_order[key] = value
                print('\nNothing has been changed')
            else:
                chosen_order[key] = chosen_value
        print(chosen_order)
    elif user_input == 5:
        listing_orders(orders_list)
        delete_order = int(
            input('\nPlease choose which order to delete by its order number: '))
        del orders_list[delete_order]
        print(orders_list)