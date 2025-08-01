import math
import random
import time
import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("클리커")

RETRY_BUTTON_WIDTH = 200
RETRY_BUTTON_HEIGHT = 50
RETRY_BUTTON_COLOR = (0, 255, 0)
RETRY_BUTTON_TEXT = "Retry"
RETRY_BUTTON_FONT = pygame.font.SysFont("constantia", 36)

#colors
BG = (153, 255, 255)
BLACK = (0, 0, 0)
win.fill(BG)

font = pygame.font.SysFont('constantia', 36)
title_font = pygame.font.SysFont('constantia', 72)

#buttons
start_text = pygame.image.load('startbutton.png')
game_title_rect = pygame.Rect(379, 100, 200, 50)
#start_button = pygame.Rect(379, 200, 200, 50)
start_button = start_text
exit_button = pygame.Rect(379, 400, 200, 50)

running = True
while running:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                #if start_button.collidepoint(mouse_pos):
                    #running = False
                if 382 <= mouse[0] <= 582 and 210 <= mouse[1] <= 310:
                    running = False
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()

    #pygame.draw.rect(win, BLACK, start_button)
    pygame.draw.rect(win, BLACK, exit_button)   
    pygame.draw.rect(win, BG, game_title_rect)

    #start_text = font.render("Start", True, "white")
    
    exit_text = font.render("Exit", True, "white")
    game_title_text = title_font.render("CLICKER", True, "black")

    title_x = game_title_rect.centerx - game_title_text.get_width() / 2
    title_y = game_title_rect.centery - game_title_text.get_height() / 2


    win.blit(start_text, (382, 210))
    win.blit(exit_text, (450, 410))
    win.blit(game_title_text, (title_x, title_y))

    pygame.display.flip()

#MAIN GAME CODE
TARGET_INCREMENT = 850 #in miliseconds
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING  = 30

BG_COLOR = (153, 255, 255)
LIVES = 3
TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("constantia", 24)

class Target:
    #we can adjust here
    MAX_SIZE = 25
    GROWTH_RATE = 0.5
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

#making the circle targets
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide (self, x, y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size

def draw(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)
 

def format_time(secs): #take in the number of seconds we have, return to us a string that contains the number of miliseconds, seconds, and minutes in a nice format
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} targets/s", 1, "black")

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")

    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", 1, "black")

    win.blit(time_label, (60, 5))
    win.blit(speed_label, (300, 5))
    win.blit(hits_label, (600, 5))
    win.blit(lives_label, (800, 5))

#retry button rectangle
retry_button = pygame.Rect((390, 600, 200, 50))

def draw_retry_button(win):
    pygame.draw.rect(win, RETRY_BUTTON_COLOR, retry_button)
    retry_text = RETRY_BUTTON_FONT.render(RETRY_BUTTON_TEXT, True, "black")
    win.blit(retry_text, (retry_button.x + 60, 600))


def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} targets/s", 1, "black")

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")

    if clicks == 0:
        accuracy = 0
    else:
        accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()
    draw_retry_button(win)

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    main() #restarting the game

def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time() #track how much time has elapsed since we started, giving us the total duration of the round we're currently in

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT) #trigger TARGET_EVENT every TARGET_INCREMENT miliseconds

    while run:
        clock.tick(120) # regulates the speed at which this while loop runs
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_pos): #splat operator
                targets.remove(target)
                targets_pressed += 1

        if misses >= LIVES:
            end_screen(win, elapsed_time, targets_pressed, clicks)

        draw(win, targets)
        draw_top_bar(win, elapsed_time, targets_pressed, misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()