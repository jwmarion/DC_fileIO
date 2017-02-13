#ex1

path = raw_input("Enter a file:(try test.txt) ")
with open(path) as f1:
    print f1.read()
