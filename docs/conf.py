# -*- coding: utf-8 -*-
#
# discord.py documentation build configuration file
import sys
import os
import re

on_rtd = os.getenv('READTHEDOCS') == 'True'
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.asyncio',
]
intersphinx_mapping = {
    'python': ('http://docs.python.org/3', None),
    'aiohttp': ('http://aiohttp.readthedocs.org/en/stable', None)
}

if on_rtd:
  extensions.append('sphinxcontrib.napoleon')
else:
  extensions.append('sphinx.ext.napoleon')

autodoc_member_order = 'bysource'

extlinks = {
    'issue': ('https://github.com/Rapptz/discord.py/issues/%s', 'issue '),
}

rst_prolog = """
.. |coro| replace:: This function is a |corourl|_.
.. |corourl| replace:: *coroutine*
.. _corourl: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'discord.py'
copyright = u'2015-2017, Rapptz'
version = ''
with open('../discord/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
language = None
exclude_patterns = ['_build']

pygments_style = 'friendly'
html_static_path = ['_static']
htmlhelp_basename = 'discord.pydoc'


# -- Options for manual page output ---------------------------------------
man_pages = [
    ('index', 'discord.py', u'discord.py Documentation',
     [u'Rapptz'], 1)
]

texinfo_documents = [
  ('index', 'discord.py', u'discord.py Documentation',
   u'Rapptz', 'discord.py', 'One line description of project.',
   'Miscellaneous'),
]

def setup(app):
  app.add_javascript('custom.js')
