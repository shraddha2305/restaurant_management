import pandas as pd
import numpy as np

customer_dict = {'cust_id': [1, 2],
                 'name': ['xyz', 'abc'],
                 'password': ['xyz', 'abc']}


# Dataframe created for customer details
df_customer = pd.DataFrame(customer_dict)
df_customer = df_customer.set_index('cust_id')

#
# Function to view customer details
#


def view_customer():
    '''Display the list of customer'''
    print(df_customer)

#
# Function to verify customer login
#


def customer_login(username, password):
    '''Check for validity of customer'''
    sub_df_customer = df_customer[df_customer['name'] == username.lower()]
    if (len(sub_df_customer) > 0):
        if sub_df_customer['password'].values[0] == password.lower():
            cust_id = sub_df_customer.index
            return cust_id[0]
        else:
            return 0
    else:
        return 0

#
# Function to get customer name for given customer id
#


def get_customer_name(customer_id):
    customername = df_customer.loc[customer_id, 'name']
    return customername
