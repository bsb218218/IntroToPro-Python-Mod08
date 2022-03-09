# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SKang,3.8.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
listOfProductObjects = []
list_of_product_rows = []
table_lst = []
choice_str = ""


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SKang,3.8.22,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    # Constructor
    def __init__(self, product_name, product_price):
        """set product name and price of a new product """
        # Attributes
        try:
            self.product_name = str(product_name)
            self.product_name = float(product_price)
        except Exception as e:
            raise Exception("Error with setting values: \n" + str(e))

    # Properties
    # Product name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numeric")

    # Product price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Prices should be numeric")

    # Methods
    def __str__(self):
        """Convert product data to string"""
        return "[" + self.product_name + "," + str(self.product_price) + "]"

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product rows:

    methods:
        save_data_to_file(file_name, list_of_product_rows):

        read_data_from_file(file_name): -> (a list of product objects)

        add_data_to_list(name, price, list_of_product_rows):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SKang,3.8.2022,Modified code to complete assignment 8
    """
    #two functions (because it is about processing not data, you are going to use static method-don't use "self");
    # not need to create a new object each time; I can just call the functions directly

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_rows):
        """ Writes data from a list of product rows to a File

        :param file_name: (string) with name of file:
        :param list_of_product_rows: (list) you want filled with file data:
        :return: (list) of product rows
        """
        # TODO: Add Code Here!
        try:
            file = open(file_name, "w")
            for row in list_of_product_rows:
                file.write(str(row["Product"] + "," + str(row["Price"]))+ "\n")
            file.close()
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows


    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of product rows

        :param file_name: (string) with name of file:
        :return: (list) of product rows
        """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was an error")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows

    @staticmethod
    def add_data_to_list(name, price, list_of_product_rows):
        """ Adds data to a list of product rows

        :param name: (string) with name of product:
        :param price: (string) with price of product:
        :param list_of_product_rows: (list) you want filled with file data:
        :return: (list) of product rows
        """
        row = {"Product": str(name).strip(), "Price": str(price).strip()}
        # TODO: Add Code Here!
        list_of_product_rows.append(row)
        return list_of_product_rows


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ Performs Input and Output tasks

    methods:
        output_menu_options():
        input_menu_choice():
        output_current_items_in_list(list_of_product_rows):
        input_new_product_and_price():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SKang,3.8.2022,Modified code to complete assignment 8"""


    # each of the following will be functions
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_options():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show the current data
            2) Add a new item
            3) Save data to file        
            4) Exit program
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_items_in_list(list_of_product_rows: list):
        """ Shows the current items in the list of product rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items are: *******")
        for row in list_of_product_rows:
            print(row["Task"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user; product name and price
    @staticmethod
    def input_new_product_and_price():
        """  Gets product and price to be added to the list

        :return: (string, string) with product and price
        """
        # pass  # TODO: Add Code Here!
        try:
            print("Type in 'Product' and 'Price' for your product list")
            product_name = str(input(" Enter an Item: ")).strip()
            product_price = float(input(" Enter Price: ").strip())
            # print()
            productItem = Product(product_name=product_name, product_price=product_price)
        except Exception as e:
            print(e)
        return product_name, product_price

# Presentation (Input/Output)  -------------------------------------------- #




# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
try:
    list_of_product_rows = FileProcessor.read_data_from_file(strFileName)  # read file data

# Show user a menu of options
    while (True):
        IO.output_menu_options()  # Shows menu
        choice_str = IO.input_menu_choice()  # Get menu option

# Get user's menu option choice
    # Choice 1: Show user current data in the list of product objects
    # Choice 2: Let user add data to the list of product objects
    # Choice 3: let user save current data to file and exit program
        if choice_str.strip() == '1':
            IO.output_current_items_in_list(list_of_product_rows)  # Show current data in the list/table
            continue

        elif choice_str.strip() == '2':  # Add a new Task
            product_name, product_price = IO.input_new_product_and_price()
            table_lst = FileProcessor.add_data_to_list(name=product_name, price=product_price, list_of_product_rows=table_lst)
            continue  # to show the menu

        elif choice_str == '3':  # Save Data to File
            table_lst = FileProcessor.save_data_to_file(file_name=strFileName, list_of_product_rows=table_lst)
            print("Data Saved!")
            continue  # to show the menu

        elif choice_str == '4':  # Exit Program
            print("Goodbye!")
            break  # by exiting loop
except Exception as e:
    print("There was an error!")
    print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script  ---------------------------------------------------- #

