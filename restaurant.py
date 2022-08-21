from venv import create
import pandas as pd
import customer
import menu
import cart
import order
import admin


def main():

    # Login Details
    while True:
        login = input(
            "Welcome to Nimblity, Please select the user type(Customer/ Admin)-")
        if (login.lower() == 'customer'):
            display_customer_menu()
            break
        elif (login.lower() == 'admin'):
            display_admin_menu()
            break
        else:
            continue


def display_cart(cust_id):
    '''Display menu items in cart'''
    dcartmenu = {"Menuid": [], "Name": [], "Cost": [], "Quantity": []}

    ret_val = cart.check_cart_empty(cust_id)
    if (0 == ret_val):
        return 0

    total_cost = 0
    # to check wether the customer has cart
    cartid = cart.get_cart_for_customer(cust_id)
    if (0 == cartid):
        return 0
    cartmenu = cart.get_menuitem_from_cart(cust_id)
    if (0 == cartmenu):
        return 0
    elif (len(cartmenu) > 0):
        for item in cartmenu:
            df_menudetail = menu.get_menuitem_detail(item['menu_id'])
            dcartmenu['Menuid'].append(item['menu_id'])
            dcartmenu['Name'].append(
                df_menudetail.loc[item['menu_id'], 'item_name'])
            dcartmenu['Cost'].append(
                df_menudetail.loc[item['menu_id'], 'cost'])
            dcartmenu['Quantity'].append(item['quantity'])
            total_cost = total_cost + \
                item['quantity'] * (df_menudetail.loc[item['menu_id'], 'cost'])

        df_cart = pd.DataFrame(dcartmenu)
        df_cart = df_cart.set_index('Menuid')
        print(df_cart)                      # display items in cart
        print("\nTotal Cost : {}".format(total_cost))


def display_customer_menu():
    ''' Display menu for customer login'''
    while True:
        cust_username = input("Hello Customer, Please enter your registered username –")
        cust_password = input("Please Enter your password –")
        customer_id = customer.customer_login(cust_username, cust_password)
        if customer_id == 0:
            print("Invalid username or password")
        else:
            break
    retval_display_admin_menu = 0
    while True:
        print("\n\nPlease select an option from the following –")
        print("1. View the menu card")
        print("2. Add items into the cart")
        print("3. Remove something from the cart")
        print("4. Display items in cart")
        print("5. Place the order")
        print("6. Logout")
        print("0. To 'exit'")
        option = input('Enter your choice: ')
        if option == "":
            print("Invalid option selected")
            continue
    
        if 0 == int(option):
            break
        elif 1 == int(option):  # View Menu
            df_menuitem = menu.view_menu()
            print(df_menuitem)
        elif 2 == int(option):  # Add item in cart
            while True:
                menuid = input("Enter item id :")
                qty = input("Enter quantity :")

                #
                # Error handling
                #
                input_val_id = menuid.isnumeric()
                input_val_qty = qty.isnumeric()
                if False == input_val_id or input_val_qty == False:
                    print("Given input value should be an integer....")
                    continue

                retval_id = menu.get_menuitem_detail(int(menuid))
                if len(retval_id) == 0:
                    print("\n Menu id {} does not exist\n".format(menuid))
                    continue

                cart.additem_incart(
                    customer_id, {'menu_id': int(menuid), 'quantity': int(qty)})
                bval = input("Do you want to add more items in cart (y/n)")
                if (bval == 'n'):
                    break

        elif 3 == int(option):  # remove item from cart
            #print("Menuid      Name     Cost     Quantity\n")
            retval = display_cart(customer_id)
            if (0 == retval):
                print("No items in cart to remove....")
                continue

            while True:
                menuid = int(input("Enter item id :"))
                cart.removeitem_fromcart(customer_id, menuid)
                retval = display_cart(customer_id)
                if (0 == retval):
                    print("No items in cart to remove....")
                    break
                else:
                    bval = input(
                        "Do you want to remove more items in cart (y/n)")
                    if (bval == 'n'):
                        break

        elif 4 == int(option):     # Display items in cart
            retval = display_cart(customer_id)
            if (0 == retval):
                print("No items in cart......")
                continue

        elif 5 == int(option):  # Place order item  from cart
            ret_val = cart.check_cart_empty(customer_id)
            if (0 == ret_val):
                print("Cart Empty. Order cannot be placed")
                continue
            order.CreateOrderid()
            order.CreateOrder(order.order_id, customer_id)
            display_order_detail(order.order_id)
            cart.delete_cart(customer_id)

        elif 6 == int(option):
            while True:
                login = input(
                    "Welcome to Nimblity, Please select the user type(Customer/ Admin)-")
                if login.lower() == 'customer':
                    display_customer_menu()
                    break
                elif (login.lower() == 'admin'):
                    retval_display_admin_menu = display_admin_menu()
                    break
                else:
                    continue
        if (-1 == retval_display_admin_menu):
            break
       # else:
        #    print(f'Not a correct choice: <{int(option)}>,try again')


def display_admin_menu():
    ''' Display menu for admin login'''
    while True:
        admin_username = input(
            "Hello admin, Please enter your registered username –")
        admin_password = input("Please Enter your password –")
        admin_id = admin.admin_login(admin_username, admin_password)
        if admin_id == 0:
            print("Invalid username or password")
            continue
        else:
            break

    while True:
        print("\n\nPlease select an option from the following –")
        print("1. Check summery of all orders")
        print("2. Check order details of an order")
        #print("3. Generate Bill")
        print("0: Exit")
        choice = input("Enter choice :")
        if choice == "":
            print("Invalid option selected")
            continue
        
        if int(choice) == 1:
            if(len(order.order_dict) <= 0):
                print("No order placed")
                continue
            for temporder in order.order_dict:
                print("*" * 30)
                print('Customer Name: {}'.format(
                    customer.get_customer_name(temporder['cust_id'])))
                print('Order No: {}'.format(temporder['orderid']))
                print('Ordered at -{}'.format(temporder['order_date']))
                print('Ordered at -{}'.format(temporder['total_price']))
                print("*" * 30)
                print('Item Ordered –')

        elif int(choice) == 2:
            input_order_id = input("Enter the order id: ")
            display_order_detail(int(input_order_id))
        elif int(choice) == 0:
            return -1

        # elif int(choice) == 3:


def display_order_detail(order_id):
    '''Display order detail for given order id'''
    if(len(order.order_dict) <= 0):
        print("No order placed")
        return 0

    for temporder in order.order_dict:
        if temporder['orderid'] == order_id:
            print("*" * 30)
            print('Order No: {}'.format(order_id))
            print('Customer Name: {}'.format(
                customer.get_customer_name(temporder['cust_id'])))
            print('Ordered at -{}'.format(temporder['order_date']))
            print("*" * 30)
            #print('Item Ordered –')

            #print('S.No.     Item Name     Qty.     Price')
            dorder = {"S.No": [], "Item Name": [], "Qty.": [], "Price": []}
            sno = 1
            for orderitem in temporder['orderitems']:
                dorder['S.No'].append(sno)
                dorder['Item Name'].append(orderitem['item_name'])
                dorder['Qty.'].append(orderitem['quantity'])
                dorder['Price'].append(orderitem['total_cost'])
                sno = sno + 1
            df_order = pd.DataFrame(dorder)
            df_order = df_order.set_index('S.No')
            print(df_order)
            print("\n Total Cost : {}".format(temporder['total_price'])),
            print("*" * 30)


if __name__ == '__main__':
    main()
