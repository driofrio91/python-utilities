import sys

def read_file_lines(filename):
    with open(filename, 'r') as file:
        return set(line.strip() for line in file)

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py file1.txt file2.txt output.txt")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = sys.argv[3]

    strings1 = read_file_lines(file1)
    strings2 = read_file_lines(file2)

    difference = strings1 - strings2

    with open(output, 'w') as out_file:
        for string in sorted(difference):
            out_file.write(string + '\n')

    print(f"{len(difference)} strings have been written to {output}")

if __name__ == "__main__":
    main()
