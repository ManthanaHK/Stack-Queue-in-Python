import os

def parenthesisMatching(filePath):
    stack = []
    open_list = "([{"
    close_list = ")]}"
    try:
        with open(filePath,'r') as file:
            content = file.read()
        file.close()
    except FileNotFoundError:
        print("File Not Found")
        
    for i in content:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            if len(stack) == 0:
                print("Matching Not Done : "+i)
                return 
            ind = close_list.index(i)
            val = open_list[ind]
            if val in stack:
                ind1 = stack.index(val)
                if stack.index(val) == len(stack)-1:
                    stack.pop(ind1)
            else:
                print("Matching Not Done: "+i)
                return
    if len(stack) != 0:
        print("Syntax Error")

parenthesisMatching('E:\ADS LabFiles\DummyFile2.txt')