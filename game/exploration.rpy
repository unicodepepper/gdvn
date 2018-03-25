label mainloop:
    python:
        mnlplist=[]                                     #make the menu
        if skye.location==player.location and skye.action=="": #TODO change these hardcoded characters tbh
            mnlplist.append(("talk to skye",skye))
        if dave.location==player.location and dave.action=="":
            mnlplist.append(("talk to dave",dave))
        mnlplist=mnlplist+[("use an item","backpack"),("stay here","work"),("go somewhere else","travel")]

        mnlpaction=renpy.display_menu(mnlplist)     #display the menu

    if type(mnlpaction)==mycharacter:               #redirect the player
        call charmenu(mnlpaction)
    elif mnlpaction=="backpack":
        call backpackmenu(player)
    elif mnlpaction=="work":
        call workmenu(player)
    elif mnlpaction=="travel":
        call travelmenu()
    else:
        "you're not supposed to see this"
    jump mainloop


label charmenu(character):
    menu:
        "I've got something for you.":
            call backpack(character)
        "Can you help me do something?":
            call workmenu(character)
    return


label workmenu(character):
    python:
        worklist=[]
        for i in game_status.keys():
            worklist.append(("work in the "+i,i))
        workaction=renpy.display_menu(worklist)
        character.action=workaction
    if character.name=="you":
        "you're gonna focus on the [workaction] of the game."
        call time_advance
    else:
        "[character.name] is gonna focus on the [workaction] of the game."

    return

label travelmenu():
    python:
        travellist=[]
        for i in connections[player.location]:
            travellist.append(("go to the "+i,i))
        travelaction=renpy.display_menu(travellist)
        player.location=travelaction
    call expression travelaction
