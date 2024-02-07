import math
import numpy as np

domain = []
cage_domains = []

for i in range(81) :
    domain = []
    for j in range(10) :
        domain.append(j)
    cage_domains.append(domain)

# cage_domains[31] = [x for x in cage_domains[31] if x != 3]
# print(cage_domains)
# cage_domains[31]=np.delete(cage_domains[31], [1], axis=0)
# print
# domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# cage_domains = []
# for i in range(81):
#     if i == 30:
#         cage_domains.append(domain + [10])
#     else:
#         cage_domains.append(domain)
# big_array = np.array([np.array(list(range(1, 10))) for _ in range(81)])

# # Add 10 to the 31st array inside the big array
# big_array[30] = np.append(big_array[30], [10])
# print(big_array)
# cage_domains[0] = [x for x in cage_domains[30] if x != 3]

# print(cage_domains)


# big_array = [[list(range(1, 10)) for _ in range(9)] for _ in range(9)]

# # Remove the number 3 from the 31st array inside the big array
# big_array[30][2].remove(3)

# print(big_array)

square = []
square_row = []

for i in range(0, 3) :
    square_row = []
    for j in range(3) :
        square_row.append(i * 3 + j + 1)
    square.append(square_row)
    

def turn_index_to_number(index, length):
    result = 0
    i = index[0]
    j = index[1]
    result += (i * length) + j
    return result
    
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
    # i = find_square[0]
    # j = find_square[1]
    square_i = math.floor(index[0]) * 3
    square_j = math.floor(index[1]) * 3
    for f in range(square_i, square_i + 3) :
        for t in range(square_j, square_j + 3) :
            if number not in cage_domains[turn_index_to_number(index, 9)] :
                back_prune_index(number, (f, t), cage_domains)
    return cage_domains

def forward_pruning(number, index, cage_domains):
    # cage_domains = cage_domains
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
    # i = find_square[0]
    # j = find_square[1]
    square_i = math.floor(index[0]) * 3
    square_j = math.floor(index[1]) * 3
    for f in range(square_i, square_i + 3) :
        for t in range(square_j, square_j + 3) :
            try :
                prune_index(number, (f, t), cage_domains)
            except:
                pass
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
# print(back_prune_index(3, [1, 0], cage_domains))
# forward_pruning(6, (0, 0), cage_domains)
# # # for i in range(9) :
# # #     for
# print(cage_domains)
# print("//////")
# backward_pruning(6, (0, 0), cage_domains)
# print(cage_domains)

# array_9by9 = [[6, 0, 9, 0, 0, 7, 0, 3, 0],
# [0, 0, 0, 0, 9, 0, 0, 0, 6],
# [0, 2, 0, 0, 0, 3, 9, 4, 0],
# [0, 0, 0, 0, 8, 2, 7, 0, 0],
# [2, 0, 8, 0, 7, 0, 0, 0, 3],
# [0, 0, 0, 9, 1, 6, 0, 8, 0],
# [0, 0, 2, 0, 0, 0, 0, 1, 4],
# [3, 0, 4, 6, 5, 0, 8, 0, 0],
# [1, 0, 5, 0, 0, 9, 0, 0, 0]]



array_9by9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Input the elements of the array
# print("Enter the elements of the 9x9 array:")

# for i in range(9):
#     row = list(map(int, input().split()[:9]))
#     array_9x9.append(row)

# Print the 9x9 array
print("The 9x9 array is:")
for row in array_9by9:
    print(row)
    
    
cages = int(input())
constraints = []
for i in range(cages) :
    constraints.append(input())

    
print(constraints)

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

# print(is_number_in_row(array_9by9, 4, 2))
# print(is_number_in_column(array_9by9, 5, 0))

# print(is_number_in_row(array_9by9, 5))
def is_safe(number, constraint, array, i, j) :
    index = [i , j]
    # print("i in is_safe: ")
    # print(i)
    # print("j in is_safe: ")
    # print(j)
    if not is_number_in_column(array_9by9, number, j) :
        # print("not in column")
        if not is_number_in_row(array_9by9, number, i):
            if not is_in_square(array_9by9, number, i, j) :
                # print("not in row")
                print("constraint in is_safe: ")
                print(constraint)
                # print("about to call count_cages")
                # print("about to call goal_count")
                # array_9by9[i][j] = number
                # print("number in box: ")
                # print(array_9by9[i][j])
                if count_cages(constraint, array_9by9) + number == goal_count(constraint):
                    # print("about to call find_zeros")
                    if not find_zeros(constraint, array_9by9, number, i, j) :
                        # array_9by9[i][j] = 0
                        return True
            
                elif count_cages(constraint, array_9by9) + number < goal_count(constraint) :
                    # print("called count_cages")
                    # print("called goal_count")
                    # print("number in box in elif: ")
                    # # print(array_9by9[i][j])
                    # print("about to call find_zeros2")
                    if find_zeros(constraint, array_9by9, number, i, j) :
                        # array_9by9[i][j] = 0
                        return True
                    else :
                        # array_9by9[i][j] = 0
                        return False
    # array_9by9[i][j] = 0
    return False

    
