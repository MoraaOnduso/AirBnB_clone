#!/usr/bin/python3
"""entry point for command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Implements the console for this project"""

    prompt = "(hbnb) "

    def do_quit(self, argv):
        """exit the console on execution"""
        return True

    def do_EOF(self, argv):
        """exits the program after receiving EOF signal."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
