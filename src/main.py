import sys
from calc import apply_vat

price = sys.argv[1]
percent = sys.argv[2]

#print(f'Price : {price}/ percent : {percent}')

try :
    price = float(price)
    percent = float(percent)
except ValueError:
    print ("Erreur !")

new_price = apply_vat(price, percent)
print(new_price)