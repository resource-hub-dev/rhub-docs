# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import shutil
import logging
from pathlib import Path

import sh
import requests


logging.basicConfig(level=logging.INFO)


# -- Path setup --------------------------------------------------------------

root = Path(__file__).parent.resolve()

tmp = root / '_tmp'
tmp.mkdir(exist_ok=True)


# -- Project information -----------------------------------------------------

project = 'Resource Hub'
copyright = '2021, Red Hat, Inc.'
author = 'Red Hat, Inc.'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx_antsibull_ext',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.direnv', '_tmp']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_logo = '_static/logo.png'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]


# -- Event hooks -------------------------------------------------------------


def catch_wrap(fn):
    """
    Decorator to print more info about unhandled exception in sphinx event
    callbacks.
    """
    def inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            logging.exception(f'Exception in {fn.__name__}: {e!r}')
            raise
    return inner


@catch_wrap
def hook_init(app):
    sh.ansible_galaxy.collection.install('rhub.rhub')

    Path(f'{root}/ansible/autodoc/module').mkdir(parents=True, exist_ok=True)
    sh.antsibull_docs.plugin(
        'rhub.rhub.rhub_api',
        dest_dir=f'{root}/ansible/autodoc/module',
        plugin_type='module',
    )

    Path(f'{root}/ansible/autodoc/lookup').mkdir(parents=True, exist_ok=True)
    sh.antsibull_docs.plugin(
        'rhub.rhub.rhub_api',
        dest_dir=f'{root}/ansible/autodoc/lookup',
        plugin_type='lookup',
    )

    rhub_api = tmp / 'rhub-api'
    if rhub_api.exists():
        shutil.rmtree(rhub_api)
    sh.git.clone('https://github.com/resource-hub-dev/rhub-api.git', rhub_api,
                 branch='master', depth=1)
    sh.prance.compile(rhub_api / 'src/openapi/openapi.yml', '_static/openapi.json')


def setup(app):
    app.connect('builder-inited', hook_init)
