Styleguide
==========

List of tools, libraries and documents that specify all of the coding standards
used across the Resource Hub organization, either being backend, frontend,
infrastructure, etc.

The coding standards are separated per project, in a way that we can have
multiple styleguides inside of each project, i.e., a Python styleguide, along
with a Flask styleguide.

Backend
-------

Since the project's backend uses Python with Flask, we are relying on PEP8,
PEP257 and some other tools to comply with known standards across the Python
community, such as the `Python Code Quality Authority <PyCQA>`_


All coding standards are verified using `Prospector`_, which is a tool that
provides an interface to easily executing other linters, such as `Pylint`_
(static analysis), `Vulture`_ (find unused code), `Bandit`_ (security checks).

There are also some coding standards for additional languages used on the
backend as well, such as YAML and Bash.

.. _PyCQA: https://github.com/pycqa
.. _Prospector: https://prospector.readthedocs.io/en/latest/index.html
.. _Pylint: https://www.pylint.org
.. _Vulture: https://github.com/jendrikseipp/vulture
.. _Bandit: https://github.com/PyCQA/bandit

Frontend
--------

*TBD*

Infrastructure
--------------

*TBD*
