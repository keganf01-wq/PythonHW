'''
Author: Kegan Firey
KUID: 3176824
Date: 08SEP25
Lab: lab02
Last modified: 08SEP25
Purpose: Gives solid Football Betting Advice
'''
spread=float(input("How many points is your team favored by?"))
home=input("If this is a home game enter 'H' (other input indicates away)")
bengals=input("If you are rooting for the Bengals enter 'Y' (other input indicated no)")

if bengals=='Y':
    print("My advice is: Don't bet, please God")
elif spread<=0:
    print("My advice is: Sit out on this one homie")
elif spread>=0 and spread<=3 and home!='H':
    print("My advice is: Wait for a home game")
elif spread>=0 and spread<=3 and home=='H':
    print("My advice is: Looks risky")
elif spread>=3 and spread<7.5 and home!='H':
    print("My advice is: Could be a good bet")
elif spread>=3 and spread<7.5 and home=='H':
    print("My advice is: I feel good about this one")
elif spread>=7.5:
    print("My advice is: Ooooo! Easy money!")

    
