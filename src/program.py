#
# Write the implementation for A2 in this file
#


# Use functions to: read a complex number from the console, write a complex number to the console, implement each required functionality.
# Functions communicate using input parameter(s) and the return statement (DO NOT use global variables)
# Each complex number should be represented as a list, tuple or dictionary (e.g. 1-2i as [1, -2], (1, -2) or {'real': 1, 'imag': -2} respectively).
# To access or modify numbers, use getter and setter functions.
# Separate input/output functions (those using print and input statements) from those performing the calculations (see program.py)
# Provide the user with a menu-driven console-based user interface. Input data should be read from the console and the results printed to the console.
# At each step, the program must provide the user the context of the operation (do not display an empty prompt).

### TEXT COLORS ###
tgreen = '\033[32m'  # Green Text
endc = '\033[m'  # reset to the defaults


### TEXT COLORS ###

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

def create_complex():
    """
    Creates a complex number with the input of the user
    :return: The complex number, after it is complete
    """

    nr = [''] * 2

    input_str = input("z = ")  # Input the complex number

    # Checking if there are any minuses and removing them so that I can
    # use the isdigit() function later on in the program

    if input_str[0] == '-':
        realp_negative = 1
        input_str = input_str[1:]

        if input_str[2] == '-':
            imaginaryp_negative = 1
        else:
            imaginaryp_negative = 0
    else:
        realp_negative = 0

        if input_str[2] == '-':
            imaginaryp_negative = 1
        else:
            imaginaryp_negative = 0

    ##############################################

    input_str = input_str.rstrip('i')  # Remove the last i so that isdigit()
    # works properly

    for word in input_str.split():
        if word.isdigit():  # Split input_str into words and extract the digits, assigning them to their
            if nr[0] == '':  # corresponding positions, also keeping track of their sign
                set_realp(nr, word, realp_negative)
            else:
                set_imagp(nr, word, imaginaryp_negative)

    return nr


def print_complex(nr):
    """
    Writes the complex number "nr" to the console.
    :param nr: Parameter that will be written
    :return:
    """
    if nr[1] == 0:
        print(str(get_realp(nr)))
    elif nr[0] == 0:
        print(str(get_imagp(nr)) + 'i')
    elif nr[1] > 0:
        print(str(get_realp(nr)) + " + " + str(get_imagp(nr)) + 'i')
    elif nr[1] < 0:
        print(str(get_realp(nr)) + " - " + str(-get_imagp(nr)) + 'i')


def print_menu():
    """
    Prints the user menu interface
    :return:
    """

    print("1. Read a list of complex numbers.")
    print("2. Display the entire list of complex numbers.")
    print("3. Display the longest sequence of consecutive pairs that are of equal sums. (property 9)")
    print("4. Display the longest sequence of numbers whose real parts are in the form of a mountain. (property 11)")
    print("5. Exit the application")


def print_list(list_complex):
    """
    Prints the entire list.
    :param list_complex: The list of complex numbers
    :return:
    """

    length = len(list_complex)

    for x in range(0, length):
        print(x + 1, end='')
        print(".) ", end='')
        print_complex(list_complex[x])


def read_list(list_complex):
    """
    Reads a list of complex numbers and adds them to the current list.
    :param list_complex: The current list
    :return:
    """

    correct_input = 0
    while correct_input == 0:
        try:
            nr = int(input("How many numbers would you like to add?\n"))
            correct_input = 1
        except ValueError:
            print(tgreen + "Please type a natural number\n", endc)

    for x in range(0, nr):
        complex_nr = create_complex()
        list_complex.append(complex_nr)


def start():
    """
    Control function
    :return:
    """

    list_complex = [[1, -2], [4, -2], [1, 8], [8, 9], [10, 2], [4, -1], [4, 4], [1, 3], [9, -2], [14, 24]]
    list_complex = [[1, +3], [2, -1], [3, +3], [4, -1], [10, 2], [4, -1], [3, 4], [2, 3], [1, -2], [0, 24]]

    # Command input
    while 1:
        correct_input = 0

        while correct_input == 0:
            print_menu()

            try:
                command = int(input("What would you like to do?\n"))
            except ValueError:
                print(tgreen + "\n\n\nPlease choose one of the available commands.\n", endc)
            else:
                if 1 <= command <= 4:
                    correct_input = 1
                elif command == 5:
                    exit(0)
                else:
                    print(tgreen + "\n\n\nPlease choose one of the available commands.\n", endc)
        ######################

        if command == 1:
            read_list(list_complex)
        if command == 2:
            print(tgreen + "\nThe list of complex numbers is:" + endc)
            print_list(list_complex)
        if command == 3:
            print_seq9(list_complex)
        if command == 4:
            print_seq11(list_complex)

        print("\n")


