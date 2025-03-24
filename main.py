import random
import os



shots = 10
random_number = random.randint(1000, 9999)


res = 1


d1 = random_number // 1000
d11 = d1 * 1000


updatedNumber = random_number - d11

d2 = updatedNumber // 100
d22 = d2 * 100

updatedNumber -= d22


d3 = updatedNumber // 10
d33 = d3 * 10

lastNumber = updatedNumber - d33





print(random_number)
print(updatedNumber, 'ywfhaipusfhaskf')
print(d1, d2, d3, lastNumber)
print(lastNumber)





