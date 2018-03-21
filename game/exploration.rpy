label mainloop:
    python:     #BUILDING THE MENU
        menulist=[("Open the backpack.","backpack_label")]
        for i in connections[currplace]:
            menulist.append((i,i)) #TODO change it so locations have pretty names?
        currjump=renpy.display_menu(menulist,screen="choice")
        if currjump=="backpack_label":
            currjump=renpy.call_screen("backpack")
            if currjump=="back":
                renpy.jump("mainloop")
    $renpy.call(currjump)
    jump mainloop
