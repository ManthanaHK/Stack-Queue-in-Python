from stackImplementing import *
import webbrowser


instance1 = Stack()
instance2 = Stack()


instance1.stackPush('https://www.youtube.com/results?search_query=Kendall+Jenner')
instance1.stackPush('https://www.youtube.com/results?search_query=kylie+Jenner')
instance1.stackPush('https://youtube.com/')


def Buttons():
    but = input("Got To Youtube")
    if but == "Go":
        url = instance1.stackPop()
        instance2.stackPush(url)
        webbrowser.open(url)

    but2 = input("Enter Forward or Backward")
    if but2 == "F":
        webbrowser.open(instance1.stackPop())
    if but2 == "B":
        webbrowser.open(instance2.stackPop())
    but3 = input("Enter Forward or Backward")
    if but3 == "F":
        webbrowser.open(instance1.stackPop())

Buttons()
