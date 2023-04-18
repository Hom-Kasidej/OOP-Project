from enum import Enum

class CarBrand(Enum):
    Aston_martin = 1
    Audi = 2
    BMW = 3
    BYD = 4
    Bentlay = 5
    Chevrolet = 6
    Citroen = 7
    FOMM = 8
    Fiat = 9
    Ford = 10
    GWM = 11
    Honda = 12
    Hyundai = 13
    Isuzu = 14
    Jaguar = 15
    Jeep = 16
    Kia = 17
    LDV = 18
    Lamborgini = 19
    Land_Rover = 20
    Lexus = 21
    MG = 22
    Maserati = 23
    Mazda = 24
    Mercedes_Benz = 25
    Mini = 26
    Mitsubishi = 27
    Nissan = 28
    Porsche = 29
    Rolls_Royce = 30
    Subaru = 31
    Suzuki = 32
    Tesla = 33
    Toyota = 34
    Volvo = 35
    Other = 36


class GearType(Enum):
    Manual = 1
    Auto = 2


class FuelType(Enum):
    Benzien = 1
    Benzien_91 = 2
    Benzien_95 = 3
    Benzien_E20 = 4
    Benzien_E85 = 5
    CNG = 6
    Diesel = 7
    Diesel_B10 = 8
    Diesel_B20 = 9
    Diesel_B5 = 10
    Diesel_B7 = 11
    Hybrid = 12
    LPG = 13
    NGV = 14
    EV = 15
    Plugin_Hybird = 16


class GPSType(Enum):
    CarTrack = 1
    Eyefleet = 2
    NoneGPS = 3
    Others = 4
    Otoplug = 5


class Gender(Enum):
    Male = 1
    Female = 2
    Others = 3


class Status(Enum):
    Canceled = 1
    Pending = 2
    Success = 3

    
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