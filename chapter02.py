# Think Python 2
# Chapter 01, page 15

import math

print("*** CHAPTER 02 EXERCISES ***")

r = 5
pi = math.pi
vol_sphere = (4/3)*pi*r**3
print("2.2.1 The volume of a sphere with radius 5 is", round(vol_sphere,2))

price = 24.95
discount = 40 #percent
shipping = (3, 0.75)
copies = 60
shipping_fee = shipping[0] + (shipping[1]*(copies-1))
wholesale = price*copies*((100-discount)/100)
total = wholesale + shipping_fee

print("2.2.2 if the price of a book is $24.95")
print("..... and there is a discount of 40%")
print("..... shipping is $3 plus 0.75 for each extra copy")
print("..... The wholesale cost of 60 books is", round(total,2))