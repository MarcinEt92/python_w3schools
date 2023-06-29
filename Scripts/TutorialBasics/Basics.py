import copy
import datetime
import json
import TutorialBasics.HelperClasses.Person
import re
from TutorialBasics.HelperClasses.Person import Person, Student
from TutorialBasics.HelperClasses.IteratorNumbers import IteratorNumbers
from TutorialBasics.HelperClasses.VehiclePolymorph import Vehicle, Plane

class Basics:

    @classmethod
    def variables(cls):
        cls.casting()
        cls.unpack_collection()
        cls.output_variables()

    @classmethod
    def casting(cls):
        print("\n ==================== casting ==================== \n")
        number_str = "3"
        number_int = int(number_str)
        print(f"{number_str} is {type(number_str)} and can be converted to {type(int(number_str))}")

    @classmethod
    def unpack_collection(cls):
        print("\n ==================== unpack_collection ==================== \n")
        fruits = ["orange", "apple", "pear"]
        orange, apple, pear = fruits
        print(f"Fruits: {orange}, {apple}, {pear}")

    @classmethod
    def output_variables(cls):
        print("\n ==================== output_variables ==================== \n")
        a, b = 10, 5
        c = "word"
        print(f"python adds numbers and prints them: a + b = {a + b}")
        try:
            result = a + c
        except TypeError:
            print("Cannot add number and string")

    @classmethod
    def strings_and_collections(cls):
        cls.string_operations()
        cls.list_operations()
        cls.list_comprehensions()
        cls.list_sorting()
        cls.tuple_operations()
        cls.set_operations()
        cls.set_operations_part_2()
        cls.dict_operations()
        cls.nested_dict()

    @classmethod
    def string_operations(cls):
        print("\n ==================== string_operations ==================== \n")
        iterable = ["a", "b", "c"]
        string = " a new sentence "
        print(f"sentence upper: {string.upper()}")
        print(f"sentence capitalized: {string.capitalize()}")
        print(f"sentence remove whitespace: {string.strip()}")
        print(f"letter \"e\" occurrs {string.lower().count('e')} times in a sentence")
        print(f"does sentence end with \"tence\": {string.strip().endswith('tence')}")
        print(f"letter \"e\" found at index: {string.index('e')}")
        print(f"join method returns concat string: {','.join(iterable)}")

    @classmethod
    def list_operations(cls):
        print("\n ==================== list_operations ==================== \n")
        fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
        fruit_list[1:3] = ["plum", "grape"]
        print(f"List replacements: {fruit_list}")
        fruit_list.insert(1, 'pear')
        print(f"List insert: {fruit_list}")
        fruit_list.append("blaccurant")
        print(f"List append: {fruit_list}")
        fruit_list.extend(["tangerine"])
        print(f"List extend: {fruit_list}")
        fruit_list.remove("grape")
        print(f"List remove banana: {fruit_list}")
        fruit_list.pop(3)
        print(f"List remove specified index: {fruit_list}")

    @classmethod
    def list_comprehensions(cls):
        print("\n ==================== list_comprehensions ==================== \n")
        fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
        fruit_list_with_a_letter = [fruit.title() for fruit in fruit_list if "a" in fruit]
        print(f"fruit_list_with_a_letter: {fruit_list_with_a_letter}")

    @classmethod
    def list_sorting(cls):
        print("\n ==================== list_sorting ==================== \n")
        fruit_list = ["cherry", "apple", "banana", "orange", "kiwi", "mango", "blaccurant"]
        fruit_list.sort(reverse=True, key=lambda fruit: len(fruit))
        print(f"Default sorting: {fruit_list}")

    @classmethod
    def tuple_operations(cls):
        print("\n ==================== tuple_operations ==================== \n")
        fruit_tuple = tuple(["cherry", "apple", "banana", "orange", "kiwi", "mango", "blaccurant"])
        # tuples can be added and multiplied
        fruit_tuple = fruit_tuple * 2
        print(f"Doubled fruit tuple: {fruit_tuple}")
        print(f"fruit tuple index of apple: {fruit_tuple.index('apple')}")
        print(f"fruit tuple count of apple: {fruit_tuple.count('apple')}")

    @classmethod
    def set_operations(cls):
        print("\n ==================== set_operations ==================== \n")
        my_set = set(("a", "b", "c"))
        my_set.add("d")
        another_set = list(("e", "f"))
        my_set.update(another_set)
        my_set.remove("a")
        print(f"Set after add and update: {my_set}")

    @classmethod
    def set_operations_part_2(cls):
        print("\n ==================== set_operations_part_2 ==================== \n")
        set_1 = {"a", "b", "c"}
        set_2 = {1, 2, 3, "c"}
        set_union = set_1.union(set_2)
        set_intersection = set_1.intersection(set_2)
        set_sym_difference = set_1.symmetric_difference(set_2)
        print(f"Sets union: {set_union}")
        print(f"Sets intersection [only duplicates]: {set_intersection}")
        print(f"Sets symmetric difference [all but not duplicates]: {set_sym_difference}")

    @classmethod
    def dict_operations(cls):
        print("\n ==================== dict_operations ==================== \n")
        car_dict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
        }
        car_colors = dict(colors=["white", "black"], finnish=["polished", "satin", "mat"])

        car_dict.update(car_colors)
        car_dict.items()

        vehicles = ["bike", "car"]
        colors = "single color"
        vehicles_colors = dict.fromkeys(vehicles, colors)
        print(f"The dict: {car_dict}")
        print(f"Does dict contain \'brand\' key: {'brand' in car_dict}")
        print(f"Dict made from keys: {vehicles_colors}")

    @classmethod
    def nested_dict(cls):
        print("\n ==================== nested_dict ==================== \n")
        nested_d = {
            "person_1": {
                "name": "Mark",
                "surname": "Brown"
            },
            "person_2": {
                "name": "Jason",
                "surname": "Smith"
            }
        }

        print(f"Person 2 surname: {nested_d['person_2']['surname']}")

    @classmethod
    def functions_classes(cls):
        cls.lambda_expressions()
        cls.classes()
        cls.iterators_examples()
        cls.polymorphism()
        cls.modules()

    @classmethod
    def lambda_expressions(cls):
        print("\n ==================== lambda_expressions ==================== \n")
        x = lambda x: x * 2
        print(f"lambda expression: {x(5)}")

    @classmethod
    def classes(cls):
        print("\n ==================== classes ==================== \n")
        person_john = Person(name="John", age=33)
        print(f"Person John: {person_john}")
        print(f"Is {person_john.name} adult: {person_john.is_adult()}")

        student_mark = Student(name="Mark", age=21, grade=3)
        print(f"Student Mark: {student_mark}")
        print(f"Is {student_mark.name} adult: {student_mark.is_adult()}")

    # to do: https://www.w3schools.com/python/python_iterators.asp

    @classmethod
    def iterators_examples(cls):
        """iterator is an object which implements the iterator protocol, methods __iter__() and __next__()"""
        print("\n ==================== iterators_examples ==================== \n")
        fruit_tuple = ("apple", "pineapple")
        fruit_iterator = iter(fruit_tuple)
        print(f"next item of fruit_iterator: {next(fruit_iterator)}")
        print(f"next item of fruit_iterator: {next(fruit_iterator)}\n")

        numbers = IteratorNumbers()
        numbers_iterator = iter(numbers)
        print(f"next item of numbers_iterator: {next(numbers_iterator)}")
        print(f"next item of numbers_iterator: {next(numbers_iterator)}")

        print("\nIterating over numbers_iteration with for loop:\n")
        # new iterator is required
        for number in iter(IteratorNumbers()):
            print(f"number: {number}")

    @classmethod
    def polymorphism(cls):
        print("\n ==================== polymorphism ==================== \n")
        car = Vehicle("Ford", "Fiesta")
        plane = Plane(brand="Boeing", model="737", number_of_wings=2)
        plane_default = Plane()
        for vehicle in (car, plane, plane_default):
            print(vehicle, end=", ")
            vehicle.move()

    @classmethod
    def modules(cls):
        print("\n ==================== modules ==================== \n")
        print(Person)
        print(f"Module names: {dir(Person)}")

    @classmethod
    def date_time(cls):
        print("\n ==================== date_time ==================== \n")
        date_time_now = datetime.datetime.now()
        print(f"Current date and time: {date_time_now}")

        # Return the year and name of weekday:
        print(f"Current year: {date_time_now.year}")
        print(f"Current name of weekday: {date_time_now.strftime('%A')}")

        # create date_time object with specific time
        date_specific = datetime.datetime(2022, 12, 29)
        print(f"Specific date: {date_specific}, name of the month: {date_specific.strftime('%B')}")


    @classmethod
    def others(cls):
        cls.json_works()
        cls.reg_expressions()
        cls.string_formatting()

    @classmethod
    def json_works(cls):
        print("\n ==================== json_works ==================== \n")
        # parse json to python dictionary
        json_sample = '{ "name":"John", "age":30, "city":"New York"}'
        sample_dict = json.loads(json_sample)
        print(f"json converted to dict: {sample_dict}\n")

        # convert dict to json
        sample_dict = {
            "name": "John",
            "surname": "Smith",
            "age": 34
        }

        sample_json = json.dumps(sample_dict, indent=4, sort_keys=True)
        print(f"dict converted to json: {sample_json}")

    @classmethod
    def reg_expressions(cls):
        print("\n ==================== reg_expressions ==================== \n")
        text = "The rain in Spain"
        searched = re.search("^The.*Spain$", text)
        if searched: print(f"Yes, regex searched: {searched}")

        # another ex:
        txt = "The rain in Spain"
        searched = re.search("ai", txt)
        searched = re.search("^The.*Spain$", text)
        print(f"x searched and found at index: {searched.start()}, end at: {searched.end()}, span: {searched.span()}")

    @classmethod
    def string_formatting(cls):
        print("\n ==================== string_formatting ==================== \n")
        number = 5.345
        print(f"formatetd string: {number: .2f}")









# https://www.w3schools.com/python/python_sets.asp - to do




