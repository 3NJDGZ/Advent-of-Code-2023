def main():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.split('\n')
            line = line[0]
            line = line.split(':')[1]
            line = line.split('|')

            winning_numbers = line[0]
            winning_numbers = winning_numbers.split(' ')
            wn_filtered = [item for item in winning_numbers if item != '']

            your_numbers = line[1]
            your_numbers = your_numbers.split(' ')
            yn_filtered = [item for item in your_numbers if item != '']

            matching_elements = list(set(wn_filtered).intersection(yn_filtered))

            point_exponentiation = len(matching_elements)-1
            if point_exponentiation < 0:
                number_to_be_added = 0
            else:
                number_to_be_added = 2**point_exponentiation
            total += number_to_be_added

    print(total)


if __name__ == "__main__":
    main()