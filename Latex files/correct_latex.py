import os
import fnmatch
import re

"""
This script corrects several errors/integrations in a given .tex file.
    - It corrects the admonitions by replacing the framed environment with the appropriated block from the awesomebox package.
    - It corrects the subfigures by replacing the figure environment with the subfigure environment.
    - It corrects the videos by adding the video logo to the figure environment.
    - It corrects the bibliography by replacing the \citep command with the \parencite command.

Usage:
    1. Place this script in the same directory as your .tex files
    2. Run the script
    3. The script will correct all .tex files in the directory
"""

def extract_data():
    # Extract the data from the index.tex file
    with open('index.tex', 'r') as file:
        content = file.read()

    # Acronyms
    acronyms = re.findall(r'%{5,}\s*acronyms\s*(.*?)%{5,}\s*', content, re.DOTALL)[0]
    print(acronyms)

    # return glossary, acronyms, includes

def make_glossary():
    # Copy the data at the right places in the main.tex file
    
    glossary, acronyms, includes = extract_data()

    with open('index.tex', 'r') as file:
        content = file.read()

    with open('main.tex', 'w') as file:
        file.write(content)

def correct_admonitions_images(text: str) -> str:

    # Define the patterns for the admonitions
    admonition_patterns = [r"(\\begin\{noteblock\}.*?\\end\{noteblock\})",
                           r"(\\begin\{tipblock\}.*?\\end\{tipblock\})",
                           r"(\\begin\{warningblock\}.*?\\end\{warningblock\})",
                           r"(\\begin\{importantblock\}.*?\\end\{importantblock\})",
                           r"(\\begin\{cautionblock\}.*?\\end\{cautionblock\})",
                           r"(\\begin\{awesomeblock\}.*?\\end\{awesomeblock\})",
                           r"(\\begin\{exercise\}.*?\\end\{exercise\})"]
    
    for admonition_pattern in admonition_patterns:
        admonitions = re.findall(admonition_pattern, text, re.DOTALL)
        modified_admonitions = []
        for admonition in admonitions:
            # Suppress the beginning of the figure environment
            admonition = re.sub(r"\\begin{figure}\[!htbp\]\s*\\centering\s*",
                                r"", admonition, flags=re.DOTALL)
            # Suppress the end of the figure environment
            admonition = re.sub(r"\\caption\[\].*?\\end{figure}",
                                r"", admonition, flags=re.DOTALL)
            # Correct the size of the image
            admonition = re.sub(r"\\includegraphics\[.*?\]{(.*?)}",
                                r"\\bigskip\\includegraphics[width=0.5\\linewidth, center]{\1}", admonition, flags=re.DOTALL)
            # Append the modified main figure environment to the list of modified main figures
            modified_admonitions.append(admonition)

        # Replace the admonitions in the text
        for admonition, modified_admonition in zip(admonitions, modified_admonitions):
            text = text.replace(admonition, modified_admonition)

    return text

def correct_footnotes_images(text: str) -> str:
    text = re.sub(r"\\footnote\{(.*?)\n\n\\begin\{figure\}\[!htbp\]\s*\\centering\s*\\includegraphics\[width=(.*?)\\linewidth\]\{(.*?)\}\s*\\caption\*\{(.*?)\}\s*\\end\{figure\}\}",
                  r"\\footnote{\1\n\\includegraphics[width=0.5\\linewidth, center]{\3}}", text)
    return text

def correct_biblio(text: str) -> str:
    text = re.sub(r"\\citep", r"\\parencite", text)
    return text

def correct_videos(text: str) -> str:
    text = re.sub(r"\\begin{figure}\[!htbp\]\n\\centering\n\\caption", 
                  r"\\begin{figure}[!htbp]\n\\centering\n\\includegraphics[width=0.25\\linewidth]{Images/video_logo.png}\n\\caption", 
                  text, flags=re.DOTALL)
    
    return text

