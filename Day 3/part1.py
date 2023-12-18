numbers = '1234567890'
symbol_array = []

def find_adjacent(grid, symbol_array, numbers):
    seen_already = []
    total = 0
    for y_pos, row in enumerate(grid):
        for x_pos, char in enumerate(row):
            adjacent_number = ''
            if char in symbol_array:

                # Check Up
                if y_pos - 1 >= 0:
                    if grid[y_pos-1][x_pos] in numbers:

                        adjacent_number += grid[y_pos-1][x_pos] 

                        right = scan_right(grid, numbers, x_pos, y_pos-1)
                        left = scan_left(grid, numbers, x_pos, y_pos-1)

                        adjacent_number = adjacent_number + right[0]
                        adjacent_number = left[0] + adjacent_number
                        
                        for pos in right[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)
                        
                        for pos in left[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)
                        
                        if ((x_pos, y_pos-1)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos, y_pos-1)) 
                        
                        adjacent_number = ''

                # Check Down
                if y_pos + 1 <= len(grid) - 1:
                    if grid[y_pos+1][x_pos] in numbers:

                        adjacent_number += grid[y_pos+1][x_pos]

                        left = scan_left(grid, numbers, x_pos, y_pos+1)
                        right = scan_right(grid, numbers, x_pos, y_pos+1)

                        adjacent_number = adjacent_number + right[0]
                        adjacent_number = left[0] + adjacent_number

                        for pos in left[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        for pos in right[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos, y_pos+1)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos, y_pos+1))
                        
                        adjacent_number = ''

                # Check left
                if x_pos - 1 >= 0:
                    if grid[y_pos][x_pos-1] in numbers:

                        adjacent_number += grid[y_pos][x_pos-1]

                        left = scan_left(grid, numbers, x_pos-1, y_pos)

                        adjacent_number = left[0] + adjacent_number

                        for pos in left[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos-1, y_pos)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos-1, y_pos))
                        
                        adjacent_number = ''

                # Check right
                if x_pos + 1 <= len(row)-1:
                    if grid[y_pos][x_pos+1] in numbers:

                        adjacent_number += grid[y_pos][x_pos+1]

                        right = scan_right(grid, numbers, x_pos+1, y_pos)

                        adjacent_number = adjacent_number + right[0]

                        for pos in right[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos+1, y_pos)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos+1, y_pos))

                        adjacent_number = ''

                # Check Upper left
                if x_pos - 1 >= 0 and y_pos - 1 >= 0:
                    if grid[y_pos - 1][x_pos - 1] in numbers:

                        adjacent_number += grid[y_pos - 1][x_pos - 1]

                        left = scan_left(grid, numbers, x_pos-1, y_pos-1)

                        adjacent_number = left[0] + adjacent_number

                        for pos in left[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos-1, y_pos-1)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos-1, y_pos-1))
         
                        adjacent_number = ''

                # Check Upper right
                if x_pos + 1 <= len(row)-1 and y_pos - 1 >= 0:
                    if grid[y_pos - 1][x_pos + 1] in numbers:

                        adjacent_number += grid[y_pos - 1][x_pos + 1]

                        right = scan_right(grid, numbers, x_pos+1, y_pos-1)

                        adjacent_number = adjacent_number + right[0]

                        for pos in right[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos+1, y_pos-1)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos+1, y_pos-1))
     
                        adjacent_number = ''

                # Check Down left
                if x_pos - 1 >= 0 and y_pos + 1 <= len(grid) - 1:
                    if grid[y_pos + 1][x_pos - 1] in numbers:

                        adjacent_number += grid[y_pos + 1][x_pos - 1]

                        left = scan_left(grid, numbers, x_pos-1, y_pos+1)
          
                        adjacent_number = left[0] + adjacent_number
                   
                        for pos in left[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos-1, y_pos+1)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos-1, y_pos+1))
                   
                        adjacent_number = ''

                # Check Down right
                if x_pos + 1 <= len(row)-1 and y_pos + 1 <= len(grid) - 1:
                    if grid[y_pos + 1][x_pos + 1] in numbers:

                        adjacent_number += grid[y_pos + 1][x_pos + 1]

                        right = scan_right(grid, numbers, x_pos+1, y_pos+1)

                        adjacent_number = adjacent_number + right[0]

                        for pos in right[1]:
                            if pos not in seen_already:
                                seen_already.append(pos)

                        if ((x_pos+1, y_pos+1)) not in seen_already:
                            total += int(adjacent_number)
                            seen_already.append((x_pos+1, y_pos+1))
                           
                        adjacent_number = ''

    print(f"Total: {total}")

def scan_left(grid, numbers, initial_x, initial_y):
    digits = ''
    positions_seen = []
    for x in range(1, 3):
        if grid[initial_y][initial_x-x] in numbers:
            digits = grid[initial_y][initial_x-x] + digits
            positions_seen.append((initial_x-x, initial_y))
        elif grid[initial_y][initial_x-x] not in numbers:
            break

    return [digits, positions_seen]

def scan_right(grid, numbers, initial_x, initial_y):
    digits = ''
    positions_seen = []
    for x in range(1, 3):
        if grid[initial_y][initial_x+x] in numbers:
            digits = digits + grid[initial_y][initial_x+x]
            positions_seen.append((initial_x+x, initial_y))
        elif grid[initial_y][initial_x+x] not in numbers:
            break

    return [digits, positions_seen]

def main():
    # Setup grid 2D array
    grid = []
    with open('input.txt', 'r') as f:

        for line in f:
            row = []

            for char in line:
                row.append(char)

            if '\n' in row:
                row.pop(len(line)-1)

            grid.append(row)
    
    for row in grid:
        print(row)

    # Get the symbols in the txt file
    for row in grid:
        for char in row:
            if char not in numbers and char != '.':
                if char not in symbol_array:
                    symbol_array.append(char)
    
    find_adjacent(grid, symbol_array, numbers)
    
if __name__ == "__main__":
    main()