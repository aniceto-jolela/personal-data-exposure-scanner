# Configuration file for the Sphinx documentation builder.

# -- Project information
import sphinx_rtd_theme


project = "personal data exposure scanner"
copyright = "2025, Aniceto"
author = "Aniceto"

# release = '0.1'
# version = '0.1.0'

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
]

ogp_site_name = "Personal data exposure scanner Documentation"
ogp_enable_meta_description = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "pip": ("https://pip.pypa.io/en/stable/", None),
    "nbsphinx": ("https://nbsphinx.readthedocs.io/en/latest/", None),
}

htmlhelp_basename = "PersonalDataExposureScannerdoc"

language = "en"

intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"
