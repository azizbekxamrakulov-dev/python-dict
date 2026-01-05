data = { "ism": "Ali","yosh": 16,"shahar": "Toshkent"}

kalit = input("Kalit nomini kiriting: ")

if kalit in data:
    print(data[kalit])
else:
    print("Topilmadi")