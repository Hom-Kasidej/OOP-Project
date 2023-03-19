import Class as C

dict1 = {
    'Dealer1' : {
    'name' : 'Johnny Peepo',
    'profile_image': 'None',
    'gender' : 'male',
    'birth_date' : '01/01/2001',
    'info' : 'i love cars',
    'username' : 'johnnysoodlo',
    'password' : 'johnny123',
    'car_list' : []
    },
    'Dealer2' : {
    'name' : 'Somchai Hi',
    'profile_image': 'None',
    'gender' : 'male',
    'birth_date' : '11/12/1974',
    'info' : 'Hi',
    'username' : 'somchai911',
    'password' : 'jgdsg1231',
    'car_list' : []
    },
    'Dealer3' : {
    'name' : 'Naruto Sasuke',
    'profile_image': 'None',
    'gender' : 'male',
    'birth_date' : '11/12/1950',
    'info' : 'Hi hello',
    'username' : '1qgqgqwg',
    'password' : 'aegki12124',
    'car_list' : []
    },
    'Dealer4' : {
    'name' : 'Somsri Haha',
    'profile_image': 'None',
    'gender' : 'female',
    'birth_date' : '20/12/1999',
    'info' : 'Hi wassup',
    'username' : 'waegweg134',
    'password' : '12412hlkk',
    'car_list' : []
    }
    

}

dealer1 = C.Dealer(**dict1['Dealer1'])
dealer2 = C.Dealer(**dict1['Dealer2'])
dealer3 = C.Dealer(**dict1['Dealer3'])
dealer4 = C.Dealer(**dict1['Dealer4'])
