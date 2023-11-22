"""
Print the location of the primary docs makefile
"""
from os import path

if __name__ == "__main__":
    print(path.join(path.split(__file__)[0], 'Makefile'))
