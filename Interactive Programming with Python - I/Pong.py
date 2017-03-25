#author Swapnasheel Sonkamble
#Pong Game
#try running on www.codeskulptor.org

import simplegui
import random

#initailize global variables
Width = 600
Height = 400
BallRadius = 20
PadWidth = 8
PadHeight = 80
HalfPadWidth = PadWidth / 2
HalfPadHeight = PadHeight / 2
Left = False
Right = True
side = Left

#paddles
paddle1_pos = Height / 2.5
paddle2_pos = Height / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5

def gameRestart():
    newgame()

def newgame():
    global paddle1_pos, paddle2_pos # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(0)
    paddle1_pos = Height / 2.5
    paddle2_pos = Height / 2.5
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel   
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0   
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
        
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [Width / 2, Height / 2]	# position the ball at the centre of the canvas
    if direction == Right:
        ball_vel = [random.randrange(120, 240) / 60, -(random.randrange(60, 180) /60)]
    else:
        ball_vel = [-(random.randrange(120, 240) / 60), -(random.randrange(60, 180) / 60)]
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([Width / 2, 0],[Width / 2, Height], 1, "White")
    canvas.draw_line([PadWidth, 0],[PadWidth, Height], 1, "White")
    canvas.draw_line([Width - PadWidth, 0],[Width - PadWidth, Height], 1, "White")
        
    # update ball
    if ball_pos[0] <= BallRadius + PadWidth:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos+PadHeight):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(Right)
            score2 += 1
    if ball_pos[0] >= (Width - BallRadius - PadWidth):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PadHeight):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(Left)
            score1 += 1
    if ball_pos[1] <= BallRadius:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (Height - BallRadius):
        ball_vel[1] = - ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BallRadius, 0.1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= Height - PadHeight:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= Height - PadHeight:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([PadWidth / 2, paddle1_pos],[PadWidth / 2, paddle1_pos + PadHeight], PadWidth, "White")
    canvas.draw_line([Width - PadWidth / 2, paddle2_pos],[Width - PadWidth / 2, paddle2_pos + PadHeight], PadWidth, "White")
    
    # draw scores
    canvas.draw_text(str(score1), (185, 40), 40, "White")
    canvas.draw_text(str(score2), (400, 40), 40, "White")
            

#creating frame 
f = simplegui.create_frame("PONG", Width, Height)
f.add_button("Restart", gameRestart, 100)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)

# start frame
newgame()
f.start()
