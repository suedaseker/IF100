# -*- coding: utf-8 -*-
"""suedaseker_the3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tUXkBouQgwE5CforyhtH-QLQH7jjfmld
"""

while True:
  products = input("Products in shopping cart: ")

  count1 = 0
  for x in products:
    if x.find("_") != -1:
      count1 += 1
  count2 = 0
  for y in products:
    if y.find(",") != -1:
      count2 += 1
  if count1 == (count2 + 1 ) * 4:
    break
  else:
    print("Invalid input for products, please enter in correct format.")

while True:
  members = input("Family members' informations: ")

  count3 = 0
  for x in members:
    if x.find("_") != -1:
      count3 += 1
  count4 = 0
  for y in members:
    if y.find(",") != -1:
      count4 += 1

  if count3 == (count4 + 1 ) * 3:
    break
  else:
    print("Invalid input for family information, please enter in correct format.")

numM = members.count("M")
numF = members.count("F")

products = products.split(",")

totalfat = 0
for product in products:
  product = product.split("_")
  quantity = int(product[1])
  fat = int(product[2])
  totalfat += quantity * fat
fatcal = totalfat * 9

totalcarboh = 0
for product in products:
  product = product.split("_")
  quantity = int(product[1])
  carboh = int(product[3])
  totalcarboh += quantity * carboh
carbohcal = totalcarboh * 4

totalprotein = 0
for product in products:
  product = product.split("_")
  quantity = int(product[1])
  protein = int(product[4])
  totalprotein += quantity * protein
proteincal = totalprotein * 4

members = members.split(",")
for mem in members:
  mem = mem.split("_")
  if mem[0] == "M":
    w = int(mem[1])
    h = int(mem[2])
    age = int(mem[3])
    Mneed = 66.5 + (13.8 * w) + (5 * h) - (6.8 * age)
  if mem[0] == "F":
    w = int(mem[1])
    h = int(mem[2])
    age = int(mem[3])
    Fneed = 655.1 + (9.6 * w) + (1.9 * h) - (4.7 * age)

Mfneed = Mneed * 30 /100
Mcneed = Mneed * 50 / 100
Mpneed = Mneed * 20 /100
Ffneed = Fneed * 30 /100
Fcneed = Fneed * 50 /100
Fpneed = Fneed * 20 / 100

f = int(fatcal / ((numF * Ffneed) + (numM * Mfneed)))
c = int(carbohcal / ((numF * Fcneed) + (numM * Mcneed)))
p = int(proteincal / ((numF * Fpneed) + (numM * Mpneed)))

if f < 1:
  print("You need to add products with more fat to your shopping cart.")
else:
  print("These products will be enough for your family in terms of fat for", f, "days.")

if c < 1:
  print("You need to add products with more carb to your shopping cart.")
else:
  print("These products will be enough for your family in terms of carbohydrate for", c, "days.")

if p < 1:
  print("You need to add products with more protein to your shopping cart.")
else:
  print("These products will be enough for your family in terms of protein for", p, "days.")