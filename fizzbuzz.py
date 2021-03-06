"""
fizzbuzz.py
Author: Bauti G
Credit: none

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""
total=int(input("How many numbers shall we print? "))
fizzn=int(input("For multiples of what number shall we print 'Fizz'? "))
buzzn=int(input("For multiples of what number shall we print 'Buzz'? "))
listtotal=list(range(1,total+1))
number=0

while total>number:
    if listtotal[number]%fizzn==0 and listtotal[number]%buzzn==0: #are fizz and buzz factores of the number
       listtotal[number]="FizzBuzz"
       number=number+1
    elif listtotal[number]%buzzn == 0: #is buzz a factor of the number? if so, replace with buzz
        listtotal[number]="Buzz"
        number=number+1
    elif listtotal[number]%fizzn == 0: #is fizz a factor of the number? if so, replace with fizz
        listtotal[number]="Fizz"
        number=number+1
    else:
        number=number+1 #if neither fizz or buzz are factors, go to the next number

for x in listtotal:
    print (x)
"""
while total>number2:
    if listtotal[number2]%buzzn==0:
        listtotal[number2]="Buzz"
        number2=number2+1
    else:
        number2=number2+1

for x in listtotal:
    while number<total:
        number2=0
        fizznumber=listtotal[number2]%fizz
        number=number+1
        number2=number2+1
        print(x+1)

        if fizznumber=0:
            listtotal[number]=fizz
            else listtotal[number]=listtotal[number]
    print(x+1)
"""