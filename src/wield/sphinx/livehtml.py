#!/usr/bin/env python
import os
import sys
import shlex
import subprocess
from livereload import Server


import errno


def shell(cmd):
    """Execute a shell command.

    You can add a shell command::

        server.watch(
            'style.less', shell('lessc style.less', output='style.css')
        )

    :param cmd: a shell command, string or list
    :param output: output stdout to the given file
    :param mode: only works with output, mode ``w`` means write,
                 mode ``a`` means append
    :param cwd: set working directory before command is executed.
    :param shell: if true, on Unix the executable argument specifies a
                  replacement shell for the default ``/bin/sh``.
    """

    def run_shell():
        ret = subprocess.run(args=cmd, shell=True, capture_output=False)
    return run_shell


def ignore(path):
    if "_autosummary" in path:
        return True
    if "testing/" in path and "docs/" in path:
        return True
    return False


if __name__ == '__main__':
    server = Server()

    if len(sys.argv) == 1:
        arg = 'html'
    elif len(sys.argv) > 1:
        arg = sys.argv[1]

    cmd = shell('make {}'.format(arg))
    # run the build once before starting
    cmd()

    server.watch('./*.md', cmd, ignore=ignore)
    server.watch('./**/*.md', cmd, ignore=ignore)
    server.watch('./*.rst', cmd, ignore=ignore)
    server.watch('./**/*.rst', cmd, ignore=ignore)

    server.serve(root='build/sphinx/html')
