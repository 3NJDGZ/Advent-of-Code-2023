def main():
    total = 0
    with open('input.txt', 'r') as f:
        copies = []
        for line in f:
            line = line.split('\n')
            line = line[0]
            line = line.split(':')

            card_number = line[0]
            card_number = card_number.split(' ')
            for item in card_number:
                if item.isnumeric():
                    card_number = item
                    break
            copies.append(int(card_number))

            card = line[1]
            card = card.split('|')

            winning_card = card[0]
            winning_card = winning_card.split(' ')
            winning_filtered = [item for item in winning_card if item != '']

            your_cards = card[1]
            your_cards = your_cards.split(' ')
            your_filtered = [item for item in your_cards if item != '']

            matching_elements = list(set(winning_filtered).intersection(your_filtered))

            copies += [number+int(card_number) for number in range(1, len(matching_elements)+1)]
            

            # Check for copies
            if len(copies) > 0:
                if int(card_number) in copies:
                    no_of_appearances = copies.count(int(card_number))
                    for loop in range(no_of_appearances-1):
                        matching_elements = list(set(winning_filtered).intersection(your_filtered))
                        copies += [number+int(card_number) for number in range(1, len(matching_elements)+1)]

            copies.sort()
            print(f"Winning Numbers: {winning_filtered}, \nYour Numbers: {your_filtered}, \nCard Number: {card_number}, \nMatching Elements: {len(matching_elements)}\n")
        
    print(len(copies))

if __name__ == "__main__":
    main()