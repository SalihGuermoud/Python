def estPair(n):
    if n % 2 == 0:
        return True
    else:
        return False

tab = [3, 5, 8]

"""for index in range(len(tab)):
    print(tab[index])"""
    
"""sum = 0
for index in range(len(tab)):
    sum = sum + tab[index]
print(sum)"""

for index in range(len(tab)):
    if estPair(tab[index]):
        tab[index] = tab[index] * 2
print(tab)


    




