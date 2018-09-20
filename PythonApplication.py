# basics learned from the course
def callByName(name):
    firstList = ['hello','world']
    firstDictionary = {'proprety': 'value'}
    # tuples are like arrays.. but cannot change!

    del firstList
    firstDictionary.clear()

    return 'Hello ' + name
# print(callByName('Mohamed')+"\n")


# a small project
# creating a prime number generator
def primeNumberGenerator(limit):
    for i in range(2,limit):
        j = 2
        counter = 0
        while j < i:
            if i % j == 0:
                counter = 1
                j = j + 1
            else:
                j = j + 1
        if counter == 0:
            print(str(i) + " is a number.")
        else:
            counter = 0
# print(primeNumberGenerator(100))


# loop control statements: continue, pass, break
def loopControl():
    counter = 0
    while counter < 100:
        if counter == 4:
            break # breaks out of the code block
        else:
            pass # just a filler code
        print(counter)
        counter = counter + 1
    
    # let's see the continue
    for i in 'Python':
        if i == 'h':
            continue # to bypass any code underneath it
        print(i) # it'll print: p y t o n
# print(loopControl())


# talking about try and except (useful for web development)
def tryAndExceptStatements():
    try:
        if name > 3:
            print('Hi') # error: cause name is undefined
    except:
        print('Python ran into an error. Please take a look at your code again')
# print(tryAndExceptStatements())


# dir() and help() built-in functions
# dir() returns the available commands on a certain data type
# help() returns something like a documentation
def dirAndHelp():
    tiger = 'I am a tiger'
    # return dir(tiger)
    return help(tiger.upper)
# print(dirAndHelp())


# classes and inheritance
class Students(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Students('Moh',23)
student2 = Students('Malek',22)

hasattr(student1,'age') #true
hasattr(student1, 'grade') #false
setattr(student1, 'grade', 'post-graduate') #sets the grade attribute
hasattr(student1, 'grade') #true
delattr(student1, 'grade') #deletes the grade attribute


class Parent(object):
    counter = 10
    def __init__(self):
        print('Class initialized')
    def parentFunc(self):
        print('ParentFunc is being called')
    def setCounter(self, num):
        Parent.counter = num
    def showCounter(self):
        print(str(Parent.counter))
class Child(Parent):
    def __init__(self):
        print('Child class being initiliazed')
    def childFunc(self):
        print('ChildFunc being called')
c = Child()
c.childFunc() #ChildFunc being called
c.parentFunc() #ParentFunc being called
c.setCounter(20)
c.showCounter() # prints: 20
Child.showCounter() # prints: 10