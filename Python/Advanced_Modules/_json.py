
person = {"name": "Güney", "languages":["python","C#"]}

result = person["name"] #Güney
result = person["languages"] #['python', 'C#']
result = person["languages"][0] #python


import json

person_string = '{"name": "Güney", "languages":["python","C#"]}' #şu an bu bir string dictionary tipli bir veri değil

#*****************JSON string to Dict 'loads'****************************
# result = json.loads(person_string) #Stringimizi 'dictionary' yapısına döndürdü Ekran çıktısı: {'name': 'Güney', 'languages': ['python', 'C#']}
# result = result["name"] #Güney
# result = result["languages"] #['python', 'C#']
# result = result["languages"][0] #python



#*****************person.json(dışarıdan dosya) 'load'*********************
# with open("C:\\Users\\90546\\Documents\\Python\\Advanced_Modules\\person.json") as f: 
    # data = json.load(f)
    # data = data["name"]
    # print(data)
    # print(data["name"])
    # print(data["languages"])



#******************Dict to JSON string 'dumps' and 'dump'******************
person_dict = {
    "name": "Güney",
    "languages": ["Python","C#"]
}

result = json.dumps(person_dict)
print(result) #{"name": "G\u00fcney", "languages": ["Python", "C#"]}
print(type(result)) #<class 'str'> stringe çevirdik bir json dosya yapabilmek için dictionary özelliği kayboldu

#----Hazırladığımız dictionaryden strye dönen dosyayı json dosyasına atmak için----
with open("C:\\Users\\90546\\Documents\\Python\\Advanced_Modules\\person.json","w") as f:
    json.dump(person_dict,f)



print("\n")
person_dict = json.loads(person_string)
print(person_dict) #{'name': 'Güney', 'languages': ['python', 'C#']}

result = json.dumps(person_dict,indent= 4, sort_keys= True) # Ekran çıktısı:
# {
#     "languages": [
#         "python",
#         "C#"
#     ],
#     "name": "G\u00fcney"
# }



print(result)





















