# Makefile for running tests to be compatible with sphinx documentation
#

# Makefile for generating Sphinx documentation
# run make help to list the commands. Bash completion can also sometimes list available commands

# most of the rules already exist in a template that is installed with wield.docs. You can run the command to find that file
include $(shell python -m wield.sphinx.docs.makefile)

# the documentation actually lives in the docs folder
DOCDIR = docs

# include any additional rules, variable overrides, or alternate rules after the include

