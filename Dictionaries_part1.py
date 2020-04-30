## dictinaries
## dictionares are unordered collections of data in key :value pair.
### use curley brasis


user = { "name" : "Anoop", "last_name" : "Singh", "age" : 37, }
print(user)


user1 = dict(name = "Anoop", age = 37, last_name= "Singh")

print(user1)

## how to access data in dictionary
### can be accessed by key name

print(user["name"])
print(user["age"])


user_info = {
    "name": "Anoop",
    "last_name": "Singh",
    "age": 37,
    "fav_movies": ["coco", "kimi no na wa"],
    "fav_tunes": ["awakening", "fairy tale"]
}

print(user_info)
print(user_info["fav_movies"][0])

### in keyword and iterations in dictionaries

#checking if key exist in dictionary
user_info = {
    "name": "Anoop",
    "last_name": "Singh",
    "age": 37,
    "fav_movies": ["coco", "kimi no na wa"],
    "fav_tunes": ["awakening", "fairy tale"]
}

if "names" in user_info:
    print("present")
else:
    print("not present")

# checking value if it's there

if "Anoop" in user_info.values():
    print("present")
else:
    print("not present")
if ["awakening", "fairy tale"] in user_info.values():# values mehtod
    print("present")


## loops in dictionaries

for i in user_info:
    print(i)

for i in user_info.values():
    print(i)


# values method

user_info1 = user_info.values()

print(user_info1)
print(type(user_info1))

#keys method


user_info2 = user_info.keys()

print(user_info2)
print(type(user_info2))


## loops

for i in user_info:
    print(i)


for i in user_info:
    print(user_info[i])

### items method*** VERY INPORTANT

user_item = user_info.items()
print(user_item)
print(type(user_item))

for key, value in user_info.items():

    print(f"key is {key} and value is {value}")