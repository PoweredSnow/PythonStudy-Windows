import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    render = csv.reader(f)
    header_row = next(render)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
