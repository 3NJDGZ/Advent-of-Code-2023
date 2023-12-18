total = 0
word_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
word_numbers_mapping = [['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'], ['8', 'eight'], ['9', 'nine']]

def find_first_digit_of_word(word: str):
    first_digit = ''
    for x in range(len(word)):
        for y in range(5):
            sub_word = word[x:x+y+1]
            if sub_word in word_numbers:
                for element in word_numbers_mapping:
                    if element[1] == sub_word:
                        first_digit = element[0]
                break
            elif sub_word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                first_digit = sub_word
                break
        if first_digit != '':
            break

    return str(first_digit)

def find_last_digit_of_word(word: str):
    last_digit = ''
    length = len(word)
    for x in range(len(word)):
        for y in range(6):
            sub_word = word[length-y:length]
            if sub_word in word_numbers:
                for element in word_numbers_mapping:
                    if element[1] == sub_word:
                        last_digit = element[0]
                break
            elif sub_word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                last_digit = sub_word
                break
        length -= 1
        if last_digit != '':
            break

    return str(last_digit)


with open('input.txt', 'r') as file:

    for word in file:
        number = find_first_digit_of_word(word) + find_last_digit_of_word(word)
        print(f'{word} {number}')
        total += int(number)

print(total)
