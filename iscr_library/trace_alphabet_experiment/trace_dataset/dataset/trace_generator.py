from pylatex import Document, NoEscape
import argparse

def create_normal_alphabet(letter):
    # Create a Document object
    pass 

def create_trace_alphabet(letter):
    # Create a Document object
    doc = Document()
    doc.packages.append(NoEscape(r'\usepackage[T1]{fontenc}'))
    doc.packages.append(NoEscape(r'\usepackage[utf8]{inputenc}'))
    doc.packages.append(NoEscape(r'\usepackage{lmodern}'))
    doc.packages.append(NoEscape(r'\usepackage{textcomp}'))
    doc.packages.append(NoEscape(r'\usepackage{lastpage}'))
    doc.packages.append(NoEscape(r'\usepackage{graphicx}'))
    setline_command = r"""
    \newcommand{\setline}[2]{%
        \noindent\scalebox{#1}{\pdfliteral{q 1 Tr [.1 .4]0 d .1 w}#2\pdfliteral{Q}}%
    }
    """
    doc.append(NoEscape(setline_command))
    doc.append(NoEscape(r'\begin{document}'))
    doc.append(NoEscape(r'\normalsize'))
    doc.append(NoEscape(r'\setline{35}{' + letter + r'}\vspace{1cm}'))  # Use the letter variable
    doc.append(NoEscape(r'\end{document}'))
    pdf_filename = letter
    doc.generate_pdf(pdf_filename, clean_tex=False, clean=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--letter", type=str, help="The letter to create trace alphabet for")
    args = parser.parse_args()
    create_trace_alphabet(args.letter)
