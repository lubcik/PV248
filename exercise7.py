import numpy

# Part 1
m = numpy.loadtxt('exercise7.data')
m.resize((3,3))

print("Determinant: {}".format(numpy.linalg.det(m)))
print("Inverse matrix:\n{}".format(numpy.linalg.inv(m)))

# Part 2
solution = numpy.linalg.solve(m, numpy.array([1, 1, 1]))
print("Solution of the system: {}".format(solution))

# Part 3
with open('exercise7_eq.data', 'r') as f:
    raw_data = f.readlines()

def parse_coef(line):
    left_side = line.split('=')[0]
    parts = left_side.split(' ')

    sign = 1
    variable = None
    coefficient = None

    result = []

    for part in parts:
        if part == '+':
            pass
        elif part == '-':
            sign = -1
        elif part.isdigit():
            coefficient = sign * float(part)
        elif part.isalpha():
            if coefficient is None:
                coefficient = sign
            variable = part

        if variable and coefficient:
            result.append(coefficient)
            sign = 1
            variable = None
            coefficient = None

    return result

def parse_value(line):
    right_side = line.split('=')[1]
    return float(right_side.strip())

def parse_letters(line):
    left_side = line.split('=')[0]
    parts = left_side.split(' ')

    return [part for part in parts if part.isalpha()]

coefficients = [parse_coef(line) for line in raw_data]
values = [parse_value(line) for line in raw_data]
variables = parse_letters(raw_data[0])

print("Loaded system")
system_matrix = numpy.array(coefficients)
print(system_matrix)
system_values = numpy.array(values)
print(system_values)
system_solution = numpy.linalg.solve(system_matrix, system_values)

solution_string = ', '.join([
    var + ' = ' + str(value)
    for var, value in zip(variables, system_solution.tolist())
])

print("solution: {}".format(solution_string))
