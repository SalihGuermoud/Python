nbMembres = int(input())

poidsTotalEq1 = 0
poidsTotalEq2 = 0

for i in range(nbMembres):
    poidsEq1 = int(input())
    poidsEq2 = int(input())
    poidsTotalEq1 = poidsTotalEq1 + poidsEq1
    poidsTotalEq2 = poidsTotalEq2 + poidsEq2

if poidsTotalEq1 > poidsTotalEq2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 : " + str(poidsTotalEq1))
print("Poids total pour l'équipe 2 : " + str(poidsTotalEq2))
