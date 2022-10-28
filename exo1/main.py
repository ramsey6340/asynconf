from exo1.mission_code import *


def exo1():
    print("===============EXO 1===============")
    again = 'o'
    num_planet = 0
    name_list = []
    while again == 'o':
        try:
            name = input(f"Nom du planète{num_planet}: ")
            if not name.isalpha() and name != '':
                raise ValueError
        except ValueError:
            print("La valeur entrée est incorrecte !")
        else:
            if name != '':
                name_list.append(name)
                num_planet += 1
            else:
                again = 'n'
                my_dict_code = code_dictionnary(name_list)
                print("La code de la mission est: ", mission_code(my_dict_code))
