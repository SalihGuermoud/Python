quantite = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]

numIngredient = len(quantite)
while numIngredient >= len(quantite) or numIngredient < 0:
    numIngredient = int(input())
print(quantite[numIngredient])
    



