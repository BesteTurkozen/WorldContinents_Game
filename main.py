import pandas as pd
import turtle

screen = turtle.Screen()
screen.setup(width=1200, height=750)
screen.title("World Continent Game")
image = "world_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("world_map.csv", encoding="latin-1")
all_continents = data["continents"].tolist()
guessed_continents = []

while len(guessed_continents) < 9:
    answer_continent = screen.textinput(title=f"{len(guessed_continents)}/9", prompt="What's another continent's name?").title()

    if answer_continent == "Exit":
        missing_continents = [continent for continent in all_continents if continent not in guessed_continents]
        new_data = pd.DataFrame(missing_continents, columns=["continents"])
        new_data.to_csv("continents_to_learn.csv", index=False)
        break

    if answer_continent in all_continents:
        guessed_continents.append(answer_continent)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        continent_data = data[data["continents"] == answer_continent]
        t.goto(int(continent_data["x"]), int(continent_data["y"]))
        t.write(answer_continent, font=('Arial', 20, 'bold'))

screen.mainloop()


#code to find locations
#def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()
