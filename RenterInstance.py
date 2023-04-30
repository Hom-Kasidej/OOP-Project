import Class as C

renter_info_dict = {
    "Renter1" : {
        "name" : "Sompong Payongdej",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Male,
        "birth_date" : "28/02/1987",
        "info" : "Good guy",
        "username" : "Sompong",
        "password" : "ripperisthedog",
        "user_ID" : "1"
    },
    "Renter2" : {
        "name" : "Somsej Eatgrass",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Female,
        "birth_date" : "01/01/1999",
        "info" : "Capybaraaa",
        "username" : "GrossGrass",
        "password" : "iwantgrass555",
        "user_ID" : ""
    },
    "Renter" : {
        "name" : "Somjett DashForward",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Female,
        "birth_date" : "09/02/2000",
        "info" : "Get out of my way!",
        "username" : "Jett",
        "password" : "333Jettiseasytowin",
        "user_ID" : ""
    },
     "Renter4" : {
        "name" : "Gekko keeact",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Male,
        "birth_date" : "21/07/2002",
        "info" : "Let's go my buddy",
        "username" : "Anonymous",
        "password" : "OhhoMyBuddy",
        "user_ID" : ""
    },
    "Renter5" : {
        "name" : "MrBeast Latkrabang",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Male,
        "birth_date" : "11/11/1970",
        "info" : "Who want my money!!",
        "username" : "Beast",
        "password" : "1234567890",
        "user_ID" : ""
    },
    "Renter6" : {
        "name" : "RestWith OOP",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Female,
        "birth_date" : "19/03/2003",
        "info" : "OOP Project is waiting for you",
        "username" : "OOPInwZa",
        "password" : "KhorGradeANoiKrub55",
        "user_ID" : ""
    },
    "Renter7" : {
        "name" : "Somying butchai",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Female,
        "birth_date" : "20/09/1997",
        "info" : "I want cheap price",
        "username" : "Somying",
        "password" : "yinglowcost",
        "user_ID" : ""
    },
    "Renter8" : {
        "name" : "Somrew Lookmo",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Male,
        "birth_date" : "05/05/1955",
        "info" : "Parents give me money :)",
        "username" : "Want bullet?",
        "password" : "666satan666",
        "user_ID" : ""
    },
    "Renter9" : {
        "name" : "Respect Thailand",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Male,
        "birth_date" : "20/02/1969",
        "info" : "Long Live King",
        "username" : "LoveKing",
        "password" : "999KingKing",
        "user_ID" : ""
    },
     "Renter10" : {
        "name" : "Frog obob",
        "profile_image" : "",
        "gender" : C.EClass.Gender.Male,
        "birth_date" : "27/12/1975",
        "info" : "Born in R9",
        "username" : "King9",
        "password" : "loveKingThailand",
        "user_ID" : ""
    }
}

#Test 
renter_instance_list = []
for i in renter_info_dict:
    renter_instance_list.append(C.Renter(**renter_info_dict[i]))
