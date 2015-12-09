import pygame
import pygame.gfxdraw
import os

import sys

from settings import *
from datetime import datetime
from sendmail import *
import logging

pygame.init()
lcd = pygame.display.set_mode((1360, 768))
pygame.mouse.set_visible(False)
pygame.display.toggle_fullscreen()
background = pygame.Surface(lcd.get_size())
background = background.convert()


def drawitall():
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    background.fill(bcolor)
    apron()
    title()
    logging.debug(timenow() + ' background drawn')
    z = [zone1, zone2, zone3]
    for i in range(1, 4):
        circles(i, green)
        headers(z[i-1], i)
        footers(i)
        complications(i)
        number(i, 0)
        compnumber(i, 0)
        comptext(i, ct[i-1])
    logging.debug(timenow() + ' interface drawn')
    lcd.blit(background, (0, 0))
    pygame.display.flip()


def apron():
    a = pygame.Surface((ax, ay))
    a.fill(acolor)
    background.blit(a, (0, 0))


def circles(pos, color):
    if pos == 1:
        pygame.gfxdraw.aacircle(background, z1x, z1y, ocr + 1, bcolor)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, ocr + 1, bcolor)
        pygame.gfxdraw.aacircle(background, z1x, z1y, ocr, color)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, ocr, color)
        pygame.gfxdraw.aacircle(background, z1x, z1y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, icr, ccolor)
    elif pos == 2:
        pygame.gfxdraw.aacircle(background, z2x, z2y, ocr + 1, bcolor)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, ocr + 1, bcolor)
        pygame.gfxdraw.aacircle(background, z2x, z2y, ocr, color)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, ocr, color)
        pygame.gfxdraw.aacircle(background, z2x, z2y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, icr, ccolor)
    elif pos == 3:
        pygame.gfxdraw.aacircle(background, z3x, z3y, ocr + 1, bcolor)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, ocr + 1, bcolor)
        pygame.gfxdraw.aacircle(background, z3x, z3y, ocr, color)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, ocr, color)
        pygame.gfxdraw.aacircle(background, z3x, z3y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, icr, ccolor)


def innercircle(pos):
    # this updates the number and inner circle without changing color
    if pos == 1:
        pygame.gfxdraw.aacircle(background, z1x, z1y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, icr, ccolor)
    elif pos == 2:
        pygame.gfxdraw.aacircle(background, z2x, z2y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, icr, ccolor)
    elif pos == 3:
        pygame.gfxdraw.aacircle(background, z3x, z3y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, icr, ccolor)


def headers(zone, pos):
    h = hf.render(zone, 1, fcolor)
    hpos = h.get_rect()
    if pos == 1:
        hpos.center = (h1x, hy)
    elif pos == 2:
        hpos.center = (h2x, hy)
    elif pos == 3:
        hpos.center = (h3x, hy)
    background.blit(h, hpos)


def footers(pos):
    f = ff.render('minutes ago', 1, fcolor)
    fpos = f.get_rect()
    if pos == 1:
        fpos.center = (h1x, fy)
    elif pos == 2:
        fpos.center = (h2x, fy)
    elif pos == 3:
        fpos.center = (h3x, fy)
    background.blit(f, fpos)


def title():
    t1 = tf.render('Last', 1, tcolor)
    t2 = tf.render('Travel Path', 1, tcolor)
    t1pos = t1.get_rect()
    t2pos = t2.get_rect()
    t1pos.bottom = ty * 1
    t2pos.top = t1pos.bottom - 5
    t2pos.left = tx
    t1pos.left = tx
    background.blit(t1, t1pos)
    background.blit(t2, t2pos)


def complications(pos):
    if pos == 1:
        pygame.gfxdraw.filled_circle(background, comp1x, compy, compr, acolor)
        pygame.gfxdraw.aacircle(background, comp1x, compy, compr, acolor)
        pygame.gfxdraw.filled_circle(background, comp1x, compy, compr, green)
        pygame.gfxdraw.aacircle(background, comp1x, compy, compr, green)
    elif pos == 2:
        pygame.gfxdraw.filled_circle(background, comp2x, compy, compr, acolor)
        pygame.gfxdraw.aacircle(background, comp2x, compy, compr, acolor)
        pygame.gfxdraw.filled_circle(background, comp2x, compy, compr, yellow)
        pygame.gfxdraw.aacircle(background, comp2x, compy, compr, yellow)
    elif pos == 3:
        pygame.gfxdraw.filled_circle(background, comp3x, compy, compr, acolor)
        pygame.gfxdraw.aacircle(background, comp3x, compy, compr, acolor)
        pygame.gfxdraw.filled_circle(background, comp3x, compy, compr, red)
        pygame.gfxdraw.aacircle(background, comp3x, compy, compr, red)


