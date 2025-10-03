"""
Module de lecture et traitement de données depuis un fichier CSV.
"""
#### Imports et définition des variables globales
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row]
            l.append(row)
    return l

def get_list_k(data, k):
    """Retourne la k-ième liste convertie en entiers."""
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste converti en entier."""
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste converti en entier."""
    return l[-1]

def get_max(l):
    """Retourne le maximum de la liste convertie en entiers."""
    return max(l)

def get_min(l):
    """Retourne le minimum de la liste convertie en entiers."""
    return min(l)

def get_sum(l):
    """Retourne la somme des éléments de la liste convertis en entiers."""
    s = 0
    for x in enumerate(l):
        s += x
    return s


#### Fonction principale


def main():
    """Fonction principale du programme."""
    data = read_data('listes.csv')
    for l in data:
        print(l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
