import cmd
from CmdFunction import *
import doctest


class Controller(cmd.Cmd):

    cmdFunction = CmdFunction()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>>"

    def do_load_file(self, file_path):
        """
        Loads file - lf (filename/filepath)
        :param file_path: String - name of the file to be loaded
        :return:
        """
        self.cmdFunction = CmdFunction()
        print(self.cmdFunction.load_file(file_path))

    def do_display_good(self, msg):
        """
        Displays good data in a 2d table - dg
        :param  none
        :return: none
        """
        self.cmdFunction.display_good(msg)


    def do_display_bad(self, msg):
        """
        Displays bad data in a string array - db
        :param  none
        :return: none
        """
        self.cmdFunction.display_bad(msg)

    def do_edit_bad(self, value):
        """
        Allows user to edit bad data - eb
            Enter E to edit and D to delete
        :param  none
        :return: none
        """
        self.cmdFunction.edit_bad(value)

    def do_quit(self, msg):
        """
        Quits program - q
            Enter Y or N to exit
        :param none
        :return: none
        """
        quit = input("Are you sure you want to quit? Y/N \n>>>")
        if quit == 'Y' or quit == 'y':
            return True
        elif quit == 'N' or quit == 'n':
            pass
        else:
            print("Invalid input.")
            self.do_quit("")

    def do_display_graphs(self, value):
        """
        Displays graphs - dgr
        :param none
        :return: none
        """
        i = input("Press 1 to display BMI data\nPress 2 to display Gender data\nPress 3 to display Sales data\nPress 4 to display Bmi vs Gender data\n")
        if i == "1" or i == "2" or i == "3" or i == "4":
            self.cmdFunction.display_graphs(i)
        else:
            print("Invalid input")

    def do_serialize(self, value):
        """
        Serializes the dictionary of people as a pickle file
        :param none
        :return: none
        """
        i = input("Press 'D' to save to the Default directory,\nPress 'N' to save to a New directory.\n")
        if i == "D" or i == "d":
            self.cmdFunction.serialize(0)
        elif i == "N" or i == "n":
            self.cmdFunction.serialize(1)
        else:
            self.do_serialize("")

    def do_deserialize(self, value):
        """
        Deserializes pickled data dictionary
        :param none
        :return: none
        """
        try:
            i = input("Press 'D' to load from the Default directory,\nPress 'N' to load from to a New directory.\n")
            if i == "D" or i == "d":
                self.cmdFunction.deserialize(0)
            elif i == "N" or i == "n":
                self.cmdFunction.deserialize(1)
            else: self.do_deserialize()

        except IOError as no_file_err:
            print("No pickle file found")
            pass

    do_lf = do_load_file
    do_dg = do_display_good
    do_db = do_display_bad
    do_eb = do_edit_bad
    do_q = do_quit
    do_dgr = do_display_graphs

    def doctests(self):
        """
        >>> controller.do_load_file("test.txt")
        File loaded
        Good data: 0
        Bad data: 3

        >>> controller.do_display_good("")


        >>> controller.do_display_bad("")
        abc male 23000
        def female 12000
        ijk female 999

        >>> controller.do_load_file("goodbadtest.csv")
        File loaded
        Good data: 19
        Bad data: 3

        >>> controller.do_load_file("")
        No file/path entered

        >>> controller.do_display_good("")
        No data to display. Please load a file or run deserialize

        >>> controller.do_display_bad("")
        No data to display. Please load a file
        """


if __name__ == '__main__':
    controller = Controller()
    doctest.testmod()
    controller.cmdloop()

