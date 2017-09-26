def comma(inputlist):
    outputstring=''
    outputstring+=inputlist[0]
    for i in range(1,len(inputlist)-1):
        outputstring+=','+inputlist[i]
    outputstring+=',and '+inputlist[len(inputlist)-1]
    return outputstring

mylist=['apples','bananas', 'tofu', 'cats', 'dogs', 'mice', 'yogurt']
string=comma(mylist)
print(string)
