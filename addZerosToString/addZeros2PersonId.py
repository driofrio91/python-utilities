
import argparse


def add_leading_zeros(input_file, output_file):
    with open(input_file, "r") as file:
        numbers = file.readlines();
    with open(output_file, "w") as file:
        for number in numbers:
            number = number.strip()
            number_with_zeros = number.zfill(10)
            file.write(number_with_zeros + "\n")
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add zeros to left")
    parser.add_argument("input_file", type=str, help="Input file")
    parser.add_argument("output_file", type=str, help="Output file")

    args = parser.parse_args()

    add_leading_zeros(args.input_file, args.output_file);

    print(f"\nThe numbres the {args.input_file} has process and save in {args.output_file}\n")
