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


