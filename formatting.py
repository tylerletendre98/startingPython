for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    # adding a colon makes the field width

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    # using the < will left align and the > will right align and ^ will center align

print()

print("Pi is approxiamately {0:12}".format(22 / 7))
print("Pi is approxiamately {0:12f}".format(22 / 7))
print("Pi is approxiamately {0:12.50f}".format(22 / 7))
print("Pi is approxiamately {0:52.50f}".format(22 / 7))
print("Pi is approxiamately {0:62.50f}".format(22 / 7))
print("Pi is approxiamately {0:<72.54f}".format(22 / 7))
