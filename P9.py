def adder(N):
    i =  0
    accumulator = 0
    while (i < N):
        i = i + 1
        accumulator = accumulator + i
    return accumulator

#
print "adder(5): ", adder(5)
print "adder(10): ", adder(10)

###
done = False
while not done:
    c = input("Enter some value: ")

    if c.isdigit():
        print "Is digit"
    elif c.isalpha():
        print "Is letter"
    else:
        done = True

print "Thanks for using this program"
