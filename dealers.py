import Class as C

dict1 = {
    'Dealer1' : {
    'name' : 'Hi',
    'profile_image': 'None',
    'gender' : 'male',
    'birth_date' : '1111',
    'info' : 'Hi',
    'username' : 'Hi',
    'password' : 'Hi',
    'car_list' : []
    },
    'Dealer2' : {
    'name' : 'aafasfawf',
    'profile_image': 'None',
    'gender' : 'male',
    'birth_date' : '111213',
    'info' : 'Hi',
    'username' : 'aaddss',
    'password' : 'jgdsg1231',
    'car_list' : []
    },
    'Dealer3' : {
    'name' : 'aawdasd',
    'profile_image': 'None',
    'gender' : 'male',
    'birth_date' : '1134',
    'info' : 'Hi hello',
    'username' : '1qgqgqwg',
    'password' : 'aegki12124',
    'car_list' : []
    },
    'Dealer4' : {
    'name' : 'qqwtqegh2h',
    'profile_image': 'None',
    'gender' : 'female',
    'birth_date' : '1111',
    'info' : 'Hi',
    'username' : 'waegweg134',
    'password' : '12412h',
    'car_list' : []
    }
    

}

dealer1 = C.Dealer(**dict1['Dealer1'])
dealer2 = C.Dealer(**dict1['Dealer2'])
dealer3 = C.Dealer(**dict1['Dealer3'])
dealer4 = C.Dealer(**dict1['Dealer4'])