def correct_subfigures(text: str) -> str:
    """
    Corrects the subfigures in the given text.
    Replaces the figure environment with the subfigure environment.

    Args:
        text (str): The text containing the subfigures

    Returns:
        str: The text with the corrected subfigures
    """

    # Define the pattern for a main figure environment
    main_figure_pattern = r"(\\begin{figure}\[!htbp\]\s*\\centering\s*\\begin{figure}\[!htbp\].*?\\end{figure}\s*\\caption\[\]{.*?}\s*\\label{.*?}\s*\\end{figure})"

    # Define the pattern for a nested figure environment
    nested_figure_pattern = r"(\\begin{subfigure}.*?\\end{figure})"

    # Find all main figure environments
    main_figures = re.findall(main_figure_pattern, text, re.DOTALL)

    # For each main figure environment, replace \begin{figure} and \end{figure} with \begin{subfigure} and \end{subfigure}
    modified_main_figures = []
    for main_figure in main_figures:
        # Replace \begin{figure} with \begin{subfigure}
        main_figure = re.sub(r"\n\\begin{figure}\[!htbp\]", r"\n\\begin{subfigure}", main_figure)
        # Find all nested figure environments
        nested_figures = re.findall(nested_figure_pattern, main_figure, re.DOTALL)
        # Replace \begin{figure} and \end{figure} with \begin{subfigure} and \end{subfigure} in each nested figure environment
        modified_nested_figures = [re.sub(r"\\begin{subfigure}", r"\\begin{subfigure}{\\textwidth}", re.sub(r"\\end{figure}", r"\\end{subfigure}", nested_figure)) for nested_figure in nested_figures]
        # Replace each nested figure environment in the main figure environment with the modified nested figure environment
        for nested_figure, modified_nested_figure in zip(nested_figures, modified_nested_figures):
            main_figure = main_figure.replace(nested_figure, modified_nested_figure)
        # Correct the label of the main figure environment
        main_figure = re.sub(r"\\label{(.*?)-(.*?)}\s*\\end{figure}", r"\\label{\1}\n\\end{figure}", main_figure)
        # Append the modified main figure environment to the list of modified main figures
        modified_main_figures.append(main_figure)

    # Replace each main figure environment in the text with the modified main figure environment
    for main_figure, modified_main_figure in zip(main_figures, modified_main_figures):
        text = text.replace(main_figure, modified_main_figure)
    
    return text

# Function to correct the admonitions in the given text
def correct_admonitions(text: str) -> str:
    """
    Corrects the admonitions in the given text.
    Replaces the framed environment with the tipblock or noteblock environment.

    Args:
        text (str): The text containing the admonitions

    Returns:
        str: The text with the corrected admonitions
    """

    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Hint\}\\\\(.*?)\\end\{framed\}', r'\\begin{tipblock}\1\\end{tipblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Note\}\\\\(.*?)\\end\{framed\}', r'\\begin{noteblock}\1\\end{noteblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Attention\}\\\\(.*?)\\end\{framed\}', r'\\begin{warningblock}\1\\end{warningblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Warning\}\\\\(.*?)\\end\{framed\}', r'\\begin{warningblock}\1\\end{warningblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Important\}\\\\(.*?)\\end\{framed\}', r'\\begin{importantblock}\1\\end{importantblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Caution\}\\\\(.*?)\\end\{framed\}', r'\\begin{cautionblock}\1\\end{cautionblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Question\}\\\\(.*?)\\end\{framed\}', r'\\begin{awesomeblock}[teal]{2pt}{\\faQuestionCircle}{teal}\1\\end{awesomeblock}', text, flags=re.DOTALL)
    # text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Exercice\}\\\\(.*?)\\end\{framed\}', r'\\begin{awesomeblock}[violet]{2pt}{\\faEdit}{violet}\1\\end{awesomeblock}', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{framed\}\s*\\textbf\{Exercice\}\\\\(.*?)\\end\{framed\}', r'\\begin{exercise}\1\\end{exercise}', text, flags=re.DOTALL)
    return text

def correct_tex_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Correct the admonitions in the given file
    content = correct_admonitions(content)
    # Correct the admonitions images in the given file
    content = correct_admonitions_images(content)
    # Correct the footnotes images in the given file
    content = correct_footnotes_images(content)
    # Correct the subfigures in the given file
    content = correct_subfigures(content)
    # Correct the videos in the given file
    content = correct_videos(content)
    # Correct the bibliography in the given file
    content = correct_biblio(content)

    with open(file_path, 'w') as file:
        file.write(content)

def correct_all_tex_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.tex'):
            correct_tex_file(file)

def correct_bib_file():
    with open('main.bib', 'r') as file:
        content = file.read()

    content = re.sub(r'\n\thowpublished =(.*?),', r'', content, flags=re.DOTALL)

    with open('main.bib', 'w') as file:
        file.write(content)

# Call the function with the path to your .tex file
if __name__ == '__main__':
    correct_all_tex_files()
    correct_bib_file()
    make_glossary()
    extract_data()
