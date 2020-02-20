import time
import random
from csv import writer


def append_to_csv(times_list, size_list):
    with open('assignment2.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(size_list)
        csv_writer.writerow(times_list)


def dictionary_tests(type, max_size, tries):

    times_list = [] # list of times
    size_list = [] # list of sizes

    if type.lower() == 'copy':

        for i in range(tries):
            #  create an initial dictionary of random keys and size.
            initial_dictionary = {str(i): "value" for i in range(random.randint(0, max_size))}

            start_time = time.time() # time of start
            copied_dictionary = initial_dictionary.copy()
            end_time = time.time() # time of completion
            times_list.append(round(end_time - start_time, 6))
            size_list.append(len(initial_dictionary))

        append_to_csv(times_list, size_list)
        return times_list, size_list


print(dictionary_tests('copy', 10, 10))