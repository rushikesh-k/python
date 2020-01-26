# declare variables

print("Hello World")
name = "Rushikesh"
print("My Name is " + name)
birthdate = 12
print(birthdate)


def greeting(name):  # create function 1 paramm
    print("Greeting, " + name)


greeting("Rushi")


def greeting2(name, age):  # create function 2 paramms
    print("Greeting," + name)
    print("Age : " + age)


greeting2("Rushi", "29")


def area_triangle(base,  height):  # return type function
    return base*height/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b

print("Area A : " + str(area_a))
print("Area B : " + str(area_b))
print("Sum of both areas : " + str(sum))


def convert_seconds(seconds):  # return multiple values
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, remaining_seconds = convert_seconds(1000)
print("Hours : " + str(hours) + " Minutes : " + str(minutes) +
      " Remaining Seconds : " + str(remaining_seconds))

print(10 < 1)  # conditional statements

print("cat" == "dog")

print(1 != 2)

print("cat" == "Cat")

print(25 < 80 and 1 > 20)

print(25 < 80 or 1 > 20)

print(not 42 == "ABC")


def checkLength(name):  # if else statements
    if len(name) > 4:
        print("length is " + str(name))
    elif len(name) < 4:
        print("username should be greater than 4")


# for loop
for x in range(5):
    print(x)

friends = ['Rushikesh', 'Prasad', 'Siddhesh']
for friend in friends:
    print("Hi " + friend)
    print(f'Hi,{friend}')


values = [23, 12, 8, 9, 5]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Sum : " + str(sum) + "\nAverage : " + str(sum/length))

# range for loop
product = 1
for n in range(1, 10):
    product = product * n

print(product)


def to_celsius(x):  # temperature farren to celsius
    return (x-32)*5/9


for x in range(0, 101, 10):
    print(x, to_celsius(x))

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# nested for loops
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end="")
    print()

teams = ['Dragons', 'Wolves', 'Owls', 'Lions']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + ' vs ' + away_team)


def factorial(n):  # recursion functions
    print("Factorial called with " + str(n))
    if n < 2:
        print('Returning 1')
        return 1
    result = n * factorial(n-1)
    print('Returning ' + str(result) + ' for factorial of ' + str(n))
    return result


factorial(4)


text = "Rushikesh"  # strings
print(text[-1])
print(text[1:4])
print(text[:4])
print(text[4:])
print(text.index('s'))
print("o" in text)
print(text.lower())
print(text.upper())
print(text.capitalize())
text = " Rushikesh "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
text = "Rushikesh"
print(text.count('s'))
print(text.endswith('h'))
print(text.endswith('o'))
print(text.isnumeric())
text = "My Name is Rushikesh"
print(text.split())

baseprice = 7.5
tax = 1.09
print("Base price is ${:.2f} and tax is ${:.2f}".format(baseprice, tax))

xList = text.split()  # lists
print(xList)
print(len(xList))
print("name" in xList)
print("Name" in xList)
print(xList[3])
print(xList[-1])
print(xList[1:3])
print(xList[:3])
print(xList[1:])
xList.append('Korgaonkar')
print(xList)
xList.insert(4, 'Jagdish')
print(xList)
xList.pop(4)
print(xList)

myName = ('Rushikesh', 'Jagdish', 'Korgaonkar')  # tuples
print(myName)
name, middleName, lastName = myName
print(name, middleName, lastName)

for person in enumerate(myName):
    print(person)


def generateEmail(people):
    result = []
    for email, name in people:
        result.append("{}<{}>".format(name, email))
        return result


print(generateEmail([('rushikesh.k@gmail.com', 'Rushikesh K')]))


multiples = [x * 7 for x in range(1, 11)]
print(multiples)


file_counts = {"jpg": 10, "txt": 25, "png": 20, "pdf": 26}  # dictionary
for extension in file_counts:
    print(extension)

print(file_counts.keys())
print(file_counts.values())


class FirstClass:  # classes and methods
    name = "Rushi"

    def speak(self):
        print("I am {} ".format(self.name))


firstInstance = FirstClass()
firstInstance.speak()

secondInstance = FirstClass()
secondInstance.name = "PK"
secondInstance.speak()

secondInstance = FirstClass()
secondInstance.name = "Sid"
secondInstance.speak()
