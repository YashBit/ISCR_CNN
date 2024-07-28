from pylatex import Document, NoEscape
import argparse  

def create_trace_alphabet(letter, font_name):
    # Create a Document object
    doc = Document()
    doc.packages.append(NoEscape(r'\usepackage[T1]{fontenc}'))
    doc.packages.append(NoEscape(r'\usepackage[utf8]{inputenc}'))
    doc.packages.append(NoEscape(r'\usepackage{lmodern}'))
    doc.packages.append(NoEscape(r'\usepackage{textcomp}'))
    doc.packages.append(NoEscape(r'\usepackage{lastpage}'))
    doc.packages.append(NoEscape(r'\usepackage{graphicx}'))
    doc.packages.append(NoEscape(r'\usepackage{fontspec}'))
    doc.packages.append(NoEscape(r'\setmainfont{' + font_name + '}'))

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
    pdf_filename = letter + '_trace' + '_' + font_name
    doc.generate_pdf(pdf_filename, clean_tex=False, clean=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create trace alphabet')
    parser.add_argument('--font', type=str, help='Font name')
    parser.add_argument('--letter', type=str, help='Letter to be traced')
    args = parser.parse_args()
    create_trace_alphabet(args.letter, args.font)