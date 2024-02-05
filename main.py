array_9x9 = [[6, 0, 9, 0, 0, 7, 0, 3, 0],
[3, 8, 0, 0, 9, 0, 0, 0, 6],
[6, 2, 0, 0, 0, 3, 9, 4, 0],
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
for row in array_9x9:
    print(row)
    
print(array_9x9[0][0])
cages = int(input())
constraints = []
for i in range(cages) :
    constraints.append(input())
    
# # for i in range(cages) :
    
print(constraints)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_safe(number, constraint, array, i, j) :
    index = [i , j]
    if any(row[j] == number for row in array) :
        if any(col[i] == number for col in array) :
            if count_cages(readable_constraints(constraint)) + number == goal_count(readable_constraints(constraint)):
                if not find_zeros(constraint) :
                    return True
            elif count_cages(readable_constraints(constraint)) + number < goal_count(readable_constraints(constraint)) :
                if find_zeros(constraint) :
                    return True
    return False


    
def count_cages(readable_constraint, array) :
    counter = 0
    size = len(readable_constraint)
    # readable_constraint.pop()
    for cage_number in readable_constraint :
        i = translate_cage_number(cage_number)[0]
        j = translate_cage_number(cage_number)[1]
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
    index = []
    index.append(int(string[0]))
    index.append(int(string[1]))
    return index



def readable_constraints(constraints) :
    readable_constraints = []
    single_constraint = []
    for constraint in constraints :
        # print("constraint :")
        # print(constraint)
        for part in constraint.split() :
            # print("part :")
            # print(part)
            if part != '>' :
                single_constraint.append(part)
        readable_constraints.append(single_constraint)
        single_constraint = []
    return readable_constraints

# print(len(readable_constraints(constraints)[0]))

# print(translate_cage_number(readable_constraints(constraints)[0][0]))

def cage_number_only (readable_constraint) :
    readable_constraint.pop()
    return readable_constraint
        
def cage_numbers_all_constraints (readable_constraints) :
    new_readable_constraints = []
    for readable_constraint in readable_constraints :
        readable_constraint.pop()
        new_readable_constraints.append(readable_constraint)
    return new_readable_constraints
# print(count_cages(cage_number_only(readable_constraints(constraints)[0]), array_9x9))
# input = str(input())
# print(input.split()[0])

# print(cage_number_only(readable_constraints(constraints)[1]))

# print(readable_constraints(constraints))

#11 21 22 > 14
#12 > 4
#13 23 > 10
#14 15 25 > 16
#16 > 7

print(find_constraint('14', cage_numbers_all_constraints(readable_constraints(constraints))))