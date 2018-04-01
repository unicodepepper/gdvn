default backpack_items = []


label backpackmenu(character):
    python:
        backpacklist=[]
        for i in backpack_items:
            backpacklist.append((i.name,i.action))
        renpy.call(renpy.display_menu(backpacklist),character)


    return


    ## below is the fancy backpack screen, which I've disabled for testing purposes

    # vbox:
    #     viewport:
    #         scrollbars "vertical"
    #         frame:
    #             xfill True
    #             textbutton "Go back." action Return("back"):
    #                 tooltip "Return to the previous screen."
    #                 yalign 0.5
    #         for i in backpack_items:
    #             frame:
    #                 xfill True
    #                 textbutton i.name action Return(i.action):
    #                     tooltip i.description
    #                     yalign 0.5
    #             # imagebutton auto i.image action Return(i.action):
    #             #     tooltip i.description
    #     frame:
    #         padding (10,10)
    #         $tooltip=GetTooltip()
    #         xfill True
    #         if tooltip:
    #             text "[tooltip]"








init:
    python:
        class myitem():
            def __init__(   self,
                            name="???",
                            description="This item doesn't exist.",
                            # image="exitbutton_hover.png",
                            action=None):
                self.name=name
                self.description=description
                # self.image=image
                self.action=action
                pass

        brick=myitem(name="brick", description="It's a brick.",action="brickaction")
        yesbrick=myitem(name="brick that makes you say yes", description="It's a brick.",action="yesbrickaction")
        food=myitem(name="food", description="it's food",action="foodaction")

label brickaction(character):
    if character.sayer.name=="You":
        "you hold the brick."
    else:
        "[character.sayer.name] holds the brick."
    $character.sayer("it's a bit heavy.")
    "[character.sayer.name] feels revigorized."
    $character.stamina=6
    return

label foodaction(character):
    if character.sayer.name == "You":
        "you eat the food"
    else:
        "[character.sayer.name] eats the food"
    $character.hunger=1
    $backpack_items.remove(food)

label yesbrickaction(character):
    "[character.sayer.name] holds the brick."
    $character.sayer("Yes")
    return
