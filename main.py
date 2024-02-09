import math
import numpy as np

domain = []
cage_domains = []

for i in range(81) :
    domain = []
    for j in range(1, 10) :
        domain.append(j)
    cage_domains.append(domain)

square = []
square_row = []

for i in range(0, 3) :
    square_row = []
    for j in range(3) :
        square_row.append(i * 3 + j + 1)
    square.append(square_row)
    
##### forward pruning function
def turn_index_to_number(index, length):
    result = 0
    i = index[0]
    j = index[1]
    result += (i * length) + j
    return result
    
def turn_number_to_index(number, length) :
    i = math.floor(number / length)
    j = number - (i * length)
    return i , j


def backward_pruning(number, index, cage_domains) :
    #add number from row:
    j = index[1]
    for i in range(9) :
        back_prune_index(number, (i, j), cage_domains)
    #add number to column:
    i = index[0]
    j = 0
    for j in range(9) :
        back_prune_index(number, (i, j), cage_domains)
    #add number from 3*3 square
    square_i = math.floor(index[0] / 3) * 3
    square_j = math.floor(index[1] / 3) * 3
    for f in range(square_i, square_i + 3) :
        for t in range(square_j, square_j + 3) :
            back_prune_index(number, (f, t), cage_domains)
    return cage_domains

def forward_pruning(number, index, cage_domains):
    #delete number from row:
    j = index[1]
    for i in range(9) :
        prune_index(number, (i, j), cage_domains)
    #delete number from column:
    i = index[0]
    j = 0
    for j in range(9) :
        prune_index(number, (i, j), cage_domains)
    #delete number from 3*3 square
    square_i = math.floor(index[0] / 3) * 3
    square_j = math.floor(index[1] / 3) * 3
    for f in range(square_i, square_i + 3) :
        for t in range(square_j, square_j + 3) :
            prune_index(number, (f, t), cage_domains)
    return cage_domains


def find_square(index, square) :
    square_i = math.floor(index[0] / 3)
    square_j = math.floor(index[1] / 3)
    new_index = square_i , square_j 
    return square_i , square_j
        
    
def prune_index(num, index, cage_domains):
    number = turn_index_to_number(index, 9)
    if num in cage_domains[number] :
        cage_domains[number].remove(num)
    return cage_domains

def back_prune_index(num, index, cage_domains) :
    number = turn_index_to_number(index, 9)
    if num not in cage_domains[number] :
        cage_domains[number].append(num)
    return cage_domains

def print_cage_domains_with_index(cage_domains) :
    cage_domain_counter = 0
    for cage_domain in cage_domains :
        indexOfCageDomains = turn_number_to_index(cage_domain_counter, 9)
        cage_domain_counter += 1
        index_to_stringList = [str(x) for x in indexOfCageDomains]
        indexList_to_string = ', '.join(index_to_stringList)
        string_list = [str(x) for x in cage_domain]
        cage_domain_to_string = ', '.join(string_list)
        print("[(" + indexList_to_string + ")[" + cage_domain_to_string + "]]", end= ' ')
        indexOfCageDomains = []


#####MRV function
def get_mrv_cell(grid):
    min_candidates = 10
    mrv_cell = None
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                candidates = get_candidates(grid, i, j)
                if len(candidates) < min_candidates:
                    min_candidates = len(candidates)
                    mrv_cell = (i, j)
    return mrv_cell

