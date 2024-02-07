import math

domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cage_domains = []
for i in range(81) :
    cage_domains.append(domain)
    

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
    result += (i * length) + j + 1
    return result
    

def forward_pruning(number, index, cage_domains):
    #delete number from row:
    j = index[1]
    for i in range(9) :
        if i != index[0] :
            prune_index(number, (i, j), cage_domains)
        else :
            cage_domains[turn_index_to_number(index, 9)].clear()
    #delete number from column:
    i = index[0]
    j = 0
    for j in range(9) :
        if j != index [1] :
            prune_index(number, (i, j), cage_domains)
            
    #delete number from 3*3 square
    i = find_square[0]
    j = find_square[1]
    for f in range(i * 3 + 3) :
        for t in range(j * 3 + 3) :
            try :
                prune_index(number, (f, t), cage_domains)
            except:
                pass
    
    
def find_square(index, square) :
    square_i = math.floor(index[0] / 3)
    square_j = math.floor(index[1] / 3)
    new_index = square_i , square_j 
    return square_i , square_j
        
    
def prune_index(num, index, cage_domains):
    number = turn_index_to_number(index)
    cage_domains[number].remove(num)
    return cage_domains


array_9by9 = [[6, 0, 9, 0, 0, 7, 0, 3, 0],
[0, 0, 0, 0, 9, 0, 0, 0, 6],
[0, 2, 0, 0, 0, 3, 9, 4, 0],
[0, 0, 0, 0, 8, 2, 7, 0, 0],
[2, 0, 8, 0, 7, 0, 0, 0, 3],
[0, 0, 0, 9, 1, 6, 0, 8, 0],
[0, 0, 2, 0, 0, 0, 0, 1, 4],
[3, 0, 4, 6, 5, 0, 8, 0, 0],
[1, 0, 5, 0, 0, 9, 0, 0, 0]]

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

def is_safe(number, constraint, array, i, j) :
    index = [i , j]
    print("i in is_safe: ")
    print(i)
    print("j in is_safe: ")
    print(j)
    if any(row[j] == number for row in array) :
        if any(col[i] == number for col in array) :
            print("about to call count_cages")
            print("about to call goal_count")
            if count_cages(constraint, array_9by9) + number == goal_count(constraint):
                print("about to call find_zeros")
                if not find_zeros(constraint) :
                    return True
        
            elif count_cages(constraint, array_9by9) + number < goal_count(constraint) :
                print("called count_cages")
                print("called goal_count")
                print("about to call find_zeros")
                if find_zeros(constraint) :
                    return True
    return False

    
def count_cages(readable_constraint, array) :
    counter = 0
    # size = len(readable_constraint)
    # readable_constraint.pop()
    readable_constraint = cage_number_only(readable_constraint)
    print("readable_contsraint in count_cages: ")
    print(readable_constraint)
    for cage_number in readable_constraint :
        print("cage_number in count_cages: ")
        print(cage_number)
        translation = translate_cage_number(cage_number)
        i = translation[0]
        print("i in count_cages: ")
        print(i)
        j = translation[1]
        print("j in count_cages: ")
        print(j)
        # j = translate_cage_number(cage_number)
        counter += array[i - 1][j - 1]
    return counter
        

def goal_count(readable_constraint) :
    return int(readable_constraint[-1])


def find_constraint(cageNumber, readable_constraints) :
    for constraint in readable_constraints :
        for cage_number in constraint :
            if cage_number == cageNumber :
                return constraint
         
            
def find_zeros(constraint, array) :
    for cageNumber in cage_number_only(readable_constraints(constraint)) :
        if (check_cage(translate_cage_number(cageNumber), array)) == 0 :
            return True
    return False


def check_cage(cage_number, array) :
    i = cage_number[0]
    j = cage_number[1]
    return array[i][j]
     

def translate_cage_number(string) :
    print("string in translate_cage_number: " + string)
    index = []
    index.append(int(string[0]))
    index.append(int(string[1]))
    return index


def readable_constraints(constraints) :
    counter1 = 0
    counter2 = 0
    readable_constraints = []
    single_constraint = []
    for constraint in constraints :
        # print("iteration through every constraint:")
        counter1 += 1
        # print("constraint :")
        # print(constraint)
        for part in constraint.split() :
            # print("iteration through 1 constraint: ")
            counter2 += 1
            # print("part :")
            # print(part)
            if part != '>' :
                single_constraint.append(part)
        readable_constraints.append(single_constraint)
        single_constraint = []
    return readable_constraints


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
    for row in range(9):
        for col in range(9):
            #find constraint
            string = ''
            string += str(row + 1)
            string += str(col + 1)
            print("string in solve_sudoku: " + string)
            # print(string)
            constraint = find_constraint(string, readable_constraints(constraints))
            print("called find_constraint")
            print("constraint in solve_sudoku: ")
            print(constraint)
            counter += 1
            print("counter in solve_sudoku: ")
            print(counter)
            print("col in solve_sudoku: ")
            print(col)
            if array_9by9[row][col] == 0:
                # Try to fill the cell with a valid number
                for number in range(1, 10):
                    print("number: ")
                    print(number)
                    print("about to call is_safe: ")
                    if is_safe(number, constraint, array_9by9, row, col) :
                        array_9by9[row][col] = number
                        print(array_9by9)
                        # Recursively solve the rest of the puzzle
                        if solve_sudoku(array_9by9):
                            print("called solve_sudoku")
                            return True
                        # Backtrack
                        array_9by9[row][col] = 0
                return False
    return True


print("constraints: ")
print(constraints)
print("readable constraints: ")
print(readable_constraints(constraints))
solve_sudoku(array_9by9)