import csv
import datetime

valid_names = []

def main():
    file_path = "./test.csv"

    file = open_file(file_path)
    reader = get_reader(file)
    headers = next(reader)

    limit_dates = [
        get_date_from_string("01/07/2024"),
        get_date_from_string("31/07/2024")
    ]

    get_valid_names(reader, limit_dates)

    show_valid_names()

def open_file(file_path):
    return open(file_path, mode="r", encoding="utf-8", newline="")

def get_reader(file):
    return csv.reader(file, delimiter=";")

def iterate(reader):
    for person in reader:
        print(person)

def get_date_from_string(date_str):
    return datetime.datetime.strptime(date_str, "%d/%m/%Y")

def get_valid_names(reader, limit_dates):
    for person in reader:
        if date_is_valid(person[3], person[4], limit_dates):
            valid_names.append(person)

def date_is_valid(init_date_str, end_date_str, limit_dates):
    init_date = get_date_from_string(init_date_str)
    end_date = get_date_from_string(end_date_str)

    return date_is_between([init_date, end_date], limit_dates)

def date_is_between(dates, limit_dates):
    return not (dates[1] < limit_dates[0] or dates[0] > limit_dates[1])
    # if dates[1] < limit_dates[0]:
    #     return False
    # elif dates[0] < limit_dates[0] and dates[1] >= limit_dates[0]:
    #     return True
    # elif dates[0] >= limit_dates[0] and dates[1] <= limit_dates[1]:
    #     return True
    # elif dates[0] <= limit_dates[1] and dates[1] >= limit_dates[1]:
    #     return True
    # else:
    #     return False


def show_valid_names():
    for person in valid_names:
        print(person)

main()
