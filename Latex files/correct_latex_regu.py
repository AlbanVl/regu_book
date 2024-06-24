import os
import fnmatch
import re
from correct_latex import *

"""
This script corrects the text for the Regulation book.

Usage:
    1. Place this script in the same directory as your .tex files
    2. Run the script
    3. The script will correct all .tex files in the directory
"""

# correct the size of the error table
def correct_error_table(text: str) -> str:

    text = re.sub(r"\\includegraphics\[width=0.7\\linewidth\]\{files/TableauErreurs(.*?)\}\n\\caption\[\]\{Tableau des erreurs en fonction de la classe du système\}", 
                  r"\\includegraphics[width=\\linewidth]{files/TableauErreurs\1}\n\\caption[]{Tableau des erreurs en fonction de la classe du système}",
                  text, flags=re.DOTALL)

    return text

def correct_regu_tex_files():
    for file_path in os.listdir('.'):
        if fnmatch.fnmatch(file_path, '*.tex'):
            with open(file_path, 'r') as file:
                content = file.read()

            # Correct the error table in the given file
            content = correct_error_table(content)

            with open(file_path, 'w') as file:
                file.write(content)

# Call the function with the path to your .tex file
if __name__ == '__main__':
    correct_all_tex_files()
    correct_regu_tex_files()
    correct_bib_file()
