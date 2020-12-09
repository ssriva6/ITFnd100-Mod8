# ------------------------------------------------------------------------ #
# Title: Assignment 8
# Description: Working with classes

# ChangeLog (Who,When,What):
# SSrivatsan,12.8.2020,Created started script
# SSrivatsan,12.8.2020,Added pseudo-code to start assignment 8
# SSrivatsan,12.8.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
input_product = ""  # user input: for name of product
input_price = 0.0  # user input:  for price of product
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the Status message of the functions that are processing


class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RAyeni,11.27.2020,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name, product_price):
    #Attributes--
        self.product_name = product_name
        self.product_price = product_price

# Data and Processing -------------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RAyeni,11.27.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Read data from file and into a list of objects """

        # try except clause to hand FileNotFound errors
        try:
            
            list_of_product_objects.clear()
            file = open(file_name, "r")
            for line in file:
                # split each line and assign each field to variables and include item and price
                item, price = line.split(",")
                # use item and price as arguments to create product object and append
                list_of_product_objects.append(Product(item.strip(), float(price.strip())))
            file.close()
            return list_of_product_objects
        except FileNotFoundError: #if file is not found it will print the following statement
            print("\nFile is not present, skipping the reading process...\n")

    @staticmethod
    def write_data_to_file(file_name, list_of_product_objects):
        """ Write data to file """

        # open file and write
        file = open(file_name, "w")
        for obj in list_of_product_objects:
            file.write(obj.product_name + "," + str(obj.product_price) + "\n")
        file.close()
        # return confirmation message: include data saved to and file name
        return 'Data has successfully saved to ' + file_name + '.'


class ListProcessor:
    """ Contains functions to perform list operations """

    @staticmethod
    def add_object_to_list(item, price, list_of_product_objects): #adding on to current list
        """ use item and price parameters to create object
            and add to list
        """

        # creates an object from the Product class, and is appended to the list
        list_of_product_objects.append(Product(item.strip().capitalize(), price))
        return '\nProduct added.'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes input data for use in the program
    methods:
        print_menu_products():
        input_menu_choice():
        input_yes_no_choice()
        get_current_data_from_list()
        input_product_data()
        input_press_to_continue(optional_message='')

    """

    @staticmethod
    def print_menu_options():
        print("""
        Product List Application
        Main Menu:
        1. Print Current Products in List
        2. Add Product to List
        3. Save Product List to File and Exit
        4. Exit Program
        """)
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def get_current_data_from_list(list_of_objects):
        """ Shows current data in list """

        print("******* Current Products in List: *******")
        for obj in list_of_objects:
            print(obj.product_name + " (" + str(obj.product_price) + ")")
        print("*****************************************")

    # Get data from user product and price
    @staticmethod
    def input_product_data():
        """ Ask user for product data.
            Returns product and price to main part of script
        """
        strproduct = input("Enter Product: ")
        strprice = float(input("Enter Price: "))
        return strproduct, strprice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press [Enter] to continue. ')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while (True):
    # Display a menu of options and get users selection
    IO.print_menu_options()
    strChoice = IO.input_menu_choice()

    # SDisplay current data in the list of product objects
    if strChoice.strip() == '1':
        IO.get_current_data_from_list(lstOfProductObjects)
        IO.input_press_to_continue()
        continue

    #  add data to the list of product objects: Function to input item and price, assign to variable and list
    elif strChoice.strip() == '2':
        input_product, input_price = IO.input_product_data()
        strStatus = ListProcessor.add_object_to_list(input_product, input_price, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue

    # save current data to file and exit program
    elif strChoice.strip() == '3':
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            strStatus = FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
            print("Goodbye!")
            break
        else:
            IO.input_press_to_continue("Save Cancelled.") #if not- it will say save cancelled
            continue

    elif strChoice == '4':
        print("\nGoodbye!")
        break
