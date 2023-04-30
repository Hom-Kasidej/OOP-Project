from enum import Enum


class CarBrand(Enum):
    Aston_martin = "Aston_martin"
    Audi = "Audi"
    BMW = "BMW"
    BYD = "BYD"
    Bentlay = "Bentlay"
    Chevrolet = "Chevrolet"
    Citroen = "Citroen"
    FOMM = "FOMM"
    Fiat = "Fiat"
    Ford = "Ford"
    GWM = "GWM"
    Honda = "Honda"
    Hyundai = "Hyundai"
    Isuzu = "Isuzu"
    Jaguar = "Jaguar"
    Jeep = "Jeep"
    Kia = "Kia"
    LDV = "LDV"
    Lamborgini = "Lamborgini"
    Land_Rover = "Land_Rover"
    Lexus = "Lexus"
    MG = "MG"
    Maserati = "Maserati"
    Mazda = "Mazda"
    Mercedes_Benz = "Mercedes_Benz"
    Mini = "Mini"
    Mitsubishi = "Mitsubishi"
    Nissan = "Nissan"
    Porsche = "Porsche"
    Rolls_Royce = "Rolls_Royce"
    Subaru = "Subaru"
    Suzuki = "Suzuki"
    Tesla = "Tesla"
    Toyota = "Toyota"
    Volvo = "Volvo"
    Other = "Other"


class GearType(Enum):
    Manual = "Manual"
    Auto = "Auto"


class FuelType(Enum):
    Benzien = "Benzien"
    Benzien_91 = "Benzien 91"
    Benzien_95 = "Benzien 95"
    Benzien_E20 = "Benzien E20"
    Benzien_E85 = "Benzien E85"
    CNG = "CNG"
    Diesel = "Diesel"
    Diesel_B10 = "Diesel B10"
    Diesel_B20 = "Diesel B20"
    Diesel_B5 = "Diesel B5"
    Diesel_B7 = "Diesel B7"
    Hybrid = "Hybrid"
    LPG = "LPG"
    NGV = "NGV"
    EV = "EV"
    Plugin_Hybrid = "Plugin Hybrid"


class GPSType(Enum):
    CarTrack = "CarTrack"
    Eyefleet = "Eyefleet"
    NoneGPS = "NoneGPS"
    Others = "Others"
    Otoplug = "Otoplug"


class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Others = "Others"


class Status(Enum):
    Canceled = "Canceled"
    Pending = "Pending"
    Success = "Success"


class ThailandProvince(Enum):
    Amnat_Charoen = "Amnat Charoen"
    Ang_Thong = "Ang Thong"
    Bangkok = "Bangkok"
    Bueng_Kan = "Bueng Kan"
    Buri_Ram = "Buri Ram"
    Chachoengsao = "Chachoengsao"
    Chai_Nat = "Chai Nat"
    Chaiyaphum = "Chaiyaphum"
    Chanthaburi = "Chanthaburi"
    Chiang_Mai = "Chiang Mai"
    Chiang_Rai = "Chiang Rai"
    Chon_Buri = "Chon Buri"
    Chumphon = "Chumphon"
    Kalasin = "Kalasin"
    Kamphaeng_Phet = "Kamphaeng Phet"
    Kanchanaburi = "Kanchanaburi"
    Khon_Kaen = "Khon Kaen"
    Krabi = "Krabi"
    Lampang = "Lampang"
    Lamphun = "Lamphun"
    Loei = "Loei"
    Lopburi = "Lopburi"
    Mae_Hong_Son = "Mae Hong Son"
    Maha_Sarakham = "Maha Sarakham"
    Mukdahan = "Mukdahan"
    Nakhon_Nayok = "Nakhon Nayok"
    Nakhon_Pathom = "Nakhon Pathom"
    Nakhon_Phanom = "Nakhon Phanom"
    Nakhon_Ratchasima = "Nakhon Ratchasima"
    Nakhon_Sawan = "Nakhon Sawan"
    Nakhon_Si_Thammarat = "Nakhon Si Thammarat"
    Nan = "Nan"
    Narathiwat = "Narathiwat"
    Nong_Bua_Lam_Phu = "Nong Bua Lam Phu"
    Nong_Khai = "Nong Khai"
    Nonthaburi = "Nonthaburi"
    Pathum_Thani = "Pathum Thani"
    Pattani = "Pattani"
    Phang_Nga = "Phang Nga"
    Phatthalung = "Phatthalung"
    Phayao = "Phayao"
    Phetchabun = "Phetchabun"
    Phetchaburi = "Phetchaburi"
    Phichit = "Phichit"
    Phitsanulok = "Phitsanulok"
    Phra_Nakhon_Si_Ayutthaya = "Phra Nakhon Si Ayutthaya"
    Phrae = "Phrae"
    Phuket = "Phuket"
    Prachin_Buri = "Prachin Buri"
    Prachuap_Khiri_Khan = "Prachuap Khiri Khan"
    Ranong = "Ranong"
    Ratchaburi = "Ratchaburi"
    Rayong = "Rayong"
    Roi_Et = "Roi Et"
    Sa_Kaeo = "Sa Kaeo"
    Sakon_Nakhon = "Sakon Nakhon"
    Samut_Prakan = "Samut Prakan"
    Samut_Sakhon = "Samut Sakhon"
    Samut_Songkhram = "Samut Songkhram"
    Saraburi = "Saraburi"
    Satun = "Satun"
    Sing_Buri = "Sing Buri"
    Sisaket = "Sisaket"
    Songkhla = "Songkhla"
    Sukhothai = "Sukhothai"
    Suphan_Buri = "Suphan Buri"
    Surat_Thani = "Surat Thani"
    Surin = "Surin"
    Tak = "Tak"
    Trang = "Trang"
    Trat = "Trat"
    Ubon_Ratchathani = "Ubon Ratchathani"
    Udon_Thani = "Udon Thani"
    Uthai_Thani = "Uthai Thani"
    Uttaradit = "Uttaradit"
    Yala = "Yala"
    Yasothon = "Yasothon"


