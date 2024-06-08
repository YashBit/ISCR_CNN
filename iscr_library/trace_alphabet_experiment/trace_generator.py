from pylatex import Document, NoEscape

def create_latex_document():
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
    doc.append(NoEscape(r'\setline{35}{b}\vspace{1cm}'))
    doc.append(NoEscape(r'\end{document}'))
    pdf_filename = 'final_output.pdf'
    doc.generate_pdf(pdf_filename, clean_tex=False, clean=False)

if __name__ == "__main__":
    create_latex_document()
