def verifieCode(codeSecret):
    code = ""
    while code != codeSecret :
        code = input("Entrez le code :\n")

verifieCode("4242")
print("Premier code bon.")
verifieCode("2121")
print("Bravo.")

