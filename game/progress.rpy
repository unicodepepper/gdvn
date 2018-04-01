default weekdays = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
default times = ("dawn","noon","dusk","midnight")
default clockint = 0
default clockstr = ""
default dateint  = 1
default datestr  = ""
default displaytime="it's sunday 1 at dawn"

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
        displaytime = "it's "+datestr+" "+str(dateint)+" at "+clockstr+"."
        renpy.call("game_advance")
    return

screen charstats(character):
    if character.sayer.name=="You":
        text "your stamina: "+str(character.stamina) xalign 1.0
        text "your hunger: "+str(character.hunger) xalign 1.0
    else:
        text character.sayer.name+"'s stamina: "+str(character.stamina) xalign 1.0
        text character.sayer.name+"'s hunger: "+str(character.hunger) xalign 1.0

screen stats_screen:
    zorder 100
    style_prefix "stats"
    if show_stats:
      frame:
        xalign 1.0
        yalign 0.0
        vbox:
            if displaytime:
                text "[displaytime]" xalign 1.0
            python:
                if len(backpack_items) == 1: #TODO make modular so I can put weird stuff
                    ui.text("there is 1 item in your backpack.")
                else:
                    ui.text("there are "+str(len(backpack_items))+" items in your backpack.")
            text "you're at the [player.location]" xalign 1.0
            for i in characterlist:
                if i.recruited==True:
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
          if character.recruited:
            if i.action!="":
                try:
                    game_status[i.action]+=((i.stamina*i.skills[i.action])/i.hunger)
                    i.stamina-=2
                    i.hunger+=2
                except KeyError:
                    pass
                i.action=""
            else:
                i.stamina +=2
                i.hunger+=2
            if i.stamina>10:
                i.stamina=10
            elif i.stamina<1:
                i.stamina=1
            if i.hunger>10:
                i.hunger=10
            elif i.hunger<1:
                i.hunger=1
        renpy.display_menu([(None,None)],screen="game_status")
    return
