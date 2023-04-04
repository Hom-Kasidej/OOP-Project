import Class as c
import RenterInstance as r
import DealerInstance as d 

account_pool = c.Account()
user_instance_list = r.renter_instance_list + d.dealer_instance_list
for acc in user_instance_list:
    account_pool.add_to_account(acc)


for acc in account_pool.get_accounts():
    print(acc.get_name())
me = c.User()
me.register(account_pool)

for acc in account_pool.get_accounts():
    print(acc.get_name())

