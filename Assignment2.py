import time
import random
from csv import writer


def main(max_size):
    random_int = random.randint(0,max_size)
    elements = makelist(max_size)
    return elements

def makelist(random_int):
    num_list = []
    for count in range(random_int):
        num_list.append(random.randint(1,100))
    return num_list

def append_to_csv(times_list, size_list):
    with open('assignment2.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(size_list)
        csv_writer.writerow(times_list)


def append_test(tries):
    x=34
    times_list = []
    max_size_list = []
    for i in range(tries):
        random_max_size = random.randint(100000,1000000)
        max_size_list.append(random_max_size)
        random_list = [main(random_max_size)]
        start_time = time.time()
        value = random_list.append(x)
        end_time = time.time()
        

        times_list.append(end_time - start_time)
    append_to_csv(times_list, max_size_list)
    return (times_list, max_size_list)


def pop_test(tries):
    times_list = []
    max_size_list = []
    for i in range(tries):
        random_max_size = random.randint(100000,1000000)
        max_size_list.append(random_max_size)
        random_list = [main(random_max_size)]
        start_time = time.time()
        value = random_list.pop()
        end_time = time.time()

        times_list.append(end_time - start_time)
    return (times_list, max_size_list)


def pop_i_test(tries):
    times_list = []
    max_size_list = []
    for i in range(tries):
        random_max_size = random.randint(100000,1000000)
        max_size_list.append(random_max_size)
        random_list = [main(random_max_size)]
        start_time = time.time()
        value = random_list.pop(0)
        end_time = time.time()

        times_list.append(end_time - start_time)
    append_to_csv(times_list, max_size_list)
    return (times_list, max_size_list)

def create_list(start_range, end_range, list_size):
    random_list = []

    for i in range(list_size):
        random_list.append(random.randint(start_range, end_range))

    return random_list

num1 = 1000000
start = 10
end = 50

def sort_test(tries):
    times_list = []
    random_list = []
    value_list = []
    for i in range(tries):
        random_list = create_list(start, end, num1)
        value = len(random_list)
        value_list.append(value)
        start_time = time.time()
        random_list.sort()
        end_time = time.time()
        times_list.append(end_time-start_time)
    append_to_csv(times_list, value_list)
    return (times_list, value_list)

print(sort_test(10))


