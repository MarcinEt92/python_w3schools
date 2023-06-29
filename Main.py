# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from TutorialBasics.Basics import Basics


class Tutorial(Basics):
    @classmethod
    def start(cls):
        cls.print_options()
        cls.run()

    @classmethod
    def print_options(cls):
        print("W3 Tutorial:")
        print("\t1 - variables")
        print("\t2 - strings_and_collections")
        print("\t3 - functions_classes")
        print("\t4 - date_time")
        print("\t5 - others")

    @classmethod
    def run(cls):
        choice = int(input("\nChoose Option: "))
        options = {
            1: cls.variables,
            2: cls.strings_and_collections,
            3: cls.functions_classes,
            4: cls.date_time,
            5: cls.others
        }

        option = options.get(choice)
        option()


if __name__ == '__main__':
    Tutorial.start()
