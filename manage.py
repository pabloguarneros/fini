import os
import sys
from testing import tests


commands = {
    "test":tests.TestPortfolio()
}

if __name__ == "__main__":
    try:
        subcommand = sys.argv[1]
    except IndexError:
        subcommand = "help"  # Display help if no arguments were given.
    if subcommand == "test":
        os.system("bash -c 'python testing/tests.py'")
    else:
        sys.stdout.write("Command not yet implemented")