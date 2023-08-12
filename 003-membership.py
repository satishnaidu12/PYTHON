#!/usr/bin/python3.10
db_users=['db_admin','db_conf','db_installation']
random_user="db_admin"
if random_user in db_users:
    print("yes this user is allowed to start db")
else:
    print('this user is not a valid db user')
if random_user not in db_users:
    print("yes this user is allowed to start db")
else:
    print('this user is not a valid db user')
