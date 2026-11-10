taches = []

def ajouter(titre):
    taches.append({"titre": titre, "fait": False})

def afficher():
    for i, t in enumerate(taches):
        etat = "OK" if t["fait"] else "A faire"
        print(f"{i}. [{etat}] {t['titre']}")

while True:
    cmd = input("ajouter / voir / fait / quitter : ")
    if cmd == "ajouter":
        ajouter(input("Titre : "))
    elif cmd == "voir":
        afficher()
    elif cmd == "fait":
        taches[int(input("N° : "))]["fait"] = True
    elif cmd == "quitter":
        break