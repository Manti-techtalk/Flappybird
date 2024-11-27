# A Flappy Bird game.
import intrographics
import random

# This function starts the game.
def click(x, y):
    if text.occupies(x, y):
        text.rewrite("")
        window.on_key_press(press)
        window.on_timer(30, fast_timer)
        window.on_timer(3000, slow_timer)
        

# This function creates a new set of pipes.
def slow_timer():
    top_height = random.randint(50, 200)
    bottom_y = top_height + 150
    bottom_height = window.bottom- bottom_y

    top = window.rectangle(window.right, window.top, 50, top_height)
    top.fill("green")
    top.group("pipes")

    bottom = window.rectangle(window.right, bottom_y, 50, bottom_height)
    bottom.fill("green")
    bottom.group("pipes")

# This function moves the bird and the pipes.
def fast_timer():
    bird.move(0, bird.dy)
    bird.dy = bird.dy + 0.1  # Gravity effect

    for pipe in window.all("pipes"):
        pipe.move(-3, 0)

        # Get rid of pipes that leave the window.
        if pipe.right <= window.left:
            window.remove(pipe)

        # End the game when the bird hits a pipe.
        if pipe.overlaps(bird):
            window.remove(bird)
            text.rewrite("Game over!")
            window.off_timer(slow_timer)

# This function refreshes the bird's direction.
def press(key):
    if key == "space":
        bird.dy = -3

# Window setup area.
window = intrographics.window(600, 400)

text = window.text(50, 50, "Click here to start...")
bird = window.image(200, 200, "bird.png")
bird.dy = 0

window.on_left_click(click)
window.open()