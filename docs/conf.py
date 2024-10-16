# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LIMA'
copyright = '2024, Universidad de Costa Rica EIE'
author = 'Mauricio Rodriguez Obando-Erick Carvajal-Bryan Mora'
#repo = "https://github.com/lima-ucr/OpenLane_docs_es"
#branch = "master"
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

source_suffix = {
    ".rst": "restructuredtext",
}

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'README.md',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "LIMA"
html_theme = 'sphinx_rtd_theme'
html_logo = '../img/LogoUCRtransparentePNG.png'
html_css_files = [
    'style.css',
]

html_static_path = ['_static']

numfig = True