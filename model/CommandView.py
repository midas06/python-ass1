import cmd
import os.path
from model.CmdFunction import *
import doctest


class Quitter(cmd.Cmd):
    """
    Simple command processor example
    """
    #a = Processor()
    cmdFunction = CmdFunction()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>>"

    def do_load_file(self, file_path):
        """

        :param file_path:
        :return:
        """
        self.cmdFunction = CmdFunction()
        print(self.cmdFunction.load_file(file_path))


    def do_display_good(self, msg):
        """

        :param msg:
        :return:
        """
        #self.a.database.print_all() #what to display if no file...
        #print(self.a.filer.get_file_path())
        self.cmdFunction.display_good(msg)
        #print(self.cmdFunction.display_good(msg))



    def do_display_bad(self, msg):
        """

        :param msg:
        :return:
        """
        #print(self.cmdFunction.display_bad(msg))
        self.cmdFunction.display_bad(msg)

    def do_edit_bad(self, value):
        """
        allows user to edit bad data
        :param value:
        :return:
        """
        self.cmdFunction.edit_bad(value)


    def do_quit(self, msg):
        """

        :param msg:
        :return:
        """
        #print("Quitting...")
        #return True
        #self.cmdFunction.quit(msg)
        quit = input("Are you sure you want to quit? Y/N \n>>>")
        if quit == 'Y':
            return True
        elif quit == 'N':
            pass
        else:
            print("Invalid answer")
            pass

    def do_display_graphs(self, p):
        """

        :param p:
        :return:
        """
        i = input("Press 1 to display BMI data\nPress 2 to display Gender data\nPress 3 to display Sales data\n")
        if i == "1" or i == "2" or i == "3":
            self.cmdFunction.display_graphs(i)
        else:
            print("Invalid input")

    do_lf = do_load_file
    do_dg = do_display_good
    do_db = do_display_bad
    do_eb = do_edit_bad
    do_q = do_quit
    do_dg = do_display_graphs


    def my_doctests(self):
        """
        >>> quitter.do_load_file("")
        No file/path entered

        >>> quitter.do_display_good("")
        No data to display. Please load a file

        >>> quitter.do_display_bad("")
        No data to display. Please load a file

        >>> quitter.do_load_file("test.txt")
        File loaded
        Good data: 0
        Bad data: 3

        >>> quitter.do_display_good("")
        No good data to display.

        >>> quitter.do_display_bad("")
        abc male 23000
        def female 12000
        ijk female 999

        >>> quitter.do_load_file("goodbadtest.csv") #why does it take female?
        File loaded
        Good data: 19
        Bad data: 2
        """

if __name__ == '__main__':
    quitter = Quitter()

    #c = CmdFunction()
    #doctest.testmod()
    quitter.cmdloop()

