__copyright__ = '''
seqpy/cmds/__init__.py - part of seqpy

(c) 2006 - 2012 Hidayat Trimarsanto <anto@eijkman.go.id> / <trimarsanto@gmail.com>

All right reserved.
This software is licensed under GPL v3 or later version.
Please read the README.txt of this software.
'''

import sys, os
import argparse
import importlib
import seqpy

def execute(args):
    if len(args) < 1:
        usage()

    command = args[0]
    M = importlib.import_module('seqpy.cmds.' + command)
    print(M)
    parser = M.init_argparser()
    args = parser.parse_args( args[1:] )
    M.main( args )


def arg_parser( description = None ):

    parser = argparse.ArgumentParser( description = description )

    parser.add_argument('--noattr', action='append_const', dest='io_opts', const = 'noattr',
            help = 'do not read or write sequence attribute within fasta format')

    return parser
