init:
    python:
        class item():
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

$brick=item(name="Brick.", description="It's a brick.",action="brickaction")

label brickaction:
    "you hold the brick."
    "it's a bit heavy."
    return
