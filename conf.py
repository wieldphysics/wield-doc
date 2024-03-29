#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@caltech.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.

import os
# set up the testing directory. This is relative to the CWD, which is also where conf.py is
os.environ.setdefault('TESTING_DIR', "./testing")

# most of the settings are provided here
from wield.sphinx.conf import *

# The master toctree document.
# master_doc = "docs/index"
# no need to put docs if sphinx-build called with docs as SOURCEDIR
master_doc = "index"

# General information about the project.
project = "wield"
copyright = "2023, Lee McCuller"
author = "Lee McCuller"
show_authors = False

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

version = "0.5.0"
# The full version, including alpha/beta/rc tags.
release = "0.5.0-dev"

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
# pygments_style = 'colorful'
pygments_style = "default"

# -- Options for sourcelinks
srclink_project = "https://github.com/wield/wield"
srclink_src_path = "src/wield/"
srclink_branch = "main"

html_title = "wield-physics documentation"
html_short_title = "wield"

# Output file base name for HTML help builder.
htmlhelp_basename = "wield"

# html_logo = 'docs/logo/logo_ws_block.svg'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = dict(
    description="Documentation for GQuEST design library",
    extra_nav_links={
        #'LIGO CDS repository' : 'https://git.ligo.org/CDS/dttxml'
    },
    show_powered_by=False,
    show_related=True,
    page_width='auto',
)


autodoc_mock_imports.extend([
    "pygraphviz",
    "pcaspy",
    "control",
])