def count_cages(readable_constraint, array) :
    counter = 0
    # size = len(readable_constraint)
    # readable_constraint.pop()
    # print("readable_contsraint in count_cages: ")
    # print(readable_constraint)
    # readable_constraint2 = readable_constraint
    # readable_constraint2 = cage_number_only(readable_constraint2)
    # print("readable_contsraint in count_cages: ")
    # print(readable_constraint)
    goalCount = readable_constraint.pop()
    # print("readable_contsraint in count_cages after pop: ")
    # print(readable_constraint)
    for cage_number in readable_constraint :
        # print("cage_number in count_cages: ")
        # print(cage_number)
        translation = translate_cage_number(cage_number)
        # print("translation in count_cages: ")
        # print(translation)
        i = translation[0]
        # print("i in count_cages: ")
        # print(i)
        j = translation[1]
        # print("j in count_cages: ")
        # print(j)
        # j = translate_cage_number(cage_number)
        counter += array[i][j]
    readable_constraint.append(goalCount)
    print("counter in count_cages: ")
    print(counter)
    return counter
        

def goal_count(readable_constraint) :
    # print("constraint in goal_count: ")
    print("goal count: ")
    print(int(readable_constraint[-1]))
    return int(readable_constraint[-1])

def readable_constraint(constraint) :
    # counter1 = 0
    # counter2 = 0
    readable_constraint = []
    for part in constraint.split() :
        # print("iteration through 1 constraint: ")
        # counter2 += 1
        # print("part :")
        # print(part)
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
            

# readable_constraints = []
# for constraint in constraints :
#     readable_constraints.append(readable_constraint(constraint))
# print(find_constraint("14", readable_constraints))


def find_zeros(constraint, array, number, i, j) :
    array_9by9[i][j] = number
    # print("constraint in find_zeros: ")
    # print(constraint)
    goalCount = constraint.pop()
    # print("check cage: ")
    # print(check_cage("12", array))
    # print(":check cage ")
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
    # print("cage number 0: ")
    # print(int(cage_number[0]))
    # print("cage number 1: ")
    # print(int(cage_number[1]))
    index.append(int(cage_number[0]))
    index.append(int(cage_number[1]))
    i = index[0] - 1
    j = index[1] - 1
    return array[i][j]
     

def translate_cage_number(string) :
    # print("string in translate_cage_number: " + string)
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
    # Find an empty cell
    counter = 0
    for col in range(9):
        for row in range(9):
            #find constraint
            string = ''
            string += str(row + 1)
            string += str(col + 1)
            # print("string: ")
            # print(string)
            readable_constraints = []
            for constraint in constraints :
                readable_constraints.append(readable_constraint(constraint))
            constraint = find_constraint(string, readable_constraints)
            # print("constraint: ")
            # print(constraint)
            counter += 1
            if array_9by9[row][col] == 0:
                # Try to fill the cell with a valid number
                for number in range(1, 10):
                    print("number: ")
                    print(number)
                    print("row and col: ")
                    print(row, col)
                    # print("about to call is_safe: ")
                    # array_9by9[row][col] = number
                    if is_safe(number, constraint, array_9by9, row, col) :
                        array_9by9[row][col] = number
                        print("number in array: ")
                        print(number)
                        # for row
                        print(array_9by9)
                        # Recursively solve the rest of the puzzle
                        if solve_sudoku(array_9by9):
                            # print("called solve_sudoku")
                            return True
                        # Backtrack
                        array_9by9[row][col] = 0
                        if array_9by9[row][col] == 0 :
                            print("back tracked!")
                return False
    return True


# print("constraints: ")
# print(constraints)
# print("readable constraints: ")
# print(readable_constraints(constraints))
solve = solve_sudoku(array_9by9)
# print(solve)

# print(is_safe(5, find_constraint("31", readable_constraints(constraints)), array_9by9, 2, 0))



# 11 21 22 > 14
# 12 > 4
# 13 23 > 10
# 14 15 25 > 16 
# 16 > 7
# 26 27 > 6 
# 17 18 > 3
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
# 54 64 65 66 > 23  
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


# array_9by9 = [[6, 0, 9, 0, 0, 7, 0, 3, 0],
# [0, 0, 0, 0, 9, 0, 0, 0, 6],
# [0, 2, 0, 0, 0, 3, 9, 4, 0],
# [0, 0, 0, 0, 8, 2, 7, 0, 0],
# [2, 0, 8, 0, 7, 0, 0, 0, 3],
# [0, 0, 0, 9, 1, 6, 0, 8, 0],
# [0, 0, 2, 0, 0, 0, 0, 1, 4],
# [3, 0, 4, 6, 5, 0, 8, 0, 0],
# [1, 0, 5, 0, 0, 9, 0, 0, 0]]


# print(is_in_square(array_9by9, 3, 1, 1))
# readable_constraint(constraints[3])
# print(count_cages(readable_constraint(constraints[3]), array_9by9))
# print(goal_count(readable_constraint(constraints[3])))
# print(check_cage("11", array_9by9))


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

