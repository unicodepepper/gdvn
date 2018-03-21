default weekdays = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
default times = ("dawn","noon","dusk","midnight")
default clockint = 3
default clockstr = ""
default dateint  =-1
default datestr  = ""
default displaytime=""

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
    return

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
