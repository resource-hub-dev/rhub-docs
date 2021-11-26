# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path


# -- Path setup --------------------------------------------------------------

root = Path(__file__).parent.resolve()


# -- Project information -----------------------------------------------------

project = 'Resource Hub'
copyright = '2021, Red Hat, Inc.'
author = 'Red Hat, Inc.'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.direnv']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_logo = '_static/logo.png'
html_static_path = ['_static']
html_css_files = ['custom.css']
