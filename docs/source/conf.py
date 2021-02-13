# See http://www.sphinx-doc.org/en/master/config
project = "apparatus"
copyright = "2019, Greenhouse AI team"
author = "Greenhouse AI team"

import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))

release = "0.0.0"

html_sidebars = {
    "**": [
        "localtoc.html",
        "globaltoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
    ]
}
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
