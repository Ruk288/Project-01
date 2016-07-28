alien_0={'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points=alien_0['points']
print("you just got "+ str(new_points)+" points")

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

# starting with an empty list
alien_1={}
alien_1['color']='green'
alien_1['points']=5
print(alien_1)

# modifying value in dictionary
alien_1['color']='yellow'
print(alien_1)

#tracking positionof an alien

alien_2={'xposition':0, 'yposition':25, 'speed':'medium'}

if alien_2['speed']=='slow':
    xincrement=1
elif alien_2['speed']=='medium':
    xincrement=2
else:
    xincrement=3

alien_2['xposition']=alien_2['xposition']+xincrement
print("New xposition is "+ str(alien_2['xposition']))

del alien_0['points']
print(alien_0)

fav_lang={
    'jen':'python',
'sara':'c',
'edward':'python',
}
print("jen's favourite language is "+fav_lang['jen'].title())

########### TRY YOURSELF ##################
# 6-1
person={'first_name': 'ali','last_name':'khan','age':20,'city':'Karachi'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2
fav_number={'ali':2,'sara':23,'khan':45,'gina':45,'saira':3}
for key, value in fav_lang.items():
    print("key "+ key)
    print("value "+ value)

friends=['phil','jen']
for name in fav_lang.keys():
    print(name.title())
    if name in friends:
        print("Hi "+ name.title()+" your favourite languga is "+ fav_lang[name])
    if 'ali' not in fav_lang.keys():
        print("sorry")


#looping through a dictionary keys in order
for name in sorted(fav_lang.keys()):
    print(name.title())


for language in set(fav_lang.values()):
    print(language)

############### TRY YOURSELF ####################

#6-4
fav_lang={
    'jen':'python',
'sara':'c',
'edward':'python',
}
for key, values in fav_lang.items():
    print("teh favourite language is "+values.title())

#list of dictionaries

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# empty list for storing aliens
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green', 'points':5}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=35
    print(alien)
#######33 list in a dictionary
pizza={'crust':'thick','topings':['mushroom','pepproni','extra cheese']}
print("you ordered a "+pizza['crust']+" pizza crust with the topping of ")
for toping in pizza['topings']:
    print(toping)