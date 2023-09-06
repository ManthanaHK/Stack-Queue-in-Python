def reversingContent(filePath):
    stack = []
    try:
        with open(filePath,'r') as file:
            cnt = file.read()
        file.close()
    except FileNotFoundError:
        print("File Not Found")
    cnt = cnt.split()
    stack = cnt
    stack.reverse()

    try:
        with open(filePath,'w') as fileWrite:
            for i in stack:
                fileWrite.write(i+" ")
        fileWrite.close()
    except FileNotFoundError:
        print("File Not Found")

reversingContent('E:\ADS LabFiles\DummyFile1.txt')