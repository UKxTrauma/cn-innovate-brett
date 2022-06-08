pokemon_info = {
    "Bulbasaur": {
        "Element(s)":"Grass",
        "Base stage":"Bulbasaur",
        "Evo one":"Ivysaur",
        "Evo two":"Venasaur"
        },
    "Charmander": {
        "Element(s)":"Fire",
        "Base stage":"Charmander",
        "Evo one":"Charmeleon",
        "Evo two":"Charizard"
        },
    "Squirtle": {
        "Element(s)":"Water",
        "Base stage":"Squirtle",
        "Evo one":"Wartortle",
        "Evo two":"Blastoise"
        }
}

for x in pokemon_info.items():
    print(x)
for y in pokemon_info.keys():
    print(y)
for z in pokemon_info.values():
    print(z)

for u in pokemon_info["Bulbasaur"].items():
    print(u)
for v in pokemon_info["Bulbasaur"].keys():
    print(v)
for w in pokemon_info["Bulbasaur"].values():
    print(w)

for r in pokemon_info["Charmander"].items():
    print(r)
for s in pokemon_info["Charmander"].keys():
    print(s)
for t in pokemon_info["Charmander"].values():
    print(t)

for o in pokemon_info["Squirtle"].items():
    print(o)
for p in pokemon_info["Squirtle"].keys():
    print(p)
for q in pokemon_info["Squirtle"].values():
    print(q)

print(f'''Bulbasaur has the {pokemon_info['Bulbasaur']['Element(s)']} element, it's final evolutionary stage is {pokemon_info['Bulbasaur']['Evo two']}.''')
print(f'''If you would like to have a {pokemon_info["Squirtle"]['Element(s)']} type Pokemon, you should go for either a {pokemon_info["Squirtle"]['Base stage']}, {pokemon_info["Squirtle"]['Evo one']} or {pokemon_info["Squirtle"]['Evo two']}.''')
print(f'''If you envy trainers whom weild a {pokemon_info["Charmander"]['Evo two']}, the big boi of Gen 1, you need to obtain and evolve your {pokemon_info["Charmander"]['Evo one']}.''')

pokemon_info["Bulbasaur"].setdefault("New key", "New value")
for u in pokemon_info["Bulbasaur"].items():
    print(u)
for v in pokemon_info["Bulbasaur"].keys():
    print(v)
for w in pokemon_info["Bulbasaur"].values():
    print(w)