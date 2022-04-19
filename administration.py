import pygame as pg
from customer import *
from theme import *

def setup_button(lst):
    tabs = []
    for i in range(len(lst)):
        tabs.append([lst[i], pg.Rect(30, 150+50*i, 200, 50)])
    return tabs
    
def background(window):
    window.fill(BACKGROUND)

def draw_pages(window, active, searchtext, w):
    if active == 1:
        draw_search_box(window, w, searchtext)
        customer_loop(window, searchtext)

def draw_tabs(window, tabs, h, isOpened, active):
    INDENT = 10
    h_font = pg.font.Font(font1, 40)
    tab = pg.font.Font(font4, 20)
    if isOpened:
        header = h_font.render("Nana's Bakery", True, WHITE)
        size = header.get_rect()
        width = INDENT*2+size[2]
        rect = pg.Rect(0, 0, width, 75)
        pg.draw.rect(window, TABS, (0, 0, width, h))
        pg.draw.line(window, WHITE, (10, 75), (width-10, 75))
        window.blit(header, (INDENT, (75-size[3])/2))
    
        for i in range(len(tabs)):
            if active == i:
                pg.draw.rect(window, PINK, (5, tabs[i][1].y+5, width-10, 40))
            text = tab.render(tabs[i][0], True, WHITE)
            window.blit(text, (tabs[i][1].x, tabs[i][1].y+((tabs[i][1].height-text.get_rect()[3])/2)))
        return rect
    else:
        header = h_font.render("N", True, WHITE)
        size = header.get_rect()
        width = size[2]+INDENT*2
        rect = pg.Rect(0, 0, width, 75)
        pg.draw.rect(window, TABS, (0, 0, width, h))
        pg.draw.line(window, WHITE, (10, 75), (width-10, 75))
        window.blit(header, (INDENT, (75-size[3])/2))
        
        rct = tabs[active][1]
        pg.draw.rect(window, PINK, (10, rct.y+10, width-20, 30))
        text = tab.render(tabs[active][0][:3], True, WHITE)
        window.blit(text, ((width-text.get_rect()[2])/2, rct.y+((rct.h-text.get_rect()[3])/2)))
        print()
        return rect
    
def draw_exit(window, button):
    pg.draw.rect(window, RED, button)

def draw_search_box(window, w, text):
    SIZE = 600
    rect = pg.Rect((w-SIZE)/2, 25, SIZE, 50)
    context = pg.font.Font(font4, 20)
    pg.draw.rect(window, GREY, rect, 4)
    text_surface = context.render(text, True, BLACK)
    window.blit(text_surface, (rect.x+((rect.width-text_surface.get_rect()[2])/2), rect.y+((rect.height-text_surface.get_rect()[3])/2)))
   
def main(window):
    running = True
    clock = pg.time.Clock()
    fps = 60
    surface = pg.display.get_surface()
    w, h = surface.get_width(), surface.get_height()
    
    header_button = pg.Rect(0, 0, w, 75)
    lst = ['Dashboard', 'Customers', 'Orders', 'Products', 'Employees',  'Statistics']
    tabs = setup_button(lst)
    exit_button = pg.Rect(w-50, 0, 50, 50)
    
    tabOpened = True
    active = 0
    searchtext = ''
    
    while running:
        clock.tick(fps)
        
        background(window)
        draw_pages(window, active, searchtext, w)
        header_button = draw_tabs(window, tabs, h, tabOpened, active)
        draw_exit(window, exit_button)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in range(len(tabs)):
                    if tabs[i][1].collidepoint(pg.mouse.get_pos()):
                        active = i
                        searchtext = ''
                if exit_button.collidepoint(pg.mouse.get_pos()):
                    running = False
                    break
                
                if header_button.collidepoint(pg.mouse.get_pos()):
                    tabOpened = not tabOpened
            
            if event.type == pg.KEYDOWN:
                if active == 1:
                    if event.key == pg.K_RETURN:
                        searchtext = ''
                    elif event.key == pg.K_BACKSPACE:
                        searchtext = searchtext[:-1]
                    elif event.key == pg.K_SPACE:
                        searchtext += ' '
                    else:
                        if event.unicode.isalnum():
                            searchtext += event.unicode
            
        pg.display.update()
    pg.quit()

def admin_init():
    pg.init()
    WIDTH, HEIGHT = 1920, 1080
    window = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
    pg.display.set_caption('Administration')
    main(window)
    
if __name__ == '__main__':
    admin_init()