import Class as C

dict1 = {
    'Dealer1' : {
        'name' : 'Johnny Peepo',
        'profile_image': 'None',
        'gender' : C.EClass.Gender.Male,
        'birth_date' : '01/01/2001',
        'info' : 'i love cars',
        'username' : 'johnnysoodlo',
        'password' : 'johnny123',
    },
    'Dealer2' : {
        'name' : 'Somchai Hi',
        'profile_image': 'None',
        'gender' : C.EClass.Gender.Male,
        'birth_date' : '11/12/1974',
        'info' : 'Hi',
        'username' : 'somchai911',
        'password' : 'jgdsg1231',
    },
    'Dealer3' : {
        'name' : 'Naruto Sasuke',
        'profile_image': 'None',
        'gender' : C.EClass.Gender.Male,
        'birth_date' : '11/12/1950',
        'info' : 'Hi hello',
        'username' : '1qgqgqwg',
        'password' : 'aegki12124',
    },
    'Dealer4' : {
        'name' : 'Somsri Haha',
        'profile_image': 'None',
        'gender' : C.EClass.Gender.Female,
        'birth_date' : '20/12/1999',
        'info' : 'Hi wassup',
        'username' : 'waegweg134',
        'password' : '12412hlkk',
    }
}

dealer_list = []

for dealer in dict1:
    dealer_list.append(C.Dealer(**dict1[dealer]))