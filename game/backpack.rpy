default backpack_items = []


label backpackmenu(character):
    "you're opening the backpack for [character.name]"
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

$brick=myitem(name="Brick.", description="It's a brick.",action="brickaction")

label brickaction:
    "you hold the brick."
    "it's a bit heavy."
    return
