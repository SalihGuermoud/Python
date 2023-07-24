"https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=577"

def afficherLigne(taille, caractere):
    for loop in range(taille):
        print(caractere, end = "")
    print()
    
taille = int(input())
afficherLigne(taille, "X")
afficherLigne(taille, "#")
afficherLigne(taille, "i")