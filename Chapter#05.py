# simple if statement
cars=['audi','bmw','suzuki','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

car='Audi'
car.lower() =='audi'

# checking for inequality
requested_topping='paproni'
if requested_topping != 'mashrooms':
    print("hold the mashrooms!")

# Numerical Comparisions
answer=17
if answer!=42:
    print("that is not the correct number")

#checking user is not in the list
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title() + ", you can response")

# TRY IT YOURSELF
#5-1
car='subaru'
print("Is car == 'subaru' I predict true")
print(car=='subaru')

#5-2
for car in cars:
    if car=='Audi':
        print(car.lower()=='audi')
    if car!='audi':
        print(car=='suzuki')

numbers=[1,2,3,5,6,7]
for num in numbers:
    if (num==4 or num==6):
        print(str(num) + "is not in the list")
    if(num!=4):
        print(str(num) + "is in the list")

#Simple IF statement
age=12
if age >= 18:
    print("you can vote")
print("you can not vote")

# if else statement
age=17
if age>=18:
    print("you are eligible for the test")
else:
    print("sorry you are not elligiable")

#if-elif-else

age=12
if age<4:
    price=0
elif age < 18:
    price=5
else:
    price=10
print("you admission cost is "+str(price))

#MULTIPLE ELIF STATEMENTS

age=12
if age<4:
    price=0
elif age < 18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5

print("you admission cost is "+str(price))

#multiple if without else of elif
requested_topping=['mushrooms','extra cheese']
if 'mushrooms'in requested_topping:
    print("adding mushrooms")
if'papproni'in requested_topping:
    print("Add peproni")
if 'extra cheese' in requested_topping:
    print("add extra cheese")

##################### TRY YOURSELF #######################
# AlienColors
#5-4
alien_color=['green','yellow','red']
if 'green' in alien_color:
    print("the player earned 5 points")
else:
    print("th eplayer just earned 10 points")

#5-5
alien_color=['green','yellow','red']
if 'green' in alien_color:
    print("the player earned 5 points")
elif 'yellow' in alien_color:
    print("the player just earned 10 points")
else:
    print("The player earned 15 points")

#5-6
age=14
if age<2:
    print("the person is a baby")
elif age==2  or age<4:
    print("the person is toddler")
elif age==4 or age<13:
    print("the person is kid")
elif age==20 or age<65:
    print("the person is an adult")
elif age>=65:
    print("the person is elder")

#5-7
fav_fruits=['apple','mango','banana','pinapple','melon']
if 'apple' in fav_fruits:
    print("I really like apple")
if 'mango' in fav_fruits:
    print("I really like mango")
if 'banana' in fav_fruits:
    print("I really like banana")
if 'pinapple' in fav_fruits:
    print("I really like pinapple")
if 'melon' in fav_fruits:
    print("I really like melon")

# Checking for special items
requested_toppings=['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("sorry  we are out of green peppers right now")
    else:
        print("Adding " + requested_topping)
print("finished  making piza")

requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping)
        print("Finish making your pizza")
else:
    print("Are you sure you want a plan pizza")

available_toppings=['mushrooms','olives','green peppers','pepproni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+ requested_topping)
else:
    print("sorry  we dont have " + requested_topping)
print("Finished making pizza")

# TRY YOURSELF
#5-8
username=['ali','sara','admin','zara','saira']
for user in username:
    if user=='admin':
        print("hi "+ user+ " welocme here")
else:
    print("hi "+ user + "welcome")