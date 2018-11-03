# -*- encoding: utf-8 -*- #

number = int ( raw_input ( "Pick a number between 1 and 100: ") )
print number


for x in range ( 1, number ):
    if x % 3 == 0 and x % 5 == 0:
        print "fizzbuzz"
    elif x % 3 == 0:
        print "fizz"
    elif x % 5 == 0:
        print "buzz"
    else:
        print x

print "THANKS FOR YOUR TIME".lower()