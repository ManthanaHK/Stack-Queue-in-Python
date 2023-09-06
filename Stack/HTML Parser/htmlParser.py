from stackImplementing import *

instance = Stack()

def match_tags(html):
    i = 0  
    while i < len(html):
        if html[i] == '<':
            if html[i:i + 2] == '</':
                i += 2
                tag_end = html.find('>',i)
                if tag_end == -1:
                    return False  
                closing_tag = html[i:tag_end].strip()
                i = tag_end + 1
                if not instance.data or instance.stackPop() != closing_tag:
                    return False
            else:
                i += 1
                tag_end = html.find('>', i)
                if tag_end == -1:
                    return False  
                opening_tag = html[i:tag_end].strip()
                i = tag_end + 1
                instance.stackPush(opening_tag)
        else:
            i += 1
    return len(instance.data) == 0


try:
    with open('E:\\ADS LabFiles\\Stack\\HTML Parser\\forParser.html','r') as file:
        cnt = file.read()
except FileNotFoundError:
    print("File not found")


if match_tags(cnt):
    print("Tags are properly matched.")
else:
    print("Tags are not properly matched.")