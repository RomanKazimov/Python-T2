database = {}
def parametrs():  
    query_dict = {}  
    print("Heyvanin xusisiyetlerin qeyd edin")
    try:
        name_value = input("Heyvanin adini qeyd edin: ")
        breed_value = input("Heyvanin cinsini qeyd edin: ")
        gender_value = input("Heyvanin genderini qeyd edin: ")
        color_value = input("Heyvanin rengini qeyd edin: ")

        query_dict = {
            "name": name_value, 
            "breed": breed_value, 
            "gender": gender_value, 
            "color": color_value
        }
    except Exception as e:
        raise ValueError(f"Xeta oldu: {e}")

    return query_dict

while True:
    try:
        sinif = input("Heyvanin sinifi qeyd edin: ")
    except Exception as e:
        raise ValueError(f"Xeta oldu: {e}")
    
    live_creature = parametrs()
    database[sinif] = live_creature

    print("Databasede olan:")
    for sinif, i in database.items():
        print(f"Sinif: {sinif}")

        for key, value in i.items():
            print(f"  {key.capitalize()}: {value}")
        print()  
    
    davam = input("teze heyvan yaratmaq (he/yox): ")
    if davam.lower() != "he":
        break
print("Databasede olan melumatlar:")
for sinif, i in database.items():
    print(f"Sinif: {sinif}")
    for key, value in i.items():
        print(f"  {key.capitalize()}: {value}")
    print()  
