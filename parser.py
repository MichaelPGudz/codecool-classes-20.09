import sys

def get_filename():
    if len(sys.argv) >= 2:
        # print(sys.argv)
        file_name = sys.argv[1]
        return file_name
    else:
        print("You should run this program by calling: python parser.py your_name")
        return ""

def main():
    file_name = get_filename()

    if len(file_name) == 0:
        return

    print(f"File to parse: {file_name}")


if __name__ == "__main__":
    main()
