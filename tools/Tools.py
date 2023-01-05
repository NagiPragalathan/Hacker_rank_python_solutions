import os
import pathlib


def word_to_var(word):
    return "_".join(word.split())

def create_files():
    files = ['solution.py','question.txt','question.md']
    path = os.path.abspath(__file__)
    a=pathlib.Path(path).as_uri().split('tools')
    new_folder = a[0]+word_to_var(input("Enter string : ")+'/')
    os.mkdir(new_folder[8:])
    for i in files:
        with open(new_folder[8:]+i,'w') as file:
            file.close()

create_files()