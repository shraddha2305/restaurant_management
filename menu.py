import pandas as pd

# create dictionary for resturant menu items
menu_item = {'menu_id': [1, 2, 3, 4, 5, 6, 7, 8],
             'item_name': ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake'],
             'cost': [90, 40, 80, 50, 50, 20, 100, 30]}

# Data frame for menu items
df_menu_item = pd.DataFrame(menu_item)
df_menu_item = df_menu_item.set_index('menu_id')

#
# Function to view menu item
#


def view_menu():
    '''Function return data frame of menu item'''
    return df_menu_item

#
# Function to get menu details for the given id
# Ex. [1   coffee 90]
#


def get_menuitem_detail(menuid):
    ''' Function return a row for the menuid given, if
    menu id not present function return empty dataframe'''

    if menuid in df_menu_item.index:
        return df_menu_item.loc[[menuid]]
    else:
        return pd.DataFrame()
