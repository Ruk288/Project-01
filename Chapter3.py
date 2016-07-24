# Accessing the list

bicycles=['trek', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-2].title())
# using individual values from the list

message="My favourite bicycle is " + bicycles[0].title() + "."
print(message)

# Try it yourself
# 3-1

friend_names=["sara", "sana", "asim", "asif"]
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])
print(friend_names[3])

# 3-2
print(friend_names[0].title() + " is my best friend")
print(friend_names[1].title() + " is my best friend")
print(friend_names[2].title() + " is my best friend")
print(friend_names[3].title() + " is my best friend")

# 3-3
transport=["motor", "car", "bicycle", "rickshaw"]
print("I like " + transport[0])
print("I do not like " + transport[1])
print("I like to have " + transport[2])
print("I like to gift " + transport[3] + " to sara")

# modifying elements of a list

transport[0]= 'bike'
print(transport)

# appending element at the enf of the list

transport.append('bus')
transport.append('tricycle')
transport.append('chinchi')
print(transport)

# inserting element to a list

transport.insert(1, 'hover')
print(transport)

# deleting an element form a list

del transport[0]
print(transport)

# popping item from the list

popped_transport=transport.pop()
print(transport)
print(popped_transport)

popped_transport=transport.pop(2)
print(transport)
print(popped_transport)

# removing an item by value

transport.remove('rickshaw')
print(transport)

a= 'car'
transport.remove(a)
print("I have removed "  +a)


############ Try it yourself ###############

# 3-4
guest=["sara", "ayesha", "aamna"]
print(guest[0].title() + " is invited to dinner")
print(guest[1].title() + " is invited to dinner")
print(guest[2].title() + " is invited to dinner")

print(guest[1].title() + " will not attend the dinner")

del guest[1]
print(guest)

guest.insert(1, 'sana')
print(guest)

print(guest[0].title() + " is invited to dinner")
print(guest[1].title() + " is invited to dinner")
print(guest[2].title() + " is invited to dinner")

# 3-6 more guests

guest.insert(0,'ali')
guest.insert(1,'adeel')
guest.append('elen')
print(guest)

# 3-7
print("you can invite only two people")
popped1=guest.pop()
print("sorry " + popped1 + " you are not invited on dinner")
popped2=guest.pop()
print("sorry " + popped2 + " you are not invited on dinner")
popped3=guest.pop()
print("sorry " + popped3 + " you are not invited on dinner")
popped3=guest.pop()
print("sorry " + popped3 + " you are not invited on dinner")
print(guest)
print("hey " + guest[0] + " you are invited on dinner")
print("hey " + guest[1] + " you are invited on dinner")
del guest[0]
del guest[0]
print(guest)

# sorting a list

cars=['bmw', 'audi', 'toyota', 'sabaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# temporarily sorted

print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))

# reverse order
cars.reverse()
print(cars)

# finding length of list

print(len(cars))

# ######################## try it yourself #####################
# 3-8
places=['Spain', 'Austria', 'Japan', 'Malaysia', 'Swizerland']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3-9
print("i invited only " + str(len(guest)) + " for the dinner")