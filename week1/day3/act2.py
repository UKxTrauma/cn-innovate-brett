lang = [
    "English",
    "French",
    "German",
    "Spannish",
    "Italian",
    "English",
    "Lithuanian"
]

capitals = {
    "UK":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome"
}

print(capitals.items())

capitals.setdefault("Australia", "Canberra")
capitals.setdefault("Lithuania", "Vilnius")

print(capitals.items())

i=0
for x in capitals:
    capitals[x] = lang[i]
    i+=1

[print('The most popular spoken language in', key, 'is', value+'.') for key, value in capitals.items()]