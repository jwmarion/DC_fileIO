#ex2

ifile = raw_input("What file would you like to write to? (Try wtest.txt)")
data = raw_input("What would you like to write to this file?")

with open(ifile, 'w') as f1:
    f1.write(data)
