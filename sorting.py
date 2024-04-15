import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r", newline ="\n") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        iteration = 0
        for row in reader:
            for key, value in row.items():
                if iteration == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iteration = iteration + 1
        return data

def selection_sort(data):               #nejhorsi scenar az n**2
    """vzestupne serazeni prvku"""
    data = read_data(file_name="numbers.csv")
    serazeny_list = []
    my_list = data["series_1"]
    a = len(my_list)
    for i in range(a):
        min_idx = i
        for num_idx in range(i + 1, a):
            if my_list[num_idx] < my_list[min_idx]:
                min_idx = num_idx
        my_list[i], my_list[min_idx] =\
            my_list[min_idx], my_list[i]
        serazeny_list = my_list
    return serazeny_list

def bubble_sort(data):      #funkcni
    """tvorba vzestupne serazeneho seznamu cisel"""
    data = read_data(file_name="numbers.csv")
    my_list_two = data["series_1"]
    n = len(my_list_two)
    for i in range(n - 1):
        for num_idx in range(n - i - 1):
            if my_list_two[num_idx] > my_list_two[num_idx + 1]:
                my_list_two[num_idx], my_list_two[num_idx + 1] =\
                    my_list_two[num_idx + 1], my_list_two[num_idx]
    return my_list_two




def main():
    pass



if __name__ == '__main__':
    data = read_data(file_name="numbers.csv")
    print(data)
    serazeny_list = selection_sort(data["series_1"])
    print(serazeny_list)
    my_list_two = bubble_sort(data["series_1"])
    print(my_list_two)
    main()
