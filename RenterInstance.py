import Class as C

renter_info_dict = {
    "Renter1" : {
        "name" : "สมปอง พยองเดช",
        "profile_image" : "",
        "gender" : C.Gender.Male,
        "birth_date" : "28/02/1987",
        "info" : "คนดีย์",
        "username" : "Sompong",
        "password" : "ripperisthedog"
    },
    "Renter2" : {
        "name" : "สมเสร็จ กินหญ้า",
        "profile_image" : "",
        "gender" : C.Gender.Female,
        "birth_date" : "01/01/1999",
        "info" : "Capybaraaa",
        "username" : "GrossGrass",
        "password" : "iwantgrass555"
    },
    "Renter" : {
        "name" : "สมเจ็ท แดชหน้า",
        "profile_image" : "",
        "gender" : C.Gender.Female,
        "birth_date" : "09/02/2000",
        "info" : "Get out of my way!",
        "username" : "Jett",
        "password" : "333Jettiseasytowin"
    },
     "Renter4" : {
        "name" : "Gekko keeact",
        "profile_image" : "",
        "gender" : C.Gender.Male,
        "birth_date" : "21/07/2002",
        "info" : "Let's go my buddy",
        "username" : "Anonymous",
        "password" : "OhhoMyBuddy"
    },
    "Renter5" : {
        "name" : "MrBeast Latkrabang",
        "profile_image" : "",
        "gender" : C.Gender.Male,
        "birth_date" : "11/11/1970",
        "info" : "Who want my money!!",
        "username" : "Beast",
        "password" : "1234567890"
    },
    "Renter6" : {
        "name" : "คิดจะพัก คิดถึงโอโอพี",
        "profile_image" : "",
        "gender" : C.Gender.Female,
        "birth_date" : "19/03/2003",
        "info" : "OOP Project is waiting for you",
        "username" : "OOPInwZa",
        "password" : "KhorGradeANoiKrub55"
    },
    "Renter7" : {
        "name" : "สมหญิง แต่เป็นชาย",
        "profile_image" : "",
        "gender" : C.Gender.Female,
        "birth_date" : "20/09/1997",
        "info" : "ขอเช่ารถถูกๆหน่อยจ้า",
        "username" : "Somying",
        "password" : "yinglowcost"
    },
    "Renter8" : {
        "name" : "สมเร็ว ลูกโม่",
        "profile_image" : "",
        "gender" : C.Gender.Male,
        "birth_date" : "05/05/1955",
        "info" : "บารมีพ่อแม่ :)",
        "username" : "ลูกโม่มั๊ยย",
        "password" : "666satan666"
    },
    "Renter9" : {
        "name" : "เคารพ ธงชาติ",
        "profile_image" : "",
        "gender" : C.Gender.Male,
        "birth_date" : "20/02/1969",
        "info" : "บารมีพ่อหลวง",
        "username" : "LoveKing",
        "password" : "999KingKing"
    },
     "Renter10" : {
        "name" : "นายกบ อ๊บอ๊บ",
        "profile_image" : "",
        "gender" : C.Gender.Male,
        "birth_date" : "27/12/1975",
        "info" : "ฉันเกิดในรัชกาลที่ 9",
        "username" : "King9",
        "password" : "loveKingThailand"
    }
}

#Test 
renter_instance_list = []
for i in renter_info_dict:
    renter_instance_list.append(C.Renter(**renter_info_dict[i]))
