# template for "Stopwatch: The Game"
# Swapnasheel Sonkamble
# try running on www.codeskulptor.org


from simplegui import *

# define global variables
count = 0
running = False
TotalStops = 0
win = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    t = t/10
    C = t % 10
    t = t/10
    B = t % 6
    A = t / 6
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)

#defining start, stop, reset and score handlers
 
def stop():
    global running, count, TotalStops, win
    timer.stop()
    if running:
        TotalStops += 1
        if count % 10 == 0:
            win += 1
    running = False
        
def start():
    global running
    timer.start()
    running = True
           
def reset():
    global running, win, count, TotalStops
    timer.stop()
    running = False
    win = 0
    count = 0
    TotalStops = 0

def score():
    global win, TotalStops
    return str(win) + '/' + str(TotalStops)

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    pass

# define draw handler
def draw(canvas):
    global count
    canvas.draw_text(format(count), [60,115], 36, "White")
    canvas.draw_text(score(), [155,26], 26, "Green")

    
# create frame
f = create_frame("Stopwatch", 200, 200)

# register event handlers
f.add_button("Start", start, 120)
f.add_button("Stop", stop, 120)
f.add_button("Reset", reset, 120)
f.set_draw_handler(draw)

#creating timer
timer = create_timer(100, tick)

# start frame and timer
f.start()                           
