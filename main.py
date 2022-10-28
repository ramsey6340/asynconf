import exo1.main as exo1
import exo2.main as exo2
import exo3.main as exo3
import exo4.main as exo4
import exo5.main as exo5

NUM_EXO = [1, 2, 3, 4, 5]
AGAIN_LIST = ['o', 'n']


def main():
    again = 'o'
    numero_exercice = 0
    while again == 'o':

        while numero_exercice not in NUM_EXO:
            try:
                numero_exercice = int(input("Quel exercice voulez-vous exécuter ? "))
            except ValueError:
                print("La valeur saisie est incorrecte !")

        if numero_exercice == 1:
            exo1.exo1()
        elif numero_exercice == 2:
            exo2.exo2()
        elif numero_exercice == 3:
            exo3.exo3()
        elif numero_exercice == 4:
            exo4.exo4()
        elif numero_exercice == 5:
            exo5.exo5()
        else:
            print("Erreur: La valeur est incorrecte")

        again = 'a'
        numero_exercice = 0
        while again not in ['o', 'n']:
            again = input("Voulez-vous continuer (o/n)? ")
            again = again.lower()
    else:
        print("Au revoir !")


if __name__ == "__main__":
    main()
