from tkinter import *
import random



game_width=700
game_height=700
speed=500
space_size=50
body_parts=3
snake_clor="#00FF7F"
food_color="#FF6103"
background_color="#7F7FFF"


class snake:
    def __init__(self) :
        self.body_size=body_parts
        self.coordinates=[]
        self.squares=[]
        
        for i in range(0,body_parts):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_clor,tag="snake")
            self.squares.append(square)

class Food :
    def __init__(self) :
        x=random.randint(0,((game_width/space_size)-1)*space_size)
        y=random.randint(0,((game_height/space_size)-1)*space_size)
        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+25,y+25,fill=food_color,tag="food")


def next_turn(Snake,food):
    x,y=Snake.coordinates[0]
    z=food.coordinates[0]
    w=food.coordinates[1]
    print(x,y)
    print(z,w)
    if direction=="up":
        y-=space_size
    if direction=="down":
        y+=space_size
    if direction=="left":
        x-=space_size
    if direction=="right":
        x+=space_size
    Snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_clor)
    Snake.squares.insert(0,square)
    print(( x-20 < food.coordinates[0]<x+20) and (y-20<food.coordinates[1]<y+20))
    if (( x-20< food.coordinates[0]<x+20) and (y-20<food.coordinates[1]<y+20)):
        global score
        score += 1
        label.config(text="score:{}".format(score))
        canvas.delete("food")
        food=Food()
    else:
        del Snake.coordinates[-1]
        canvas.delete(Snake.squares[-1])
        del Snake.squares[-1]
    """if check_collision(Snake):
        game_over()
    else:"""
    window.after(speed,next_turn,Snake,food)

def change_direction(new_direction):
    global direction 
    if new_direction == 'left':
        if direction!='right':
             direction=new_direction
    elif new_direction == 'right':
        if direction!='left':
            direction=new_direction
    elif new_direction == 'up':
        if direction!='down':
            direction=new_direction
    elif new_direction == 'down':
        if direction!='up':
            direction=new_direction

def check_collision(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=game_width:
        print ("game over")
        return True
    if y<0 or y>=game_height:
        print ("game over")
        return True
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y ==body_part[1]:
            print ("game over")
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER",fill="red",tag="gameover")

window=Tk()
window.title("snake game")
window.resizable(False,False)
score=0
direction='down'

label=Label(window,text="score:{}".format(score),font=('consolas',40))
label.pack()

canvas=Canvas(window,bg=background_color,height=game_height,width=game_height)
canvas.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/4)-(window_width/4))
y=int((screen_height/4)-(window_height/4))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event:change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))
Snake=snake()
food=Food()
next_turn(Snake,food)
window.mainloop()