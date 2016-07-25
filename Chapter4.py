magicians=['alic', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + " , that was a trick")
    print("I can't wait to see your next trick" + magician.title())
print("thank you all")

########### Try it yourself ##############
# 4-1
pizzas=['chicken tikka','mashroom', 'cheese', 'bihar']
for pizza in pizzas:
    print("I like " + pizza +' pizza')

print("My all time favorite pizza is " + pizzas[0])

# 4-2
animals=['cat','dog', 'cow', 'goat']
for animal in animals:
    print("A "+ animal+" would make a great pet")

# Numbers in list

for values in range(1,6):
    print(values)
numbers=list(range(1,6,2))
print(numbers)

# square of numbers in list

square=[]
for value in range(1,11):
     square.append(value**2)
print(square)

# Simple Statistics

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


# list comprehensions

squares=[values**2 for values in range(1,10)]
print(squares)

##################### TRY IT Y0URSELF ####################
# 4-3
for value in range(1,21):
    print(value)

# 4-4
#for value in range(1,100000):
 #   print(value)

# 4-5
value=[]
for values in range(1,100000):
    value.append(values)
mini_value=min(value)
print(mini_value)
maxi_value=max(value)
print(maxi_value)
summ_value=sum(value)
print(summ_value)

# 4-6 odd numbers
for value in range(1,21,2):
    print(value)

#4-7
three=[]
for values in range(3,31):
    three.append(values*3)
print(three)


#4-9
cubes=[values**3 for values in range(1,11)]
print(cubes)

# Slicing with parts of list
players=['eli','charles', 'Michael', 'florence']
print(players[0:3])
print(players[1:2])
print(players[:3])
print(players[2:])
print(players[-3:])

# looping with the slice
for player in players[0:2]:
    print(player.title())

# copying a list
players_1=players[:]
print(players_1)
players_1.append('ela')
players.append('tim')
print(players_1)
print(players)

##################### TRY IT YOURSELF ######################
# 4-10
items=['pen','pencil','paper','marker','file','duster']
for item in items[0:3]:
    print("The item included in the list is " + item)
for item in items[2:4]:
    print("The item included in middle of the list is " + item)
for item in items[-3:]:
    print("The item included in last of the list is " + item)

# 4-11
freinds_pizza=pizzas[:]
print(freinds_pizza)
pizzas.append('paprooni')
freinds_pizza.append('tomatoo')
for pizza in pizzas:
    print("the first list for pizzas is " + pizza)
for pizza in freinds_pizza:
    print("the second list for pizzas is " + pizza)

# tuples
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

# using for loop on tuples
for dimension in dimensions:
    print(dimension)

# changing value of a tuple
dimensions=(400,5)
for dimension in dimensions:
    print(dimension)

########### Try it yourself ##############
#4-13
foods=('rice', 'biryani', 'pizza', 'sauce', 'salad', 'soup')
for food in foods:
    print(food)
diff_food=('rice','biryani','daal','sabzi', 'salad', 'soup')
for food in diff_food:
    print(food)