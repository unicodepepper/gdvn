default backpack_items = []


init:
    python:
        class thing():
            def __init__(self, name="???", description="This item doesn't exist.", image="exitbutton_hover.png", action=None):
                self.name=name
                self.description=description
                self.image=image
                self.action=action
                pass

screen backpack():
    vbox:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 600
        xfill True
        yfill True
        vpgrid:
            ymaximum 400
            yminimum 400
            cols 1
            #spacing 5
            draggable True
            mousewheel True
            scrollbars "vertical"

            # Since we have scrollbars, we have to position the side, rather
            # than the vpgrid proper.
            side_xalign 0.5
            vbox:
                frame:
                    xfill True
                    text "Use an item."
                vpgrid:
                    cols 2
                    frame:
                        xysize (294,50)
                        textbutton "Go back." action Return("back"):
                            tooltip "Return to the previous screen."
                            yalign 0.5
                    for i in backpack_items:
                        frame:
                            xysize (294,50)
                            textbutton i.name action Return(i.action):
                                tooltip i.description
                                yalign 0.5
                        # imagebutton auto i.image action Return(i.action):
                        #     tooltip i.description
        frame:
            padding (10,10)
            $tooltip=GetTooltip()
            xysize (600,100)
            if tooltip:
                text "[tooltip]"
