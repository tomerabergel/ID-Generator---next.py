# A program that generates ID numbers (next.py final exercise)

# 1) One Liners boolean function to check the validity of the ID number:
def check_id_valid(id_number):
    """Checking the correctness of an ID number.
    Description of ID validity process:
    * Step One: Multiply each digit in the ID card by 1 or 2 depending on its position in the number - a digit that is in an odd position will be multiplied by 1 and a digit that is in an even position will be multiplied by 2.
    * Step Two: Go over any number obtained as a result of the multiplication operation and we will check if it is greater than 9. If so, we will connect his two digits. Otherwise, we'll leave it as it is.
    * Step Third: Sum of all the numbers obtained in the result.
    * Step Fourth: Check whether the number obtained as a result of the third step is divisible by 10 with no remainder. If so, the ID number is correct, otherwise - incorrect.
    :param id_number: ID number value
    :type id_number: int
    :return: returns True if it is correct, otherwise it returns False.
    :rtype: boolean
    """
    return (len(str(id_number)) == 9) and (sum(map(lambda digit_num: sum(int(sub_digit) for sub_digit in str(digit_num)), [2 * int(digit) if index % 2 else int(digit) * 1 for index, digit in enumerate(str(id_number))])) % 10 == 0)


# 2) A class that represents an iterator called IDIterator:
class IDIterator:
    """
    A class used to represent an ID Iterator
    """
    def __init__(self, id1):
        self._id = int(id1)

    def __iter__(self):
        return self

    def __next__(self):
        if 100000000 > self._id > 999999999:
            raise StopIteration()
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
        return self._id


# 3) Production of 10 new IDs using iterator:
def id_using_iterator(id_number):
    """Produces 10 new IDs using an iterator (from the class we created).
    :param id_number: ID number value
    :type id_number: int
    :return: Prints the following 10 correct ID numbers on the screen
    :rtype: None
    """
    id_iterator = iter(IDIterator(id_number))
    count = -1
    for id_num in id_iterator:
        count += 1
        if count == 10:
            break
        else:
            print(id_num)


# 4) A generator function
def id_generator(idd):
    """A generator function that generates the next valid ID number in the range whenever asked to generate a value.
    :param idd: ID number value
    :type idd: int
    :return: Prints the following 10 correct ID numbers on the screen
    :rtype: Iterator[int]
    """
    for num in range(int(idd)+1, 1000000000):
        if check_id_valid(num):
            yield num


# 5) Generation 10 new IDs using generator:
def id_using_generator(id_number):
    """ A function that creates a generator using the generator function we created and produces 10 new IDs.
    :param id_number: ID number value
    :type id_number: int
    :return: Prints the following 10 correct ID numbers on the screen
    :rtype: Generator[int]
    """
    idNumber = id_generator(id_number)
    for n in range(10):
        print(next(idNumber))


# ##################################################### main ###########################################################
# 6) The main program:
def main():
    id_number = input("Enter ID: ")
    try:                              # Input integrity check
        int(id_number)
        if len(str(id_number)) != 9:
            raise ValueError
    except ValueError:
        print("ID number should be a nine-digit number")
        while len(str(id_number)) != 9 or not id_number.isdigit() or int(id_number) < 100000000:
            id_number = input("Enter ID: ")
    gen_or_it = input("Generator or Iterator? (gen/it)? ")
    while gen_or_it != "it" and gen_or_it != "gen":              # Input integrity check
        gen_or_it = input("Generator or Iterator? (gen/it)? ")
    if gen_or_it == "it":
        id_using_iterator(int(id_number))   # generate of ID numbers using a Iterator
    elif gen_or_it == "gen":
        id_using_generator(int(id_number))  # generate of ID numbers using a Generator


if __name__ == '__main__':
    main()

