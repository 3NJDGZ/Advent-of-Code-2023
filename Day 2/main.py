file = 'Day 2/input.txt'

def part_one():
    r, g, b = 12, 13, 14
    total_id_sum = 0
    with open(file, 'r') as f:
        id = 0
        for line in f:
            
            above_r = False
            above_g = False
            above_b = False

            id += 1
            line = line.split(':')
            games = line[1].split(';')
            processed_data = []
            processed_data.append(id)
            for game in games:
                processed_data.append(game)
            for x in range(1, len(processed_data)):
                single_game = processed_data[x].split(',')
                for round in enumerate(single_game):
                    if '\n' in round[1]:
                        processed = round[1].replace('\n', '')
                        single_game[round[0]] = processed
                for round in single_game:
                    round = round.split(' ')
                    round.remove('')
                    if round[1] == 'red':
                        if int(round[0]) > r:
                            above_r = True
                    if round[1] == 'green':
                        if int(round[0]) > g:
                            above_g = True
                    if round[1] == 'blue':
                        if int(round[0]) > b:
                            above_b = True
            
            if not above_r and not above_g and not above_b:
                total_id_sum += int(processed_data[0])
    return total_id_sum

print(f'Part One Answer: {part_one()}')

def part_two():
    total = 0
    with open(file, 'r') as f:
        id = 0
        for line in f:

            h_r = 0 
            h_g = 0
            h_b = 0
            temp_r = []
            temp_g = []
            temp_b = []

            id += 1
            line = line.split(':')
            games = line[1].split(';')
            processed_data = []
            processed_data.append(id)
            for game in games:
                processed_data.append(game)
            for x in range(1, len(processed_data)):
                single_game = processed_data[x].split(',')
                for round in enumerate(single_game):
                    if '\n' in round[1]:
                        processed = round[1].replace('\n', '')
                        single_game[round[0]] = processed
                for round in single_game:
                    round = round.split(' ')
                    round.remove('')
                    if round[1] == 'red':
                        temp_r.append(int(round[0]))
                    if round[1] == 'green':
                        temp_g.append(int(round[0]))
                    if round[1] == 'blue':
                        temp_b.append(int(round[0]))
            number = max(temp_r) * max(temp_g) * max(temp_b)
            total += number
        return total


print(f'Part Two Answer: {part_two()}')