#UI - Sequences

def print_seq9(list_complex):
    rez = detseq9(list_complex)

    start = rez[0]
    end = rez[0] + rez[1]

    print(tgreen + "\nThe longest sequence of complex numbers that are of equal sums begins at "
          + str(start) + " and ends at " + str(end) + " (length = " + str(end - start + 1) + ")", endc)
    for x in range(start, end + 1):
        print_complex(list_complex[x])


def print_seq11(list_complex):
    rez = detseq11(list_complex)

    start = rez[0]
    end = rez[0] + rez[1] - 1

    print(tgreen + "\nThe longest sequence of complex numbers whose real parts are of the form of a mountain begins at "
          + str(start) + " and ends at " + str(end) + " (length = " + str(end - start + 1) + ")", endc)
    for x in range(start, end + 1):
        print_complex(list_complex[x])

#
#
#

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

def set_realp(nr, realp, negative):
    """
    Sets the real part of a complex number
    :param nr: the complex number
    :param realp: the real part that the complex number will receive
    :return:
    """
    if negative == 1:
        nr[0] = -int(realp)
    else:
        nr[0] = int(realp)


def set_imagp(nr, imagp, negative):
    """
    Sets the imaginary part of a complex number
    :param nr: the complex number
    :param imagp: the imaginary part that the complex number will receive
    :return:
    """
    if negative == 1:
        nr[1] = -int(imagp)
    else:
        nr[1] = int(imagp)


def get_realp(nr):
    """
    Gets the real part of a complex number
    :param nr: the complex number
    :return:
    """

    return nr[0]


def get_imagp(nr):
    """
    Gets the imaginary part of a complex number
    :param nr: the complex number
    :return:
    """

    return nr[1]


#
#
#


#
# Functions regarding the determination of certain sequences
#

def detseq9(list_complex):
    """
    Determines the beginning index and the length of
    the longest sequence that has property 9
    """
    length = len(list_complex)
    li_index_len = [0, 0]
    lseqmax = 0

    for index in range(0, length):
        l = lengthseq9(list_complex, index)

        if l > lseqmax:
            lseqmax = l
            li_index_len = [index, lseqmax]

    return li_index_len


def lengthseq9(list_complex, ind):
    """
    Determines the longest sequence of elements that have
    property 9, beginning from 'index'
    """
    length = len(list_complex)

    lseq = 0
    lseqmax = 0

    for x in range(ind, length - 1):
        if list_complex[x][0] + list_complex[x + 1][0] == list_complex[x][1] + list_complex[x + 1][1]:
            y = x + 1
            lseq = 2
            while y + 1 < length and list_complex[y][0] + list_complex[y + 1][0] == list_complex[y][1] + list_complex[y + 1][1]:
                lseq += 1
                y += 1

            if lseq > lseqmax:
                lseqmax = lseq

    return lseqmax


def detseq11(list_complex):
    """
    Determines the longest sequence of elements that
    have property 11.
    """
    length = len(list_complex)
    l_index_lsegmax = [0, 0]
    index = 0
    lseqmax = 0

    for x in range(1, length - 2):
        lseq = lengthmountain(list_complex, x)

        if lseq[1] > lseqmax:
            lseqmax = lseq[1]
            index = lseq[0]

    l_index_lseqmax = [index, lseqmax]

    return l_index_lseqmax


def lengthmountain(list_complex, index):
    """
    Determines the length and starting position of the longest
    "mountain" sequence that has peaks at "index"
    """

    length = len(list_complex)

    indr = index + 1
    indl = index - 1

    while indr < length and list_complex[indr - 1][0] > list_complex[indr][0]:
        indr += 1

    while indl >= 0 and list_complex[indl][0] < list_complex[indl + 1][0]:
        indl -= 1

    indl += 1
    indr -= 1

    l_index_length = [indl, indr - indl + 1]

    return l_index_length

#
#
#

if __name__ == "__main__":
    start()
