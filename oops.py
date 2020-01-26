import datetime
import random


class ConstructorClass:
    """ constructors """

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


apple = ConstructorClass("red", "sweet")
print(apple.color)

# help(ConstructorClass)


class InheritedClass(ConstructorClass):
    print("haha")


newInstance = InheritedClass("yellow", "spicy")
print(newInstance.color)


class Repository:
    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


# random
print(random.randint(1, 10))
print(random.randint(1, 10))

# datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.day)
print(now + datetime.timedelta(days=28))


perdaySeconds = 86400
daysInWeek = 7


def calculateSecondsInWeek():
    totalseconds = daysInWeek * perdaySeconds
    return totalseconds


print(calculateSecondsInWeek())

# Use Python to calculate how many different passwords can be formed with 6 lower case English letters.
# For a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.
# Using this information, print the amount of possible passwords that can be formed with 6 letters.

totalAlphabets = 26


def numberofpossiblepasswords(passwordlength):
    return totalAlphabets * (totalAlphabets * passwordlength)


print(numberofpossiblepasswords(6))


disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)

print(((10 >= 5*2) and (10 <= 5*2)))


def sum(x, y):
    return(x+y)


print(sum(sum(1, 2), sum(3, 4)))


def digits(n):
	count = 0
	if n == 0:
	  count = 1
	while (n > 10):
		count += 1
		n / 10
	return count


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))    # Should print 1
