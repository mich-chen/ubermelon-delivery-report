"""
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

    """


def lines_into_list(line):
    """ takes file with lines and strips, and splits to return a list of item words """

    words = line.rstrip().split('|')
    return words


def print_info(item_list):
    """ prints delivery info from given list of items """

    melon, count, amount = item_list
    print("Delivered {} {}s for total of ${}".format(melon, count, amount))


def day_summary(day, report):
    print(f'Day {day}')
    the_file = open(report)
    for line in the_file:
        words_list = lines_into_list(line)
        print_info(words_list)
    the_file.close()

day_summary(1, "um-deliveries-20140519.txt")
day_summary(2, "um-deliveries-20140520.txt")
day_summary(3, "um-deliveries-20140521.txt")
