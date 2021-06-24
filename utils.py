from datetime import datetime


def get_now_time():
    return datetime.now().strftime('%y/%m/%d | %H:%M:%S')


def split_array_in_half(array):
    middle_index = int(len(array) / 2)
    return array[:middle_index], array[middle_index:]
