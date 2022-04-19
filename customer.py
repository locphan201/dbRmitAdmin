import pygame as pg
from theme import *

def list_of_customer():
    customers = []
    #connect to database
    customers.append(['Phan Vinh Loc', 's3938497@rmit.edu.vn', '9876543210'])
    customers.append(['Loc Vinh Phan', 'u1275898@utah.edu', '0123456789'])
    customers.append(['Evzenie Deepali Sugimoto', 's2757261@rmit.edu.vn', '0123456789'])
    customers.append(['Taras Laurentino Knezevic', 's4932372@rmit.edu.vn', '0123456789'])
    customers.append(['Evangeline Whiteley', 's8524900@rmit.edu.vn', '0123456789'])
    customers.append(['Chase Clemons', 's6362726@rmit.edu.vn', '0123456789'])
    customers.append(['Billie Mcmanus', 's7378230@rmit.edu.vn', '0123456789'])
    customers.append(['Princess Curry', 's5621585@rmit.edu.vn', '0123456789'])
    customers.append(['Jett Ramsey', 's2892118@rmit.edu.vn', '0123456789'])
    customers.append(['Angelica Gibbons', 's6902984@rmit.edu.vn', '0123456789'])
    customers.append(['Maximus Searle', 's7408579@rmit.edu.vn', '0123456789'])
    customers.append(['Rome Hanson', 's7969719@rmit.edu.vn', '0123456789'])
    customers.append(['Tahir Whelan', 's2759797@rmit.edu.vn', '0123456789'])
    customers.append(['Kayleigh Chavez', 's1011865@rmit.edu.vn', '0123456789'])
    customers.append(['Rayhan Lucas', 's2038123@rmit.edu.vn', '0123456789'])
    customers.append(['Wiktor Irvine', 's5761078@rmit.edu.vn', '0123456789'])
    return customers

def search(info, customers, result):
    info = info.lower()
    for i in range(len(customers)):
        for j in range(len(customers[i])):
            if info in customers[i][j].lower():
                result.append(customers[i])
                break
    return result

def draw_customers(window, customers):
    paragraph = pg.font.Font(font4, 20)
    end = len(customers)
    if 15 < end:
        end = 15
    for i in range(end):
        rect = pg.Rect(150, 100+50*i, 400, 50)
        email = paragraph.render(customers[i][0], True, BLACK)
        window.blit(email, (rect.x, rect.y+((rect.height-email.get_rect()[3])/2)))
        name = paragraph.render(customers[i][1], True, BLACK)
        window.blit(name, (rect.x+400, rect.y+((rect.height-name.get_rect()[3])/2)))
        
def customer_loop(window, searchtext):
    customers = list_of_customer()
    result = []
    if searchtext == '':
        result = []
        draw_customers(window, customers)
    else:
        result = search(searchtext, customers, result)
        draw_customers(window, result)