import sys

def get_filename(my_args):
    if len(my_args) >= 2:
        file_name = my_args[1]
        return file_name
    else:
        print("You should run this program by calling: python parser.py your_name")
        return ""


def read_from_file_to_list(file_name):
    output = []

    with open(file_name, "r") as file_to_read:
        for line in file_to_read.readlines():
            row = line.replace("\n", "").split(" ")
            output.append(row)
    return output


def main():

    file_name = get_filename(sys.argv)

    if len(file_name) == 0:
        return

    print(f"File to parse: {file_name}")
    data_list = read_from_file_to_list(file_name)
    print(data_list)


if __name__ == "__main__":
    main()