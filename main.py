"""
License: Apache
Organization: UNIR
Team: 3101D
Hazel
Abel
David
Lilian
"""

import os
import sys
from collections import defaultdict

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

def count_occurrences(items):
    occurrences = defaultdict(int)
    for item in items:
        occurrences[item] += 1
    return occurrences

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff","howards"]


    word_occurrences = count_occurrences(word_list)


    repeated_words = defaultdict(list)
    for word, count in word_occurrences.items():
        if count > 1:
            repeated_words[count].append(word)

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_word_list = sort_list(word_list)
    print(" ")
    print("Lista ordenada de palabras:")
    print(sorted_word_list)
    print(" ")
    for count, words in repeated_words.items():
        print(f"Palabras que se repiten {count} veces:")
        print(words)
