import os.path
from os import path


def main():

    print("File exists:" + str(path.exists("sample.txt.txt")))
    print("File exists:" + str(path.exists("dir.sample.txt")))
    print("directory exists:" + str(path.exists("dir")))


if __name__ == "__main__":
    main()
