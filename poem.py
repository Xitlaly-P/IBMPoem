import turtle

vocab = {
    "a" : '',
    "b" : '',
    "c" : '',
    "d" : '',
    "e" : '',
    "f" : '',
    "g" : '',
    "h" : '',
    "i" : '',
    "j" : '',
    "k" : '',
    "l" : '',
    "m" : '',
    "n" : '',
    "o" : '',
    "p" : '',
    "q" : '',
    "r" : '',
    "s" : '',
    "t" : '',
    "u" : '',
    "v" : '',
    "w" : '',
    "x" : '',
    "y" : '',
    "z" : ''
}

fontCount = {
    "a" : 10,
    "b" : 10,
    "c" : 10,
    "d" : 10,
    "e" : 10,
    "f" : 10,
    "g" : 10,
    "h" : 10,
    "i" : 10,
    "j" : 10,
    "k" : 10,
    "l" : 10,
    "m" : 10,
    "n" : 10,
    "o" : 10,
    "p" : 10,
    "q" : 10,
    "r" : 10,
    "s" : 10,
    "t" : 10,
    "u" : 10,
    "v" : 10,
    "w" : 10,
    "x" : 10,
    "y" : 10,
    "z" : 10
}

for x in vocab:
    temp = input("Enter a word for the letter '{}': " .format(x))
    vocab[x] = temp

titleAc = input("Enter a 3 letter word or phrase: ")
if len(titleAc) != 3:
    print("Not 3 letters! Error!!")
    exit()

paper = turtle.Screen()
pen = turtle.Turtle()
title = []

pen.up()
pen.goto(0, 200)

for char in titleAc.lower():
    pen.write(vocab[char], font=("calibri", fontCount[char], "normal") , move=True)
    pen.forward(4)
    fontCount[char] += 1
    title.append(vocab[char])
    
lineCount = 1
i = 0
pen.goto(-200, 100)
while i < len(title):
    for char in title[i]:
        pen.write(vocab[char], move = True, font=("calibri", fontCount[char], "normal"))
        pen.forward(4)
        fontCount[char] += 1
        if lineCount <= 3:
            title.append(vocab[char])
    pen.goto(-200, pen.ycor() - 30)
    lineCount += 1
    i += 1

paper.exitonclick()