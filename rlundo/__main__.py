#!/usr/bin/env python

"""
rlundo

Start a repl with undo feature.
"""

from __future__ import unicode_literals
import sys
import os
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import rlundo

from rlundo.rlundoable import modify_env_with_modified_rl
from rlundo.termrewrite import run_with_listeners

from rlundo import interps


def start_undoable_rl(args):
    for command, predicate in interps.interpreters:
        if predicate(argobject.interpreter):
            #return run_with_listeners(command + argobject.interparg)
            return run_with_listeners(command)
    else:
        modify_env_with_modified_rl()
        #run_with_listeners(argobject.interpreter + argobject.interparg)
        run_with_listeners(argobject.interpreter)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='accepting an interpreter and any interpreter arguments into rlundo')
    parser.add_argument('interpreter', metavar='I', help='command to call the interpreter')
    #parser.add_argument('interparg', action='store_const', nargs='?', help='any arguments you can feed into the interpreter')
    argobject = parser.parse_args()
    print "XXXXXXXOOOOO"
    print argobject 
    start_undoable_rl(argobject)
