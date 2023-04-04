from Class import *
import RenterInstance as r
import DealerInstance as d 

account_pool = System()
user_instance_list = r.renter_instance_list + d.dealer_instance_list
for acc in user_instance_list:
    account_pool.add_account(acc)

for acc in account_pool.get_account_list():
    print(acc.get_name())
me =  User()
me.register(account_pool)

for acc in account_pool.get_account_list():
    print(acc.get_name())

me = me.login(account_pool=account_pool)
