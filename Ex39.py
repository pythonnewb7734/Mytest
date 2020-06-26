#create a mapping of state to abbreviation
states = {
    'New South Wales': 'NSW',
    'Queensland': 'QLD',
    'Victoria': 'VIC',
    'Tasmania': 'TAS',
    'Australian Capital Teritory': 'ACT'
}

#create a basic set of states and some cities in them
cities = {
    'NSW': 'Sydney',
    'QLD': 'Brisbane',
    'VIC': 'Melbourne'
}

#add some more cities
cities['TAS'] = 'Hobart'
cities['ACT'] = 'Canberra'

#print out some cities
print('-' * 10)
print("TAS State has: ", cities['TAS'])
print("ACT Stat has: ", cities['ACT'])

#print some states
print('-' * 10)
print("New South Wales's abbreviation is: ", states['New South Wales'])
print("Queensland's abbreviation is: ", states['Queensland'])

#do it by using the state then cities dict
print('-' * 10)
print("Victoria has: ", cities[states["Victoria"]])
print("Tasmania has: ", cities[states["Victoria"]])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} is city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get an abbreviation by stat that  might not be there
sate = states.get('Western Australia')

if not state:
    print("Sorry, no Western Australia")

#get a city with a default value
city = cities.get('WA', 'Does not exist')
print(f"The city for the state 'WA' is: {city}")
