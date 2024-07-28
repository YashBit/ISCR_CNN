from pylatex import Document, NoEscape
import argparse  

def create_trace_alphabet(letter, font_name, size, typeface):
    # Create a Document object
    doc = Document()
    doc.packages.append(NoEscape(r'\usepackage[T1]{fontenc}'))
    doc.packages.append(NoEscape(r'\usepackage[utf8]{inputenc}'))
    doc.packages.append(NoEscape(r'\usepackage{lmodern}'))
    doc.packages.append(NoEscape(r'\usepackage{textcomp}'))
    doc.packages.append(NoEscape(r'\usepackage{lastpage}'))
    doc.packages.append(NoEscape(r'\usepackage{graphicx}'))
    doc.packages.append(NoEscape(r'\usepackage{' + font_name + '}'))
    setline_command = r"""
    \newcommand{\setline}[2]{%
        \noindent\scalebox{#1}{\pdfliteral{q 1 Tr [.1 .4]0 d .1 w}#2\pdfliteral{Q}}%
    }
    """
    doc.append(NoEscape(setline_command))
    doc.append(NoEscape(r'\begin{document}'))
    doc.append(NoEscape(r'\normalsize'))

    typefaces = {
        "normal": r'\textnormal{\setline{%s}{%s}}' % (size, letter),
        "semibold": r'\textbf{\setline{%s}{%s}}' % (size, letter),
        "italic": r'\textit{\setline{%s}{%s}}' % (size, letter),
        "slanted": r'\textsl{\setline{%s}{%s}}' % (size, letter),
        "bolditalic": r'\textbf{\textit{\setline{%s}{%s}}}' % (size, letter)
    }

    if typeface in typefaces:
        doc.append(NoEscape(typefaces[typeface]))
    else:
        raise ValueError(f"Unknown typeface: {typeface}")
    
    doc.append(NoEscape(r'\vspace{1cm}'))
    doc.append(NoEscape(r'\end{document}'))

    pdf_filename = f"{letter}_trace_{font_name}_{size}_{typeface}"
    doc.generate_pdf(pdf_filename, clean_tex=False, clean=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create trace alphabet')
    parser.add_argument('--font', type=str, required=True, help='Font name')
    parser.add_argument('--letter', type=str, required=True, help='Letter to be traced')
    parser.add_argument('--size', type=float, required=True, help='Size of the letter')
    parser.add_argument('--typeface', type=str, required=True, choices=['normal', 'semibold', 'italic', 'slanted', 'bolditalic'], help='Typeface')
    args = parser.parse_args()
    create_trace_alphabet(args.letter, args.font, args.size, args.typeface)
