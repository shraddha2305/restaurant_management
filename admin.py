import pandas as pd
import numpy as np

admin_dict = {'admin_id': [1],
              'name': ['admin'],
              'password': ['admin']}

df_admin = pd.DataFrame(admin_dict)
df_admin = df_admin.set_index('admin_id')


def admin_login(username, password):
    '''Check for validity of customer'''
    sub_df_admin = df_admin[df_admin['name'] == username.lower()]
    if (len(sub_df_admin) > 0):
        if sub_df_admin['password'].values[0] == password.lower():
            admin_id = sub_df_admin.index
            return admin_id[0]
        else:
            return 0
    else:
        return 0