##### LCV function
def get_lcv_values(grid, row, col, candidates):
    values = []
    for candidate in candidates:
        count = 0
        for i in range(9):
            if grid[row][i] == 0 and candidate in get_candidates(grid, row, i):
                count += 1
            if grid[i][col] == 0 and candidate in get_candidates(grid, i, col):
                count += 1
            subgrid_row = 3 * (row // 3) + i // 3
            subgrid_col = 3 * (col // 3) + i % 3
            if grid[subgrid_row][subgrid_col] == 0 and candidate in get_candidates(grid, subgrid_row, subgrid_col):
                count += 1
        values.append((candidate, count))
    values.sort(key=lambda x: x[1])
    return [x[0] for x in values]


#### heuristic function
def get_next_cell(grid):
    return get_mrv_cell(grid)

def get_sorted_values(grid, row, col):
    candidates = get_candidates(grid, row, col)
    return get_lcv_values(grid, row, col, candidates)


def is_number_in_column(matrix, number, column_index):
    return any(row[column_index] == number for row in matrix)

def is_number_in_row(matrix, number, row_index):
    return number in matrix[row_index]

def is_in_square(matrix, number, i, j) :
    i_square = math.floor(i / 3) * 3
    j_square = math.floor(j / 3) * 3
    for r in range(i_square, i_square + 3) :
        for t in range(j_square, j_square + 3) :
            if matrix[r][t] == number :
                return True
    return False

def is_safe(number, constraint, array, i, j) :
    index = [i , j]
    if not is_number_in_column(array_9by9, number, j) :
        if not is_number_in_row(array_9by9, number, i):
            if not is_in_square(array_9by9, number, i, j) :
                if count_cages(constraint, array_9by9) + number == goal_count(constraint):
                    if not find_zeros(constraint, array_9by9, number, i, j) :
                        return True
            
                elif count_cages(constraint, array_9by9) + number < goal_count(constraint) :
                    if find_zeros(constraint, array_9by9, number, i, j) :
                        return True
                    else :
                        return False
    return False
   
def count_cages(readable_constraint, array) :
    counter = 0
    goalCount = readable_constraint.pop()
    for cage_number in readable_constraint :
        translation = translate_cage_number(cage_number)
        i = translation[0]
        j = translation[1]
        counter += array[i][j]
    readable_constraint.append(goalCount)
    return counter
        
def goal_count(readable_constraint) :
    return int(readable_constraint[-1])

def readable_constraint(constraint) :
    readable_constraint = []
    for part in constraint.split() :
        if part != '>' :
            readable_constraint.append(part)
    return readable_constraint

def find_constraint(cageNumber, readable_constraints) :
    for constraint in readable_constraints :
        goalCount = constraint.pop()
        for cage_number in constraint :
            if cage_number == cageNumber :
                constraint.append(goalCount)
                return constraint

def find_zeros(constraint, array, number, i, j) :
    array_9by9[i][j] = number
    goalCount = constraint.pop()
    for cageNumber in constraint :
        if (check_cage(cageNumber, array)) == 0 :
            array_9by9[i][j] = 0
            constraint.append(goalCount)
            return True
    constraint.append(goalCount)
    array_9by9[i][j] = 0
    return False

def check_cage(cage_number, array) :
    index = []
    index.append(int(cage_number[0]))
    index.append(int(cage_number[1]))
    i = index[0] - 1
    j = index[1] - 1
    return array[i][j]
     
def translate_cage_number(string) :
    index = []
    index.append(int(string[0]) - 1)
    index.append(int(string[1]) - 1)
    return index

def cage_number_only (readable_constraint) :
    readable_constraint2 = readable_constraint
    readable_constraint2.pop()
    return readable_constraint2
   
def cage_numbers_all_constraints (readable_constraints) :
    new_readable_constraints = []
    for readable_constraint in readable_constraints :
        readable_constraint.pop()
        new_readable_constraints.append(readable_constraint)
    return new_readable_constraints
            
def solve_sudoku(array_9by9):
    counter = 0
    for col in range(9):
        for row in range(9):
            string = ''
            string += str(row + 1)
            string += str(col + 1)
            readable_constraints = []
            for constraint in constraints :
                readable_constraints.append(readable_constraint(constraint))
            constraint = find_constraint(string, readable_constraints)
            counter += 1
            if array_9by9[row][col] == 0:
                # Try to fill the cell with a valid number
                for number in sorted(cage_domains[turn_index_to_number([row, col], 9)]):
                    if is_safe(number, constraint, array_9by9, row, col) :
                        array_9by9[row][col] = number
                        forward_pruning(number, [row, col], cage_domains)
                        for r in array_9by9 :
                            for elem in r :
                                print(elem, end=' ')
                            print()
                        print("/////")
                        # Recursively solve the rest of the puzzle
                        
                        if solve_sudoku(array_9by9):
                            # print("solve sudoku is true")
                            return True
                        # Backtrack
                        array_9by9[row][col] = 0
                        backward_pruning(number, [row, col], cage_domains)
                        if array_9by9[row][col] == 0 :
                            print("back tracked!")
                return False
    return True

# cage_domains[turn_index_to_number([row, col], 9)] = sorted(cage_domains[turn_index_to_number([row, col], 9)])
## array example 1
# array_9by9 = [[6, 0, 9, 0, 0, 7, 0, 3, 0],
# [0, 0, 0, 0, 9, 0, 0, 0, 6],
# [0, 2, 0, 0, 0, 3, 9, 4, 0],
# [0, 0, 0, 0, 8, 2, 7, 0, 0],
# [2, 0, 8, 0, 7, 0, 0, 0, 3],
# [0, 0, 0, 9, 1, 6, 0, 8, 0],
# [0, 0, 2, 0, 0, 0, 0, 1, 4],
# [3, 0, 4, 6, 5, 0, 8, 0, 0],
# [1, 0, 5, 0, 0, 9, 0, 0, 0]]


## cage number example1:
# 11 21 22 > 14
# 12 > 4
# 13 23 > 10
# 14 15 25 > 16 
# 16 > 7
# 26 27 > 6 
# 17 18 > 4
# 19 29 > 14 
# 28 38 39 > 16
# 35 36 37 46 > 20 
# 24 34 > 9
# 32 33 42 > 18
# 31 41 51 > 14
# 43 > 6
# 44 45 > 11
# 47 48 49 > 13
# 61 > 7
# 52 62 72 > 12
# 53 63 73 > 13
# 54 64 65 66 75 > 23  
# 57 > 6
# 58 59 > 12
# 55 56 > 12
# 68 69 > 10
# 67 76 77 78 88 > 20
# 79 89 > 13 
# 71 81 82 83 > 23 
# 74 84 > 13
# 91 92 93 > 14
# 94 > 2
# 85 95 > 9
# 86 87 96 > 18
# 97 98 99 > 16


# ## array example 2
# array_9by9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# 22
# 11 21 > 10
# 12 22 > 4
# 13 14 15 16 > 30
# 17 18 19 27 28 29 38 39 > 36
# 23 24 33 34 43 > 25
# 25 26 > 7
# 31 32 41 42 > 22
# 35 45 44 55 56 57 66 > 38
# 36 37 46 47 > 19
# 48 58 > 8
# 49 59 69 79 > 19
# 51 61 > 8
# 52 53 62 63 > 23
# 54 64 65 > 13
# 67 68 78 77 76 > 29
# 71 81 82 91 92 93 > 35
# 72 73 83 > 10
# 74 75 84 85 > 24
# 86 87 96 97 > 22
# 88 89 > 10
# 94 95 > 3
# 98 99 > 10



#cage_numbers3
#27
# 11 21 > 13
# 12 13 22 > 9
# 14 15 16 > 16
# 17 18 28 > 16
# 19 29 > 11
# 23 24 32 33 34 > 24
# 25 35 > 12
# 26 27 36 37 38 > 23
# 31 41 > 9
# 39 49 > 10
# 42 52 51 > 11
# 43 44 45 46 47 > 25
# 48 58 59 > 15
# 53 54 55 56 57 64 65 66 > 44
# 61 71 81 91 > 20
# 62 63 > 9
# 67 68 > 10
# 69 79 89 99 > 16
# 72 82 > 11
# 73 74 > 9
# 75 85 95 > 15
# 76 77 > 11
# 78 88 > 10
# 83 93 92 > 15
# 84 94 > 3
# 86 96 > 14
# 87 97 98 > 24


# 8 5 9 0 0 2 4 0 0
# 7 2 0 0 0 0 0 0 9
# 0 0 4 0 0 0 0 0 0
# 0 0 0 1 0 7 0 0 2
# 3 0 5 0 0 0 9 0 0
# 0 4 0 0 0 0 0 0 0
# 0 0 0 0 8 0 0 7 0
# 0 1 7 0 0 0 0 0 0
# 0 0 0 0 3 6 0 4 0
# 45
# 11 12 13 14 15 > 30
# 16 17 18 19 > 25
# 21 22 23 24 > 20
# 25 26 27 28 29 > 30
# 31 32 33 34 > 20
# 35 36 37 38 39 > 30
# 41 42 43 44 > 25
# 45 46 47 48 > 20
# 51 52 53 54 > 20
# 55 56 57 58 59 > 30
# 61 62 63 64 > 25
# 65 66 67 68 69 > 30
# 71 72 73 74 > 20
# 75 76 77 78 79 > 30
# 81 82 83 84 > 25
# 85 86 87 88 89 > 30
# 91 92 93 94 95 > 30
# 96 97 98 99 > 25

# array_9by9 = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
#  [0, 3, 0, 0, 2, 0, 0, 0, 8],
#  [0, 0, 9, 6, 0, 0, 5, 0, 0],
#  [0, 0, 5, 3, 0, 0, 9, 0, 0],
#  [0, 1, 0, 0, 8, 0, 0, 0, 2],
#  [6, 0, 0, 0, 0, 4, 0, 0, 0],
#  [3, 0, 0, 0, 0, 0, 0, 1, 0],
#  [0, 4, 0, 0, 0, 0, 0, 0, 7],
#  [0, 0, 7, 0, 0, 0, 3, 0, 0]]

# 11 12 13 14 15 > 30
# 16 17 18 19 > 25
# 21 22 23 24 > 20
# 25 26 27 28 29 > 30
# 31 32 33 34 > 20
# 35 36 37 38 39 > 30
# 41 42 43 44 > 25
# 45 46 47 48 > 20
# 51 52 53 54 > 20
# 55 56 57 58 59 > 30
# 61 62 63 64 > 25
# 65 66 67 68 69 > 30
# 71 72 73 74 > 20
# 75 76 77 78 79 > 30
# 81 82 83 84 > 25
# 85 86 87 88 89 > 30
# 91 92 93 94 95 > 30
# 96 97 98 99 > 25

# 0 0 0 0 0 0 0 0 0
# 0 4 0 0 0 0 7 0 2
# 0 2 8 5 4 0 3 1 0
# 0 0 2 0 0 0 0 4 0
# 0 0 0 0 0 0 0 0 1
# 6 0 0 1 0 0 2 0 0
# 0 8 1 0 6 3 0 2 0
# 2 0 9 0 0 5 0 0 0
# 0 0 0 0 2 8 0 6 0
# 34
# 11 12 13 > 9
# 14 > 6
# 15 16 > 9
# 17 18 19 > 21
# 21 22 23 > 19
# 24 34 > 13
# 25 26 > 4
# 27 28 29 38 48 > 19
# 31 41 > 15
# 32 42 33 > 11
# 35 36 > 13
# 37 47 57 > 14
# 39 > 6
# 43 44 > 5
# 45 55 > 17
# 46 56 > 10
# 49 59 > 8
# 51 61 71 > 14
# 52 62 > 14
# 53 54 > 9
# 58 68 78 > 14
# 63 64 > 5
# 65 > 5
# 66 67 77 > 18
# 69 79 > 12
# 72 82 81 > 16
# 73 74 > 8
# 75 85 > 7
# 76 86 87 > 16
# 83 93 92 > 19
# 84 94 > 13
# 88 89 99 > 15
# 91 > 4
# 95 96 97 98 > 17


# 0 0 0 0 0 7 0 0 0
# 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 2 0 0
# 0 2 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 2
# 0 0 3 0 5 0 0 0 0
# 6 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 6
# 0 0 0 0 6 0 0 0 0
# 34
# 11 21 > 8
# 12 > 6
# 13 23 33 > 17
# 14 15 16 > 13
# 17 > 9
# 18 19 28 27 > 17
# 22 > 4
# 24 25 26 > 15
# 29 39 49 59 > 19
# 31 41 > 10
# 32 42 43 > 17
# 34 44 > 14
# 35 36 46 > 12
# 37 38 > 6
# 45 > 7
# 47 57 67 > 18
# 48 > 5
# 51 52 > 13
# 53 63 62 61 71 > 21
# 54 55 > 7
# 56 66 76 77 > 21
# 58 68 > 7
# 64 74 > 3
# 65 75 > 8
# 69 79 89 > 22
# 72 73 83 > 17
# 78 88 87 > 12
# 81 91 > 9
# 82 > 3
# 84 > 5
# 85 95 > 15
# 86 96 > 12
# 92 93 94 > 17
# 97 98 99 > 16



# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 4 0 0
# 0 0 0 0 0 0 9 0 0
# 0 7 0 0 0 0 0 0 0
# 0 0 0 0 6 0 0 5 0
# 0 0 0 0 0 0 0 0 4
# 0 0 6 2 0 0 0 0 0
# 0 0 9 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0
# 34
# 11 > 2
# 12 13 23 > 9
# 14 > 4
# 15 25 24 > 12
# 16 > 7
# 17 18 28 > 16
# 19 29 > 13
# 21 22 31 > 21
# 26 36 46 > 13
# 27 37 38 > 14
# 32 42 41 > 14
# 33 34 > 12
# 35 45 44 > 16
# 39 49 > 11
# 43 53 > 11
# 47 48 > 8
# 51 > 9
# 52 > 4
# 54 64 74 75 > 21
# 55 56 66 65 > 18
# 57 67 77 87 > 13
# 58 59 69 > 17
# 61 62 72 > 19
# 63 73 > 8
# 68 78 > 16
# 71 81 82 83 > 18
# 76 86 85 > 20
# 79 89 > 4
# 84 94 > 15
# 88 98 > 10
# 91 > 7
# 92 93 > 6
# 95 96 97 > 12
# 99 > 5

array_9by9 = []
while len(array_9by9) < 9:
    row = input().strip().split()
    if len(row) != 9:
        print("Invalid input. Please enter 9 numbers for each row.")
        continue
    try:
        row = [int(num) for num in row]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        continue
    array_9by9.append(row)

        
cages = int(input())
constraints = []
for i in range(cages) :
    constraints.append(input())
    
print("The 9x9 array is:")
for row in array_9by9:
    print(row)
    

for i in range(9) :
    for j in range(9) :
        forward_pruning(array_9by9[i][j], [i, j], cage_domains)
        
solve = solve_sudoku(array_9by9)