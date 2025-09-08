'''
Author: Kegan Firey
KUID: 3176824
Date: 08SEP25
Lab: lab02
Last modified: 08SEP25
Purpose: Solves and Prints Long Division Problems
'''
numerator=int(input("Enter a numerator"))
denominator=int(input("Enter a denominator"))
if denominator==0:
    print("nice try bud")
    print("exiting...")
else:
    print(numerator, '/', denominator, '=', numerator//denominator, 'remainder', numerator%denominator)
    print("goodnight sweet prince")
