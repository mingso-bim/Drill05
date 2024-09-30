from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
dog = load_image('dog.png')

def handle_events():
    global running, dirX, dirY
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                print('r up')
            elif event.key == SDLK_LEFT:
                dirX += 1
                print('l up')
            elif event.key == SDLK_UP:
                dirY -= 1
                print('u up')
            elif event.key == SDLK_DOWN:
                dirY += 1
                print('d up')


running = True
x = 800 // 2
y = 600 // 2
frame = 0
dirX, dirY = 0, 0
motion = 0

while running:
    clear_canvas()
    background.draw(400, 300)
    if dirX < 0:        # 왼쪽
        motion = 2
    elif dirX > 0:      # 오른쪽
        motion = 1
    elif dirY < 0:      # 아래
        motion = 3
    elif dirY > 0:      # 위
        motion = 0
    elif dirX == 0 and dirY == 0:
        motion = 3

    print('X', dirX)
    print('Y', dirY)
    dog.clip_draw(frame * 256, motion * 256, 256, 256, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += dirX * 5
    y += dirY * 5
    delay(0.05)

# fill here


close_canvas()