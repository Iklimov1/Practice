#create dictionary
people = [{"name": "Harry", "house": "Gryffindor"},
          {"name": "Cho", "house": "RavenClaw"},
          {"name": "Draco", "house": "Slytherin"}
]
#sort people and print them
#def f(person):
    #return person["name"]

people.sort(key=lambda person: person["name"]) 
#this takes a person as the input and returns their name using lambda
#this uses the function f to sort by name because python doesn't know how to sort dictionaries
# if we were to switch "name" to "house" it would return the houses sorted
print(people)
