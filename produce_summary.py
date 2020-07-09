

def get_item(lst):
    """ takes list and stores melon name, number, and $ amount"""

    item_lst = 0
    melon = lst[0]
    count = lst[1]
    amount = lst[2]

    return [melon, count, amount] # returns as >>> (melon, count, amount) <<is a tuple


def lines_into_list(line):
    """ takes file with lines and strips, and splits to return a list of item words """

    words = line.rstrip().split('|')
    return words

def print_info(item_list):
    """ prints delivery info from given list of items """

    melon = item_list[0]
    count = item_list[1]
    amount = item_list[2]

    print("Delivered {} {}s for total of ${}".format(melon, count, amount))



def day_1():
    print("Day 1") # prints "day 1" as a title
    the_file = open("um-deliveries-20140519.txt") # opens text file and stores into the_file as each line 
    for line in the_file: # for each line in the_file
        line = line.rstrip() # strip the white space from the end of each line
        words = line.split('|') # words is a list of strings of sections that are split by '|'

        melon = words[0] # the first string section of the list word is stored in melon
        count = words[0] # the first string section of the list word is stored in count
        amount = words[0] # the first string section of the list word is stored in amount

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount)) 
    the_file.close() # close opened file
    # since melon, count, and amount are all the same index element of words, therefore we are only printing that one item repeatedly in the print statement.

def day_2():
    print("Day 2")
    the_file = open("um-deliveries-20140520.txt")
    for line in the_file:
        words_list = lines_into_list(line)
        items = get_item(words_list)
        print_info()
    the_file.close()

def day_3():
    print("Day 3")
    the_file = open("um-deliveries-20140521.txt")
    for line in the_file:
        words_list = lines_into_list(line)
        items = get_items(words_list)
        print_info()
    the_file.close()
    
