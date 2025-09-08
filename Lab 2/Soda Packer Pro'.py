'''
Author: Kegan Firey
KUID: 3176824
Date: 08SEP25
Lab: lab02
Last modified: 08SEP25
Purpose: Tells user ideal packing for a given quantity of sodas
'''
soda=int(input("how many sodas do you have?"))
fridgeCube=(soda//24)
sixPack=((soda%24)//6)
singles=((soda%24)%6)
print("Fridge Cubes:",fridgeCube)
print("Six-Packs:",sixPack)
print("Singles:",singles)
         
