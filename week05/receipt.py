import csv

def read_dictionary(filename, key_column_index):
    product = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for read in reader:
            key = read[key_column_index]
            product[key] = read
    return product
def main():
    products_dict = read_dictionary("products.csv", 0)
    print(products_dict)
    print()

if __name__ == "__main__":
    main()