import simpleguitk as simplegui
import random

w, h = 600, 400
tux_r = 20
pad_w = 8
pad_h = 80

def tux_spawn(right):
	global tux_pos, tux_vel
	tux_pos = [0,0]
	tux_vel = [0,0]
	tux_pos[0] = w/2
	tux_pos[1] = h/2
	if right:
		tux_vel[0] = random.randrange(2, 4)
	else:
		tux_vel[0] = -random.randrange(2, 4)
	tux_vel[1] = -random.randrange(1, 3)
	
def start():
	global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
	global score1, score2
	tux_spawn(random.choice([True, False]))
	score1, score2 = 0,0
	paddle1_vel, paddle2_vel = 0,0
	paddle1_pos, paddle2_pos = h/2, h/2

def draw(canvas):
	global score1, score2, paddle1_pos, paddle2_pos, tux_pos, tux_vel
	if paddle1_pos > (h - (pad_h/2)):
		paddle_pos = (h - (pad_h/2))
	elif paddle1_pos < (pad_h/2):
		paddle1_pos = (pad_h/2)
	else:
		paddle1_pos += paddle1_vel
	if paddle2_pos > (h - (pad_h/2)):
		paddle2_pos = (h - (pad_h/2))
	elif paddle2_pos < (pad_h/2):
		paddle2_pos = (pad_h/2)
	else:
		paddle2_pos += paddle2_vel
	canvas.draw_line([w / 2, 0], [w / 2, h], 4, 'Green')
	canvas.draw_line([(pad_w/2), paddle1_pos + (pad_h/2)], [(pad_w/2), paddle1_pos - (pad_h/2)], pad_w, 'Green')
	canvas.draw_line([w - (pad_w/2), paddle2_pos + (pad_h/2)], [w - (pad_w/2), paddle2_pos - (pad_h/2)], pad_w, 'Green')
	tux_pos[0] += tux_vel[0]
	tux_pos[1] += tux_vel[1]
	if tux_pos[1] <= tux_r or tux_pos[1] >= h - tux_r:
		tux_vel[1] = -tux_vel[1]*1.1
	if tux_pos[0] <= pad_w + tux_r:
		if (paddle1_pos + (pad_h/2)) >= tux_pos[1] >= (paddle1_pos - (pad_h/2)):
			tux_vel[0] = -tux_vel[0]*1.1
			tux_vel[1] *= 1.1
		else:
			score2 += 1
			tux_spawn(True)
	elif tux_pos[0] >= w - pad_w - tux_r:
		if (paddle2_pos + (pad_h/2)) >= tux_pos[1] >= (paddle2_pos-(pad_h/2)):
			tux_vel[0] = -tux_vel[0]
			tux_vel[1] *= 1.1
		else:
			score1 += 1
			tux_spawn(False)
	canvas.draw_image(tux, (265/2, 314/2), (265, 314), tux_pos, (45, 45))
	canvas.draw_text(str(score1), [150, 100], 30, 'Green')
	canvas.draw_text(str(score2), [450, 100], 30, 'Green')
	
def keydown(key):
	global paddle1_vel, paddle2_vel
	acc = 3
	if key == simplegui.KEY_MAP['left']:
		paddle1_vel -= acc
	elif key == simplegui.KEY_MAP['right']:
		paddle1_vel += acc
	elif key == simplegui.KEY_MAP['down']:
		paddle2_vel += acc
	elif key == simplegui.KEY_MAP['up']:
		paddle2_vel -= acc
		
def keyup(key):
	global paddle1_vel, paddle2_vel
	acc = 0
	if key == simplegui.KEY_MAP['left']:
		paddle1_vel = acc
	elif key == simplegui.KEY_MAP['right']:
		paddle1_vel = acc
	elif key == simplegui.KEY_MAP['down']:
		paddle2_vel = acc
	elif key == simplegui.KEY_MAP['up']:
		paddle2_vel = acc

frame = simplegui.create_frame('Tux for Two', w, h)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
tux = simplegui.load_image('http://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png')

start()
frame.start()