def number(pos, n):
    n = nf.render(str(n), 1, fcolor)
    npos = n.get_rect()
    if pos == 1:
        npos.center = z1c
    elif pos == 2:
        npos.center = z2c
    elif pos == 3:
        npos.center = z3c
    background.blit(n, npos)


def compnumber(pos, n):
    cn = cf.render(str(n), 1, bcolor)
    cnpos = cn.get_rect()
    if pos == 1:
        cnpos.center = (comp1x, compy)
    elif pos == 2:
        cnpos.center = (comp2x, compy)
    elif pos == 3:
        cnpos.center = (comp3x, compy)
    background.blit(cn, cnpos)


def comptext(pos, text):
    cttt = cff.render(str(text), 1, bcolor)
    ctpos = cttt.get_rect()
    if pos == 1:
        ctpos.center = (c1tx, cty)
    elif pos == 2:
        ctpos.center = (c2tx, cty)
    elif pos == 3:
        ctpos.center = (c3tx, cty)
    background.blit(cttt, ctpos)


def findlasttime(zone):
    with open('logs/travellog.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if row[1].strip() == zone1:
                time1.append(row[0])
            if row[1].strip() == zone2:
                time2.append(row[0])
            if row[1].strip() == zone3:
                time3.append(row[0])

        if zone == 1:
            return max(time1)
        elif zone == 2:
            return max(time2)
        elif zone == 3:
            return max(time3)


def timecomp():
    tt = datetime.now()
    th = str(tt.hour)
    ttm = str(tt.minute).zfill(2)
    complications(1)
    compnumber(1, th + ':' + ttm)
    comptext(1, ct[0])


# function to store PID which is used to kill the task at night
def writepidfile():
    pid = str(os.getpid())
    f = open('logs/pid.txt', 'w')
    f.write(pid)
    f.close()


def avgcomp():  # positions are in complications
    zd1 = []
    with open('logs/travellog.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            a = int(row[2])
            zd1.append(a)

    zd2 = filter(lambda aa: aa != 0, zd1)  # takes out the zeroes
    a = sum(zd2) / len(zd2)
    complications(2)
    compnumber(2, a)
    comptext(2, ct[1])


def vionumber():
    vcount = 0
    with open('logs/violations.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for _ in reader:
            vcount += 1
    return vcount


def viocomp():
    complications(3)
    compnumber(3, vionumber())
    comptext(3, ct[2])


class Violation:
    def __init__(self, time, zone, level, elapsed):
        self.time = time
        self.zone = zone
        self.level = level
        self.elapsed = elapsed
        o = open('logs/violations.csv', 'a')
        ow = csv.writer(o)
        ow.writerow([self.time, self.elapsed, self.zone, self.level])
        o.close()


# interrupts

def interrupt1(channel):
    print"falling edge 2"
    outputFile = open('logs/travellog.csv', 'a')
    now = datetime.now()
    lt = datetime.strptime(findlasttime(1), FMT)
    td = now - lt
    e = int(td.total_seconds() / 60)
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([now, zone1, e, NSN])
    outputFile.close()


def interrupt2(channel):
    print"falling edge 3"
    outputFile = open('logs/travellog.csv', 'a')
    now = datetime.now()
    lt = datetime.strptime(findlasttime(2), FMT)
    td = now - lt
    e = int(td.total_seconds() / 60)
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([now, zone2, e, NSN])
    outputFile.close()


def interrupt3(channel):
    print"falling edge 4"
    outputFile = open('logs/travellog.csv', 'a')
    now = datetime.now()
    lt = datetime.strptime(findlasttime(3), FMT)
    td = now - lt
    e = int(td.total_seconds() / 60)
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([now, zone3, e, NSN])
    outputFile.close()


def interrupt4(channel):
    print"falling edge 5"
    outputFile = open('logs/travellog.csv', 'a')
    now = datetime.now()
    lt = datetime.strptime(findlasttime(4), FMT)
    td = now - lt
    e = int(td.total_seconds() / 60)
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([now, zone1, e, NSN])
    outputFile.close()


def interrupt5(channel):
    print"falling edge 6"
    outputFile = open('logs/travellog.csv', 'a')
    now = datetime.now()
    lt = datetime.strptime(findlasttime(5), FMT)
    td = now - lt
    e = int(td.total_seconds() / 60)
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([now, zone2, e, NSN])
    outputFile.close()


def interrupt6(channel):
    print"falling edge 7"
    outputFile = open('logs/travellog.csv', 'a')
    now = datetime.now()
    lt = datetime.strptime(findlasttime(6), FMT)
    td = now - lt
    e = int(td.total_seconds() / 60)
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([now, zone3, e, NSN])
    outputFile.close()


# EXIT
def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            pygame.quit()
            sys.exit()


# Function to return current time for logging
def timenow():
    a = datetime.datetime.now()
    return a
