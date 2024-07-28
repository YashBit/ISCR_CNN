from pylatex import Document, NoEscape
import argparse

def create_pdf(letter, font_name, typeface, command, size):
    doc = Document()
    
    doc.packages.append(NoEscape(r'\usepackage[T1]{fontenc}'))
    doc.packages.append(NoEscape(r'\usepackage[utf8]{inputenc}'))
    doc.packages.append(NoEscape(r'\usepackage{' + font_name + '}'))
    doc.packages.append(NoEscape(r'\usepackage{textcomp}'))
    doc.packages.append(NoEscape(r'\usepackage{lastpage}'))
    doc.packages.append(NoEscape(r'\usepackage{graphicx}'))

    setline_command = r"""
    \newcommand{\setline}[2]{%
        \noindent\scalebox{#1}{#2}%
    }
    """
    doc.append(NoEscape(setline_command))

    doc.append(NoEscape(r'\begin{document}'))
    doc.append(NoEscape(r'\normalsize'))
    doc.append(NoEscape(command % (size, letter)))
    doc.append(NoEscape(r'\end{document}'))

    pdf_filename = f"{letter}_{font_name}_{typeface}_{size}"
    doc.generate_pdf(pdf_filename, clean_tex=False, clean=False)

def letter_generator(letter, font_name, typeface, size):
    typefaces = {
        "normal": r'\textnormal{\setline{%s}{%s}}',
        "italic": r'\textit{\setline{%s}{%s}}',
        "bold": r'\textbf{\setline{%s}{%s}}',
        "bolditalic": r'\textbf{\textit{\setline{%s}{%s}}}',
        "smallcaps": r'\textsc{\setline{%s}{%s}}',
        "slanted": r'\textsl{\setline{%s}{%s}}'
    }
    print(f"Typeface received: {typeface}")
    print(f"Font received: {font_name}")
    if typeface in typefaces:
        create_pdf(letter, font_name, typeface, typefaces[typeface], size)
    else:
        raise ValueError(f"Unknown typeface: {typeface}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create trace alphabet')
    parser.add_argument('--letter', type=str, required=True, help='Letter to be traced (a-z)')
    parser.add_argument('--font', type=str, required=True, help='Font name')
    parser.add_argument('--typeface', type=str, required=True, choices=['normal', 'italic', 'bold', 'bolditalic', 'smallcaps', 'slanted'], help='Typeface (normal, italic, bold, bolditalic, smallcaps, slanted)')
    parser.add_argument('--size', type=float, required=True, help='Size of the letter')
    args = parser.parse_args()
    letter_generator(args.letter, args.font, args.typeface, args.size)
