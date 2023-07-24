"https://www.france-ioi.org/algo/task.php?idChapter=647&idTask=1939

nbLieux = int(input())
resultat = 0

for loop in range(nbLieux):
    nbGens = int(input())
    if (nbGens > 10000):
        resultat = resultat + 1
print(resultat)    