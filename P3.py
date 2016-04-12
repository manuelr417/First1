from math import sqrt
def find_hypothenuse(a,b):
    a_squared = a * a
    b_squared = b * b
    result = sqrt(a_squared + b_squared)
    return result

print "hypothenuse 3, 4 - ", find_hypothenuse(3,4)

def print_name(name):
    print "Person Name - " + name

print_name("Jose")
print_name("Ned")
