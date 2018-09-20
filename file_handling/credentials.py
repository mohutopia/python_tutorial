f = open('./file_handling/credentials.txt', 'w')
f.write('Hello, here will be your credentials\n')
f.close()

def credentials():
 name = input('Enter your name: ')
 age = input('Enter your age: ')
 speci = input('Enter your speciality: ')
 return "Name: " + name + ", Age: " + age + "\nSpeciality: " + speci

f = open('./file_handling/credentials.txt', 'a')
f.write(credentials())
f.close()