# -*- coding: utf-8 -*-

master_doc = 'index'

project = u'sphinx-book'
copyright = u'2013, sphinx-book'
version = '1.0'
release = '1.0'
language = 'ja'
exclude_patterns = ['_build', '_build_sample']
html_theme = 'default'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'sphinx-book.tex', u'sphinx-book Documentation',
   u'sphinx-book', 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'sphinx-book', u'sphinx-book Documentation',
     [u'sphinx-book'], 1)
]

