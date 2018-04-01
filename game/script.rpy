init:
    python:
        d = Character(name="Dave")
        s = Character(name="Skye")
        p = Character(name="You")

        class mycharacter:
            def __init__(self,sayer=None,location="home",skills={   "plot"        :2,
                                                                    "writing"     :2,
                                                                    "gameplay"    :2,
                                                                    "characters"  :2,
                                                                    "backgrounds" :2,
                                                                    "music"       :2,
                                                                    "hype"        :2}):
                self.stamina=6
                self.hunger=5
                self.recruited=False
                self.location=location
                self.sayer=sayer
                self.action=""
                self.skills=skills

default connections = { "home":["city"],
                        "city":["home","cafe","park"],
                        "cafe":["city"],
                        "park":["city","forest"],
                      "forest":["park"]}

default skye=mycharacter(sayer=s,location="park",skills={   "plot"        :0,
                                                            "writing"     :0,
                                                            "gameplay"    :0,
                                                            "characters"  :6,
                                                            "backgrounds" :3,
                                                            "music"       :5,
                                                            "hype"        :0})

default dave=mycharacter(sayer=d,location="cafe",skills={   "plot"        :4,
                                                            "writing"     :6,
                                                            "gameplay"    :5,
                                                            "characters"  :5,
                                                            "backgrounds" :3,
                                                            "music"       :0,
                                                            "hype"        :4})
default player=mycharacter(sayer=p,location="home")
default characterlist=[skye,dave,player]
default game_status={   "plot"        :0,
                        "writing"     :0,
                        "gameplay"    :0,
                        "characters"  :0,
                        "backgrounds" :0,
                        "music"       :0,
                        "hype"        :0}



image bg room = ConditionSwitch("clockint==0", "bg room dawn.jpg",
                                "clockint==1", "bg room noon.jpg",
                                "clockint==2", "bg room dusk.jpg",
                                "clockint==3", "bg room midnight.jpg")
label show_characters:
    if skye.location==player.location:
        show skye:
            xalign 0.3
    if dave.location==player.location:
        show dave:
            xalign 0.7
    return

label start:
    $player.recruited=True
    scene bg room
    "I've been wanting to make a game for quite a while."
    "Since this month is the start of NaNoRenO, I figured I'd use this opportunity to do it."
    "But since this is just a demo, I'll only have a single week."
    "I don't feel motivated at all. Maybe I should go grab something to eat."
    "I know there's a cafe all the way across the city."
    "After I go there and get something to eat, I'm sure I'll be able to work much easier."
    "Lemme just uhhhh"
    "Grab my brick."
    $backpack_items.append(brick)
    "There we go."
    jump mainloop
    return


label home:
    scene bg room morning
    call show_characters
    "I'm at home."
    return

label city:
    scene bg city morning
    call show_characters
    "I'm at the city"
    return

label cafe:
    scene bg cafe morning
    call show_characters
    "I'm at the cafe"
    if dave.recruited==False:
        "There's someone here."

    return

label park:
    scene bg park morning
    call show_characters
    "I'm at the park"
    return

label forest:
    scene bg forest morning
    call show_characters
    "you're at the forest"
    return
