import math
print ("X² + x + 1 = 0")
a = input("insira a:" )
b = input("insira b:" )
c = input("insira c:" )

delta = int (b) ** 2 - 4 * int (a) * int (c)
if delta > 0:
 x_one = (- int (b) + math.sqrt(delta)) / 2 * 1
 x_two = (- int (b) - math.sqrt(delta)) / 2 * 1
 print (f"Delta = {delta}, S ={x_one},{(x_two)}")
elif delta == 0:
 x_one = (- int (b) + math.sqrt(delta)) / 2 * 1
 x_two = (- int (b) - math.sqrt(delta)) / 2 * 1
 print (f"Delta = {delta}, S ={x_one},{(x_two)}")
elif delta < 0:
  print (f"Delta = {delta}, S = null")