class CarType(Enum):
    ANTIQUE = 'Antique'
    CAMPERVAN = 'Campervan'
    CITY = 'City'
    CONVERTIBLE = 'Convertible'
    COUPE = 'Coupe'
    SUV = 'SUV'
    VAN = 'Van'
    SEDAN = 'Sedan'
    OTHER = 'Other'


class CarColor(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    GOLD = "Gold"
    WHITE = "White"
    BLACK = "Black"
    GREY = "Grey"
    SILVER = "Silver"
    BROWN = "Brown"
    OTHER = "Other"


class CarBrand(Enum):
    Aston_martin = "Aston_martin"
    Audi = "Audi"
    BMW = "BMW"
    BYD = "BYD"
    Bentlay = "Bentlay"
    Chevrolet = "Chevrolet"
    Citroen = "Citroen"
    FOMM = "FOMM"
    Fiat = "Fiat"
    Ford = "Ford"
    GWM = "GWM"
    Honda = "Honda"
    Hyundai = "Hyundai"
    Isuzu = "Isuzu"
    Jaguar = "Jaguar"
    Jeep = "Jeep"
    Kia = "Kia"
    LDV = "LDV"
    Lamborgini = "Lamborgini"
    Land_Rover = "Land_Rover"
    Lexus = "Lexus"
    MG = "MG"
    Maserati = "Maserati"
    Mazda = "Mazda"
    Mercedes_Benz = "Mercedes_Benz"
    Mini = "Mini"
    Mitsubishi = "Mitsubishi"
    Nissan = "Nissan"
    Porsche = "Porsche"
    Rolls_Royce = "Rolls_Royce"
    Subaru = "Subaru"
    Suzuki = "Suzuki"
    Tesla = "Tesla"
    Toyota = "Toyota"
    Volvo = "Volvo"
    Other = "Other"


class GearType(Enum):
    Manual = "Manual"
    Auto = "Auto"


class FuelType(Enum):
    Benzien = "Benzien"
    Benzien_91 = "Benzien 91"
    Benzien_95 = "Benzien 95"
    Benzien_E20 = "Benzien E20"
    Benzien_E85 = "Benzien E85"
    CNG = "CNG"
    Diesel = "Diesel"
    Diesel_B10 = "Diesel B10"
    Diesel_B20 = "Diesel B20"
    Diesel_B5 = "Diesel B5"
    Diesel_B7 = "Diesel B7"
    Hybrid = "Hybrid"
    LPG = "LPG"
    NGV = "NGV"
    EV = "EV"
    Plugin_Hybrid = "Plugin Hybrid"


class GPSType(Enum):
    CarTrack = "CarTrack"
    Eyefleet = "Eyefleet"
    NoneGPS = "NoneGPS"
    Others = "Others"
    Otoplug = "Otoplug"


class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Others = "Others"


class Status(Enum):
    Canceled = "Canceled"
    Pending = "Pending"
    Success = "Success"


class ThailandProvince(Enum):
    Amnat_Charoen = "Amnat Charoen"
    Ang_Thong = "Ang Thong"
    Bangkok = "Bangkok"
    Bueng_Kan = "Bueng Kan"
    Buri_Ram = "Buri Ram"
    Chachoengsao = "Chachoengsao"
    Chai_Nat = "Chai Nat"
    Chaiyaphum = "Chaiyaphum"
    Chanthaburi = "Chanthaburi"
    Chiang_Mai = "Chiang Mai"
    Chiang_Rai = "Chiang Rai"
    Chon_Buri = "Chon Buri"
    Chumphon = "Chumphon"
    Kalasin = "Kalasin"
    Kamphaeng_Phet = "Kamphaeng Phet"
    Kanchanaburi = "Kanchanaburi"
    Khon_Kaen = "Khon Kaen"
    Krabi = "Krabi"
    Lampang = "Lampang"
    Lamphun = "Lamphun"
    Loei = "Loei"
    Lopburi = "Lopburi"
    Mae_Hong_Son = "Mae Hong Son"
    Maha_Sarakham = "Maha Sarakham"
    Mukdahan = "Mukdahan"
    Nakhon_Nayok = "Nakhon Nayok"
    Nakhon_Pathom = "Nakhon Pathom"
    Nakhon_Phanom = "Nakhon Phanom"
    Nakhon_Ratchasima = "Nakhon Ratchasima"
    Nakhon_Sawan = "Nakhon Sawan"
    Nakhon_Si_Thammarat = "Nakhon Si Thammarat"
    Nan = "Nan"
    Narathiwat = "Narathiwat"
    Nong_Bua_Lam_Phu = "Nong Bua Lam Phu"
    Nong_Khai = "Nong Khai"
    Nonthaburi = "Nonthaburi"
    Pathum_Thani = "Pathum Thani"
    Pattani = "Pattani"
    Phang_Nga = "Phang Nga"
    Phatthalung = "Phatthalung"
    Phayao = "Phayao"
    Phetchabun = "Phetchabun"
    Phetchaburi = "Phetchaburi"
    Phichit = "Phichit"
    Phitsanulok = "Phitsanulok"
    Phra_Nakhon_Si_Ayutthaya = "Phra Nakhon Si Ayutthaya"
    Phrae = "Phrae"
    Phuket = "Phuket"
    Prachin_Buri = "Prachin Buri"
    Prachuap_Khiri_Khan = "Prachuap Khiri Khan"
    Ranong = "Ranong"
    Ratchaburi = "Ratchaburi"
    Rayong = "Rayong"
    Roi_Et = "Roi Et"
    Sa_Kaeo = "Sa Kaeo"
    Sakon_Nakhon = "Sakon Nakhon"
    Samut_Prakan = "Samut Prakan"
    Samut_Sakhon = "Samut Sakhon"
    Samut_Songkhram = "Samut Songkhram"
    Saraburi = "Saraburi"
    Satun = "Satun"
    Sing_Buri = "Sing Buri"
    Sisaket = "Sisaket"
    Songkhla = "Songkhla"
    Sukhothai = "Sukhothai"
    Suphan_Buri = "Suphan Buri"
    Surat_Thani = "Surat Thani"
    Surin = "Surin"
    Tak = "Tak"
    Trang = "Trang"
    Trat = "Trat"
    Ubon_Ratchathani = "Ubon Ratchathani"
    Udon_Thani = "Udon Thani"
    Uthai_Thani = "Uthai Thani"
    Uttaradit = "Uttaradit"
    Yala = "Yala"
    Yasothon = "Yasothon"


class CarType(Enum):
    ANTIQUE = 'Antique'
    CAMPERVAN = 'Campervan'
    CITY = 'City'
    CONVERTIBLE = 'Convertible'
    COUPE = 'Coupe'
    SUV = 'SUV'
    VAN = 'Van'
    SEDAN = 'Sedan'
    OTHER = 'Other'


class CarColor(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    GOLD = "Gold"
    WHITE = "White"
    BLACK = "Black"
    GREY = "Grey"
    SILVER = "Silver"
    BROWN = "Brown"
    OTHER = "Other"


class CreditCard(Enum):
    MasterCard = "MasterCard"
    Visa = "Visa"
    JCB = "JCB"


class CashType(Enum):
    Bank = "Bank"
    Cash = "Cash"
    Promptpay = "Promptpay"
