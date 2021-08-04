import csv


def read_csv_file(file_name, csv_to_read):
    with open(file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row)
        return csv_list
    
def save_csv_file(file_name, list_name):
    with open (file_name, 'w') as csv.file:
        writer = csv.wrriter(csv_file, delimiter)
