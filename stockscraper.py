import pygame
import requests
from bs4 import BeautifulSoup 

stock = 'Zoom Video Communications TM'

def priceTracker():
    url = 'https://www.marketwatch.com/investing/stock/zm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all('h3', {'class':'intraday__price'})[0].find('bg-quote', {'channel':'/zigman2/quotes/211319643/composite,/zigman2/quotes/211319643/lastsale'}).text
    return price

def priceGain():
    url = 'https://www.marketwatch.com/investing/stock/zm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    gain = soup.find_all('bg-quote', {'channel':'/zigman2/quotes/211319643/composite'})[0].find('span', {'class':'change--point--q'}).text
    return gain     

def priceGainp():
    url = 'https://www.marketwatch.com/investing/stock/zm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    gainp = soup.find_all('bg-quote', {'channel':'/zigman2/quotes/211319643/composite'})[0].find('span', {'class':'change--percent--q'}).text
    return gainp

#start window/pygame
pygame.init()

#create display conditions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#Create surface with screen variable
display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption('Wong\'s First Project')

#create font variable
font = pygame.font.Font('freesansbold.ttf', 25)
tfont = pygame.font.Font('freesansbold.ttf', 45)

#create text variable to be displayed
text = font.render('The current price of this stock is: $' +priceTracker(), True, blue, green)
textone = font.render('The current gain of this stock is $' +priceGain(), True, blue, green)
texttwo = font.render('The current percentage of gain is ' +priceGainp(), True, blue, green)
textthree = font.render(f'The name of this stock is {stock}.', True, blue, green) 
title = tfont.render('Python Stock Scraper by Wong', True, blue, green)

#text rectangle around text
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

textRectone = text.get_rect()
textRectone.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.25)

textRecttwo = text.get_rect()
textRecttwo.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.75)

textRectthree = text.get_rect()
textRectthree.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5)

textRectfour = text.get_rect()
textRectfour.center = (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8)

#start while running loop - all functions process through until canceled
while True:
    #fill surface with color
    display_surface.fill(white)
    #Blit/switch screen and input text and text box
    display_surface.blit(text, textRect)
    display_surface.blit(textone, textRectone)
    display_surface.blit(texttwo, textRecttwo)
    display_surface.blit(textthree, textRectthree)
    display_surface.blit(title, textRectfour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit when told to quit
            pygame.quit()
            #ends program
            quit()

        #updates pygame window with changes
        pygame.display.update()
