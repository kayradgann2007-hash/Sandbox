import time
import sys
import turtle

def cool_writing(line):
    for i in line:
        print(i, end="", flush=True)
        time.sleep(0.03)
    print()

def romantic_write(line):
    for i in line:
        print(i, end="", flush=True)
        time.sleep(0.06)
    print()

def main():
    cool_writing("Bugün hayatımdaki en önemli günlerden biri")
    cool_writing("Bu bizim ilk sevgililer günümüz")
    cool_writing("Bu hediye benim için çok şey ifade ediyor, umarım sen de begenirsin")
    time.sleep(1)
    romantic_write("Uzun bir yolculuktu bizim için")
    romantic_write("İyisiyle kötüsüyle,")
    romantic_write("Tartışmalarımızla ve huzur dolu anlarımızla,")
    romantic_write("En çok da sevgi dolu günler geçirdik")
    romantic_write("Zaten biricik sevgilimsin ama yine de...")
    time.sleep(0.5)
    
    answer = input("Benim sevgilim olur musun? (evet/hayır) ")
    
    if answer.lower() == "evet":
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.bgcolor("#87CEEB")
        t = turtle.Turtle()
        t.speed(0)

        
        t.penup()
        t.goto(-400, -300)
        t.pendown()
        t.color("#45a049")
        t.begin_fill()
        for _ in range(2):
            t.forward(800)
            t.left(90)
            t.forward(350)
            t.left(90)
        t.end_fill()

        
        flowers=[
    (-350, -110, 30), (-315, -45, 30), (-280, -90, 30), (-245, -30, 30), 
    (-210, -75, 30), (-175, -55, 30), (-140, -100, 30), (-105, -40, 30), 
    (-70, -85, 30), (-35, -25, 30), (0, -95, 30), (35, -50, 30), 
    (70, -115, 30), (105, -35, 30), (140, -80, 30), (175, -60, 30), 
    (210, -105, 30), (245, -40, 30), (280, -90, 30), (315, -30, 30)
]

        for x,y,size in flowers:
            t.penup()
            t.goto(x, y)
            t.setheading(270)
            t.pendown()
            t.color("#228B22")
            t.pensize(8)
            t.forward(200)

        
            t.pensize(1)
            t.color("#FFD700")
            for i in range(18):
                t.penup()
                t.goto(x, y)
                t.setheading(i * 20)
                t.pendown()
                t.begin_fill()
                t.circle(size, 60)
                t.left(120)
                t.circle(size, 60)
                t.end_fill()

        
            t.penup()
            t.goto(x, y - size/2)
            t.setheading(0)
            t.color("#5C4033")
            t.begin_fill()
            t.circle(20)
            t.end_fill()

        
        t.penup()
        t.goto(-150, -250)
        t.color("white")
        message = "Nice aylara, yıllara, bir ömre... Seni çok seviyorum Eylülcüm"
        for char in message:
            t.write(char, move=True, align="left", font=("Arial", 20, "bold"))
            time.sleep(0.1)

        t.hideturtle()
        screen.mainloop()

    elif answer.lower() == "no":
        print("Wrong answer")
        exit(1)

if __name__ == "__main__":
    main()

