default weekdays = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
default times = ("dawn","noon","dusk","midnight")
default clockint = 3
default clockstr = ""
default dateint  =-1
default datestr  = ""
default displaytime=""

default show_stats=True

label time_advance():
    python:
        clockint+=1                                 #advance the time
        if clockint >=4:                            #carry over
            clockint=0
            dateint = dateint+1
        dateWeekModulo = dateint%7                  #set display text
        datestr = weekdays[dateWeekModulo]
        clockstr= times[clockint]
        displaytime = "it's "+datestr+" at "+clockstr+"."
        renpy.call("game_advance")
    return

screen charstats(character):
    #vbox:
        text character.name+"'s stamina: "+str(character.stamina) xalign 1.0
        text character.name+"'s motivation: "+str(character.motivation) xalign 1.0
        text character.name+"'s hunger: "+str(character.hunger) xalign 1.0

screen stats_screen:
    zorder 100
    style_prefix "stats"
    if show_stats:
        vbox:
            xalign 1.0
            yalign 0.0
            if displaytime:
                text "[displaytime]" xalign 1.0
            python:
                if len(backpack_items) == 1: #TODO make modular so I can put weird stuff
                    ui.text("there is 1 item in your backpack.")
                else:
                    ui.text("there are "+str(len(backpack_items))+" items in your backpack.")
            text "you're at the [player.location]" xalign 1.0
            for i in characterlist:
                text ""
                use charstats(i)


screen game_status:
    vbox:
        for i in game_status.keys():
            hbox:
                xsize 50
                text str(game_status[i])+"% "
                text i
        frame:
            textbutton "ok" action Return()

label game_advance:
    python:
        for i in characterlist:
            if i.action!="":
                try:
                    game_status[i.action]+=((i.stamina*i.motivation)/i.hunger)
                    i.stamina-=2
                    i.hunger+=2
                except KeyError:
                    pass
                i.action=""
            else:
                i.stamina +=2
                i.hunger+=2
            #TODO cap stamina, hunger and motivation at 10 AND make them unchanged while the character is not recruited
        renpy.display_menu([(None,None)],screen="game_status")
    return
