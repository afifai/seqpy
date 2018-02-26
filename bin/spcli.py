#!/usr/bin/env python3

__copyright__ = '''
spcli - part of seqpy

(c) 2018 Hidayat Trimarsanto <anto@eijkman.go.id> / Afif Akbar Iskandar <afifai@sci.ui.ac.id>

All right reserved.
This software is licensed under GPL v3 or later version.
Please read the README.txt of this software.
'''

##
## spcli.py - seqpy command line interface
##

import sys, os

# prepare path to seqpy
sys.path.append( os.path.split( os.path.split(__file__)[0] )[0] )

import seqpy

def greet():
    seqpy.cerr('spcli - seqpy command line interface')
    seqpy.cerr('(C) 2011-2012 Hidayat Trimarsanto <trimarsanto@gmail.com>')

def usage():
    seqpy.cerr('  usage:')
    seqpy.cerr('    spcli scriptfile/CMD [ARGS]')
    seqpy.cerr('  try: spcli showcmds')
    sys.exit(0)

def main():

    greet()
    if len(sys.argv) == 1:
        usage()

    if sys.argv[1].endswith('.py'):
        # will execute a script file
        seqpy.cerr('Attempting to run script: %s' % sys.argv[1])
        with open(sys.argv[1]) as fh:
            code = compile( fh.read(), sys.argv[1], 'exec' )
            sys.argv = sys.argv[1:]
            _l = {}
            module = exec( code, None, _l )
            if 'main' in _l:
                globals().update( _l )
                main = _l['main']
                if 'init_argparser' in _l:
                    init_argparser = _l['init_argparser']
                    p = init_argparser()
                    args = p.parse_args(sys.argv[1:])
                    main(args)
                else:
                    main()

    elif sys.argv[1] == '-i':
        # interactive
        pass

    else:
        from seqpy import cmds
        cmds.execute( sys.argv[1:] )
        


if __name__ == '__main__':
    main()



