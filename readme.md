#rlundo

rlundo grants interactive interpreters magical undo powers!
Some interpreters work without requiring compiling
a new readline library:

    $ python rlundo.py python
    $ python rlundo.py ipython

You can undo using ctrl+c

![undo with ctrl+c](http://ballingt.com/assets/undoable_ipython.gif)

The goal is for this to work with any interpreter, as in

    $ python rlundo.py /usr/bin/irb

![rlundo preview example](http://ballingt.com/assets/rlundopreview.gif)

which will work if you compile the modified readline library with

    cd rlundoable
    make -f Makefileosx

There are three major parts to this project:

* rlundoable - a patch for readline that makes it fork to save state
* rewrite.py - rewinds the terminal state to how it was at the last prompt
* undoableINTERPRETER - alternative scripts for running specific interactive interpreters so that they have undo

##rlundoable

try it with 

    $ python rlundo.py /usr/bin/irb


##rewrite.py

try it with 

    $ python rewrite.py

and then in another terminal run

    nc localhost 4242

to save terminal states, and

    nc localhost 4243

to restore previous terminal states

##Running the tests

* nosetests
* you're need to install a recent version of tmux, 1.9a seems to work


---

##License

Copyright 2015 Thomas Ballinger

Released under GPL3, like GNU readline.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
