#!/usr/bin/env python
import datetime
import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

# Store Info
NSN = '9999'
zone1 = 'Lobby'
zone2 = 'Stockroom'
zone3 = 'Drive Thru'

# Online and Offline Times
offlinetime = datetime.time(22, 0, 0, 0)  # 10pm
onlinetime = datetime.time(4, 0, 0, 0)  # 4am

# Alert Info
# times when circles change colors
yellowLimit = 60
redLimit = 120
# time to wait to send notification
mailtimeLevel1 = 135
mailtimeLevel2 = 240
mailtimeLevel3 = mailtimeLevel2
# minimum time between email alerts in seconds 30min = 1800
tba = 1800
##

# POINTS
#
# apron center
ac = (680, 100)
acx = 680
acy = 100
# circle center and xy
z1c = (228, 515)
z1x = 228
z1y = 515
z2c = (682, 515)
z2x = 682
z2y = 515
z3c = (1132, 515)
z3x = 1132
z3y = 515
# outer circle radius
ocr = 215
# inner circle radius
icr = ocr - 15
# apron
ay = 200
ax = 1360
# header
hy = (z1y - ocr - ay) / 2 + ay
h1x = z1x
h2x = z2x
h3x = z3x
# footer
fy = z1y + ocr - 50  # 50 is offset from bottom of circle
# title
tx = 5
ty = ay / 2
# complications
compr = ay / 2 - 5  # 5 border on top and bottom
comp2x = ax / 3 * 2  # center complication between circle 2 and 3
comp1x = comp2x - compr * 2 - 10
comp3x = comp2x + compr * 2 + 10
compy = acy
# complication text
c1tx = comp1x
c2tx = comp2x
c3tx = comp3x
cty = compy + compr - 25

# ui colors

# circles
ccolor = (222, 222, 222)
# background
bcolor = (236, 240, 241)  # (242,242,242)
# line
lcolor = (50, 50, 50)
# font
fcolor = (21, 21, 21)
red = (192, 57, 43)  # (231, 76, 60)
green = (46, 204, 113)
yellow = (241, 196, 15)
# apron
acolor = (52, 152, 219)
# title
tcolor = bcolor

# fonts(header, footer, title, number, other)
hf = pygame.font.SysFont("freesans", 64)
ff = pygame.font.SysFont("freesans", 32)
tf = pygame.font.SysFont("freesans", 84)
nf = pygame.font.SysFont("freesans", 148)
of = pygame.font.SysFont("freesans", 48)
cf = pygame.font.SysFont("freesans", 64)
cff = pygame.font.SysFont("freesans", 24)

# Complication Names
ct = ["Now", "Average", "Violations"]

# Initalized Variables
time1 = []
time2 = []
time3 = []

lastTime = [0, 0, 0]
ltsec = [0, 0, 0]

FMT = '%Y-%m-%d %H:%M:%S.%f'
