init:
    python:
        class mycharacter:
            def __init__(self,name="",location="home"):
                self.stamina=6
                self.motivation=1
                self.hunger=5
                self.recruited=False
                self.location=location
                self.name=name
                self.action=""


default connections = { "home":["city"],
                        "city":["home","cafe","park"],
                        "cafe":["city"],
                        "park":["city","forest"],
                      "forest":["park"],}

default skye=mycharacter(name="skye",location="park")
default dave=mycharacter(name="dave",location="cafe")
default player=mycharacter(name="you",location="home")
default characterlist=[skye,dave,player]

default game_status={   "plot"        :0,
                        "writing"     :0,
                        "gameplay"    :0,
                        "characters"  :0,
                        "backgrounds" :0,
                        "music"       :0,
                        "hype"        :0}

label start:
    "woo, I just started the game"
    $backpack_items.append(brick)
    jump mainloop
    "test"
    return


label home:
    "you are at home"
    return

label city:
    "you're at the city"
    "you found food on the floor"
    $backpack_items.append(food)
    return

label cafe:
    "you're at the cafe"
    return

label park:
    "you're at the park"
    return

label forest:
    "you're at the forest"
    return
