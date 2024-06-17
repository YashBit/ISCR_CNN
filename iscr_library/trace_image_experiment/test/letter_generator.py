from pylatex import Document, NoEscape
import argparse

def create_pdf(letter, font_name, typeface, command):
    doc = Document()
    doc.packages.append(NoEscape(r'\usepackage[T1]{fontenc}'))
    doc.packages.append(NoEscape(r'\usepackage[utf8]{inputenc}'))
    doc.packages.append(NoEscape(r'\usepackage{lmodern}'))
    doc.packages.append(NoEscape(r'\usepackage{textcomp}'))
    doc.packages.append(NoEscape(r'\usepackage{lastpage}'))
    doc.packages.append(NoEscape(r'\usepackage{graphicx}'))

    # Add the font package
    doc.packages.append(NoEscape(r'\usepackage{' + font_name + '}'))

    setline_command = r"""
    \newcommand{\setline}[2]{%
        \noindent\scalebox{#1}{#2}%
    }
    """
    doc.append(NoEscape(setline_command))

    doc.append(NoEscape(r'\begin{document}'))
    doc.append(NoEscape(r'\normalsize'))
    doc.append(NoEscape(command % letter))
    doc.append(NoEscape(r'\end{document}'))

    pdf_filename = f"{letter}_{font_name}_{typeface}"
    doc.generate_pdf(pdf_filename, clean_tex=False, clean=False)

def letter_generator(letter, font_name, typeface):
    typefaces = {
        "normal": r'\textnormal{\setline{35}{%s}}',
        "italic": r'\textit{\setline{35}{%s}}',
        "bold": r'\textbf{\setline{35}{%s}}',
        "bolditalic": r'\textbf{\textit{\setline{35}{%s}}}',
        "smallcaps": r'\textsc{\setline{35}{%s}}',
        "slanted": r'\textsl{\setline{35}{%s}}'
    }
    print(f"Typeface received: {typeface}")
    if typeface in typefaces:
        create_pdf(letter, font_name, typeface, typefaces[typeface])
    else:
        raise ValueError(f"Unknown typeface: {typeface}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create trace alphabet')
    parser.add_argument('--letter', type=str, required=True, help='Letter to be traced (a-z)')
    parser.add_argument('--font', type=str, required=True, help='Font name')
    parser.add_argument('--typeface', type=str, required=True, choices=['normal', 'italic', 'bold', 'bolditalic', 'smallcaps', 'slanted'], help='Typeface (normal, italic, bold, bolditalic, smallcaps, slanted)')
    args = parser.parse_args()
    letter_generator(args.letter, args.font, args.typeface)
