def greet_user():
    print("Hello")

greet_user()

def greet_user(username):
    print("Hello "+username)
greet_user('ali')


###### TRY YOURSELF##########
#8-1

def display_msg():
    print("hi you are logged in")
display_msg()

#8-2
def fav_book(title):
    print("My favourite book is "+title)

fav_book('alice in wonderland')

def descrbe_pet(types, name):
    print("Animal type is " +types +" its name is "+name)

descrbe_pet('hamster','harry')
descrbe_pet('dog','willie')
descrbe_pet(types='cat', name='tom')
descrbe_pet(name='tom', types='cat')

def descrbe_pet(types, name='willie'):
    print("Animal type is " +types +" its name is "+name)

descrbe_pet(types='dog')

##### TRY YOURSELF#########
#8-3
def make_shirt(size,msg):
    print("your shirt size is "+size+" the message is "+msg)
make_shirt('16','medium')
make_shirt(msg='normal',size='12')

#8-4
def make_shirt(msg,size='large'):
    print("your shirt size is "+size+" the message is "+msg)
make_shirt('i love python')

#8-5
def describe_city(name, country='Pakisan'):
    print(name+" is in "+country)

describe_city('karachi')
describe_city('lahore')
describe_city('Malaga')

#
def gret_user(names):
    for name in names:
        print("hello "+name)

username=['linda','herry','sarah']
gret_user(username)