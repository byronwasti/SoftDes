# Problems 3.5
print "Problem 3.5"
print "+-----+-----+\n/     /     /\n/     /     /\n/     /     /\n/     /     /\n+-----+-----+\n/     /     /\n/     /     /\n/     /     /\n/     /     /\n+-----+-----+\n"
print

# Problem 5.3
def check_fermat(a, b, c, n):
    return "Holy smokes, Fermat was wrong!" if a**n + b**n == c**n else "No, that doesn't work."
print "Please input the four numbers"
a = int(raw_input("Please input a: "))
b = int(raw_input("Please input b: "))
c = int(raw_input("Please input c: "))
n = int(raw_input("Please input n: "))
print check_fermat(a, b, c, n)

# Problem 6.1
def compare(x, y): 
    return 1 if x > y else ( 0 if x == y else -1)

print compare( 1, 2)
