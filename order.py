from datetime import datetime
import import_ipynb
import cart
import menu

# Create dictionary for cart
order_dict = []
order_id = 0


def CreateOrderid():
    global order_id

    if order_id == 0:
        order_id = 1  # generate cart id
    else:
        order_id += 1


def CreateOrder(orderid, customer_id):
    '''Place order and create orderid, cust_id,
     order_date, orderitems, total_price'''

    temp_order_dict = {'orderitems': []}
    temp_order_dict['orderid'] = orderid  # add the order id to dictionary
    temp_order_dict['cust_id'] = customer_id  # add customer id

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    temp_order_dict['order_date'] = dt_string  # add date
    # {{'menu_id':1, 'item_name':'coffee' 'quantity':2, 'cost':90, 'total_cost':180}}

    menuitem = cart.get_menuitem_from_cart(
        customer_id)  # function called from cart module

    total_price_of_order = 0

    for item in menuitem:
        orderitems = {}  # create new dictionary to append in order dictionary
        # function called from menu module
        df_menu = menu.get_menuitem_detail(item['menu_id'])

        orderitems['menu_id'] = item['menu_id']
        orderitems['item_name'] = df_menu.iloc[0][0]
        orderitems['quantity'] = item['quantity']
        orderitems['cost'] = df_menu.iloc[0][1]
        orderitems['total_cost'] = item['quantity'] * df_menu.iloc[0][1]
        # add order from cart in order dictionary
        temp_order_dict['orderitems'].append(orderitems)
        total_price_of_order = total_price_of_order + orderitems['total_cost']

    temp_order_dict['total_price'] = total_price_of_order
    order_dict.append(temp_order_dict)
    # print(order_dict)


def Order_details(order_id):
    '''Get list of orders for particular customer'''
    for order in order_dict:
        if order['orderid'] == order_id:
            return order

# CreateOrderid()
#CreateOrder(1, 1)
# CreateOrderid()
#CreateOrder(2, 2)
# Order_details(2)


def order_summary():
    '''List of order summmary'''
    order_summary = []
    for order in order_dict:
        tmp_order_summary = {}
        tmp_order_summary['Orderid'] = order['orderid']
        tmp_order_summary['order_date'] = order['order_date']
        tmp_order_summary['total_order_price'] = order['total_price']
        order_summary.append(tmp_order_summary)
