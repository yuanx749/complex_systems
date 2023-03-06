import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Modeling Complex Systems"
copyright = "2021, yuanx749"
author = "yuanx749"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]
default_role = "obj"

html_theme = "furo"
html_static_path = ["_static"]
html_title = project

autodoc_default_options = {
    "member-order": "bysource",
    "inherited-members": True,
    "imported-members": True,
}
autodoc_mock_imports = ["numpy", "scipy", "matplotlib", "networkx"]

autosummary_imported_members = True
autosummary_ignore_module_all = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "networkx": ("https://networkx.org/documentation/stable", None),
}

myst_enable_extensions = ["dollarmath"]
