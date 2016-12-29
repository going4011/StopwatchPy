#http://www.codeskulptor.org/#user39_A5SiEUpX0EOuHvH.py
#Stopwatch: The Game mini-project.
#Timer with a start, stop and reset function.
#Number of times stopped on a whole second is
#displayed along with total times stopped.

import simplegui

#define global variables
time = 0
tries = 0
wins = 0
WIDTH = 300
HEIGHT = 200

def format(t):
    """
    Helper function that converts time into
    properly formatted as A:BC.D
    """
    
    #Calculates minutes, seconds (two digits) and
    #tenths of seconds
    minutes = (t / 10) / 60
    seconds10 = ((t / 10) % 60) / 10
    seconds = ((t / 10) % 60) % 10
    tenthseconds = t % 10
    
    #Returns properly formatted stopwatch time
    return str(minutes) + ":" + str(seconds10) + str(seconds) + "." + str(tenthseconds)
    
    
def button_start():
    """
    Event handler that starts the stopwatch.
    """
    timer.start()
    
def button_stop():
    """
    Event handler that stops the stopwatch.
    Also reports how many times it has been stopped
    as well as how many times on a whole second.
    """
    global tries
    global wins
    
    #Checks if timer is running.
    #This prevents multiple increments to tries
    #if the stop button is hit repeatedly.
    if timer.is_running():
        timer.stop()
        tries += 1
        
        #If the time is stopped on a whole second,
        #increment the win counter.
        if (time % 10) == 0:
            wins += 1
    
def button_reset():
    """
    Event handler that resets the stopwatch and
    the player's tries/wins score.
    """
    global time
    global tries
    global wins
    time = 0
    tries = 0
    wins = 0


def timer_handler():
    """
    Event handler for timer. Increments time variable
    every tick of the timer.
    """
    global time
    time +=1


def draw_handler(canvas):
    """
    Draw handler draws the time by calling the format
    helper function. Also displays wins and tries at the
    top right corner of the screen.
    """
    canvas.draw_text(format(time), [55, 125], 72, 'Red')
    canvas.draw_text(str(wins) + " / " + str(tries), [225, 30], 34, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch', WIDTH, HEIGHT)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start = frame.add_button('Start', button_start)
stop = frame.add_button('Stop', button_stop)
reser = frame.add_button('Reset', button_reset)

# start frame
frame.start()