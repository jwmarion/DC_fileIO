#ex3

def word_histogram(input):
    tdict = {}
    for word in input.split():
        if tdict.get(word) == None:
            tdict[word] = 1
        else:
            tdict[word] += 1
    return tdict

def letter_histogram(word):
    tdict = {}
    for x in xrange(len(word)):
        if tdict.get(word[x]) == None:
            tdict[word[x]] = 1
        else:
             tdict[word[x]] += 1
    return tdict

file1 = raw_input("Enter the filename: ")

with open(file1, 'r') as f1:
    data = f1.read()
print word_histogram(data)
print ""
print letter_histogram(data)
