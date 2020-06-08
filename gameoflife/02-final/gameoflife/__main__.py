import sys
from gameoflife.cli import cli
from gameoflife.gui import gui

if len(sys.argv) > 1:
    gui()
else:
    cli()
