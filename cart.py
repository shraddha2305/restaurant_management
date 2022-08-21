from datetime import datetime

# Create dictionary for cart
cart_dict = []

#
# Function to add an item from cart
#
def additem_incart(custid, dict_menuitem):
    '''add selected item form menu in cart.'''

    selected_cart_id = get_cart_for_customer(custid)
    if(selected_cart_id == 0):
        selected_cart_id = custid
        temp_cart_dict = {'menuitems': []}

        # add the cart id to dictionary
        temp_cart_dict['cartid'] = selected_cart_id
        temp_cart_dict['cust_id'] = custid  # add custid

        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        temp_cart_dict['cart_date'] = dt_string  # add date

        # assign menu item : id and quantity list
        temp_cart_dict['menuitems'].append(dict_menuitem)

        cart_dict.append(temp_cart_dict)
       # print(cart_dict)
    else:
        for cart in cart_dict:
            if(cart['cartid'] == selected_cart_id):
                cart['menuitems'].append(dict_menuitem)


# Tesing Purpose

# CreateCartid()
# additem_incart(1, 1, {'menu_id':1, 'quantity':1})
# additem_incart(1, 1, {'menu_id':2, 'quantity':1})
# additem_incart(1, 1, {'menu_id':3, 'quantity':2})
# CreateCartid()
# additem_incart(2, 2, {'menu_id':4, 'quantity':2})
# print(cart_dict)

#
# Function to remove an item from cart
#
def removeitem_fromcart(cust_id, menuItemId):
    '''remove an item from cart'''
    cartid = get_cart_for_customer(cust_id)
    # Using loop
    # Find dictionary matching value in list
    for cart in cart_dict:
        if cart['cartid'] == cartid:
            for menuItem in cart['menuitems']:
                if menuItem['menu_id'] == menuItemId:
                    cart['menuitems'].remove(menuItem)
            break
   

#
# Function to check cart empty for the customer
#
def check_cart_empty(customer_id):
    '''Delete cart after the order is placed'''
    cartid = get_cart_for_customer(customer_id)
    # Using loop
    # Find dictionary matching value in list
    for cart in cart_dict:
        if cart['cartid'] == cartid:
            if (len(cart['menuitems']) == 0):
                return 0


#
# Function to get menu item list from cart
#
def get_menuitem_from_cart(cust_id):
    ''' This return dictionary of menu items from cart 
    for customer id given'''
    cartid = get_cart_for_customer(cust_id)
    if (cartid == 0):
        return 0

    for cart in cart_dict:
        if cart['cartid'] == cartid:
            return cart['menuitems']


#
# Function to get the  cart for the customer
#
def get_cart_for_customer(customer_id):
    for cart in cart_dict:
        if cart['cust_id'] == customer_id:
            return cart['cartid']
    return 0

#
# Function to get the  cart for the customer
#
def delete_cart(customer_id):
    for cart in cart_dict:
        if cart['cust_id'] == customer_id:
            cart_dict.remove(cart)
    