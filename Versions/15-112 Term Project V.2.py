# Created By: Noah Champagne

from cmu_112_graphics import *
import math, copy, random

class Country(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.xCord = 0
        self.yCord = 0
        self.radius = 0
        self.troops = 0
    def loseTroops(self, number):
        self.troops -= number
    def loseBattle(self, other, otherColor):
        self.playerOwner = other
        self.color = otherColor
    def __repr__(self):
        return f'{self.name} owned by {self.owner}'

class Player(object):
    def __init__(self, troopsToPlace, countriesOwned):
        self.troopsToPlace = troopsToPlace
        self.countriesOwned = countriesOwned

def randomizeCountries(app, playerCount):
    countryList = ['Alaska', 'Western Canada', 'Central America',
                    'Eastern United States', 'Greenland', 'Northwest Territory',
                    'Central Canada', 'Eastern Canada', 'Western United States',
                    
                    'Argentina', 'Brazil', 'Peru', 'Venezuela',

                    'Great Britain', 'Iceland', 'Northern Europe',
                    'Scandinavia', 'Southern Europe', 'Ukraine',
                    'Western Europe',
                    
                    'Congo', 'East Africa', 'Egypt',
                    'Madagascar', 'North Africa', 'South Africa',
                    
                    'Afghanistan', 'China', 'India', 'Irkutsk',
                    'Japan', 'Kamchatka', 'Middle East', 'Mongolia',
                    'Siam', 'Siberia', 'Ural', 'Yakutsk'
                    
                    'Eastern Australia', 'Indonesia',
                    'New Guinea', 'Western Australia'     ]
    twoPlayersList = [1, 2] * 21
    random.shuffle(twoPlayersList)
    threePlayersList = [1, 2, 3] * 14
    random.shuffle(threePlayersList)
    playerOptions = [1,2,3,4]
    extraCountries = random.sample(playerOptions, k = 2)
    fourPlayersList = [1, 2, 3, 4] * 10 + extraCountries
    random.shuffle(fourPlayersList)
    countryOwnerList = []
    if playerCount == 2:
        for i in range(len(countryList)):
            countryOwnerList.append((countryList[i],twoPlayersList[i]))
    if playerCount == 3:
        for i in range(len(countryList)):
            countryOwnerList.append((countryList[i],threePlayersList[i]))
    if playerCount == 4:
        for i in range(len(countryList)):
            countryOwnerList.append((countryList[i],fourPlayersList[i]))

    app.countryDictionary = {name: Country(name=name, owner=owner) for name,owner in countryOwnerList}

    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        if countryObject.owner == 1:
            app.player1.countriesOwned.append(countryObject)
        elif countryObject.owner == 2:
            app.player2.countriesOwned.append(countryObject)
        elif countryObject.owner == 3:
            app.player3.countriesOwned.append(countryObject)
        elif countryObject.owner == 4:
            app.player4.countriesOwned.append(countryObject)

    countryCoordinates = [(363, 143, 35), (483, 204, 29), (494, 368, 40),
                            (575, 310, 40), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            
                            (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35),
                            
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35),
                            
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            
                            (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35),     ]

    for index, country in enumerate(app.countryDictionary):
        app.countryDictionary[country].xCord = countryCoordinates[index][0]
        app.countryDictionary[country].yCord = countryCoordinates[index][1]
        app.countryDictionary[country].radius = countryCoordinates[index][2]
        app.countryDictionary[country].troops = 10


#########################
# Player Selection Mode
#########################
def playerSelectionMode_mousePressed(app, event):
    if ((app.middleX - app.boxWidth) < event.x < app.middleX and
        app.topBoxY < event.y < (app.topBoxY + app.boxHeight)):
        app.players = 1
        app.mode = 'gameMode'
        app.player1.troopsToPlace = 45
        randomizeCountries(app, app.players)
    if ((app.middleX - app.boxWidth) < event.x < app.middleX + app.boxWidth and
        app.topBoxY < event.y < (app.topBoxY + app.boxHeight)):
        app.players = 2
        app.mode = 'gameMode'
        app.player1.troopsToPlace = 40
        app.player2.troopsToPlace = 40
        randomizeCountries(app, app.players)
    if ((app.middleX - app.boxWidth) < event.x < app.middleX and
        app.topBoxY + app.boxHeight < event.y < (app.topBoxY + (2 * app.boxHeight))):
        app.players = 3
        app.mode = 'gameMode'
        app.player1.troopsToPlace = 35
        app.player2.troopsToPlace = 35
        app.player3.troopsToPlace = 35
        randomizeCountries(app, app.players)
    if (app.middleX < event.x < app.middleX + app.boxWidth and
        app.topBoxY + app.boxHeight < event.y < (app.topBoxY + (2 * app.boxHeight))):
        app.players = 4
        app.mode = 'gameMode'
        app.player1.troopsToPlace = 30
        app.player2.troopsToPlace = 30
        app.player3.troopsToPlace = 30
        app.player4.troopsToPlace = 30
        randomizeCountries(app, app.players)

def playerSelectionMode_redrawAll(app, canvas):
    font1 = 'Arial 82 bold'
    font2 = 'Arial 64 bold'
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.middleX, app.middleY,
                        image=ImageTk.PhotoImage(app.scaledTitleScreen))
    canvas.create_text(app.middleX, app.middleY * .25,
                        text = 'Select Player Count', font = font1)
    canvas.create_rectangle(app.middleX - app.boxWidth, app.topBoxY,
                            app.middleX, app.topBoxY + app.boxHeight,
                            width = 10, fill = 'grey', outline = 'black')
    canvas.create_rectangle(app.middleX, app.topBoxY,
                            app.middleX + app.boxWidth, app.topBoxY + app.boxHeight,
                            width = 10, fill = 'grey', outline = 'black')
    canvas.create_rectangle(app.middleX - app.boxWidth, app.topBoxY + app.boxHeight,
                            app.middleX, app.topBoxY + (2 * app.boxHeight),
                            width = 10, fill = 'grey', outline = 'black')
    canvas.create_rectangle(app.middleX, app.topBoxY + app.boxHeight,
                            app.middleX + app.boxWidth, app.topBoxY + (2 * app.boxHeight),
                            width = 10, fill = 'grey', outline = 'black')
    canvas.create_text(app.middleX - (app.boxWidth * .5),
                        app.topBoxY + (app.boxHeight * .5),
                        text = '1', font = font2)
    canvas.create_text(app.middleX + (app.boxWidth * .5),
                        app.topBoxY + (app.boxHeight * .5),
                        text = '2', font = font2)
    canvas.create_text(app.middleX - (app.boxWidth * .5),
                        app.topBoxY + (app.boxHeight * 1.5),
                        text = '3', font = font2)
    canvas.create_text(app.middleX + (app.boxWidth * .5),
                        app.topBoxY + (app.boxHeight * 1.5),
                        text = '4', font = font2)

#########################
# Game Mode
#########################
def gameMode_keyPressed(app, event):
    pass

def countryPressed(app, mouseX, mouseY, countryLevel):
    if countryLevel == 1:
        for country in app.countryDictionary:
            if ((mouseX - app.countryDictionary[country].xCord) ** 2 + (mouseY - app.countryDictionary[country].yCord) ** 2) ** .5 < app.countryDictionary[country].radius:
                app.currentCountry = app.countryDictionary[country]
                app.countryDictionary[country].troops += 1
                return True
    if countryLevel == 2:
        for country in app.countryDictionary:
            if ((mouseX - app.countryDictionary[country].xCord) ** 2 + (mouseY - app.countryDictionary[country].yCord) ** 2) ** .5 < app.countryDictionary[country].radius:
                app.secondCountry = app.countryDictionary[country]
                app.countryDictionary[country].troops += 1
                return True
    return False

def gameMode_mousePressed(app, event):
    if app.currentCountry == None:
        if countryPressed(app, event.x,event.y, 1):
            print (app.currentCountry, app.secondCountry)
            print (app.currentCountry.troops)
    # if app.secondCountry == None:
    if countryPressed(app, event.x,event.y, 2):
        print (app.currentCountry, app.secondCountry)
            # print (app.currentCountry.troops, app.secondCountry.troops)

def gameMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.width * .59, app.height * .5,
                        image=ImageTk.PhotoImage(app.scaledMap))
    countryList = ['Alaska', 'Western Canada', 'Central America',
                    'Eastern United States', 'Greenland', 'Northwest Territory',
                    'Central Canada', 'Eastern Canada', 'Western United States',
                    
                    'Argentina', 'Brazil', 'Peru', 'Venezuela',

                    'Great Britain', 'Iceland', 'Northern Europe',
                    'Scandinavia', 'Southern Europe', 'Ukraine',
                    'Western Europe',
                    
                    'Congo', 'East Africa', 'Egypt',
                    'Madagascar', 'North Africa', 'South Africa',
                    
                    'Afghanistan', 'China', 'India', 'Irkutsk',
                    'Japan', 'Kamchatka', 'Middle East', 'Mongolia',
                    'Siam', 'Siberia', 'Ural', 'Yakutsk'
                    
                    'Eastern Australia', 'Indonesia',
                    'New Guinea', 'Western Australia'     ]
    x1 = 1177
    y1 = 217
    r = 29
    canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r)
    countryCoordinates = [(363, 143, 35), (483, 204, 29), (494, 368, 40),
                            (575, 310, 40), (720, 95, 70), (474, 147, 26),
                            (550, 206, 28), (633, 215, 32), (475, 272, 37),
                            
                            (566, 646, 60), (639, 506, 56),
                            (560, 540, 23), (535, 431, 26),
                            
                            (761, 233, 33), (762, 167, 20), (828, 248, 22),
                            (830, 159, 52), (833, 318, 33), (943, 187, 60),
                            (758, 308, 43),
                            
                            (845, 546, 30), (896, 488, 39), (855, 395, 38),
                            (936, 634, 32), (769, 469, 63), (836, 655, 58),
                            
                            (998, 292, 45), (1108, 329, 43), (1062, 440, 64),
                            (1177, 217, 29), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35), (363, 143, 35),
                            
                            (363, 143, 35), (363, 143, 35),
                            (363, 143, 35), (363, 143, 35),     ]
    
    # for x1, y1, r in countryCoordinates:
    #     canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r)
    
#########################
# Main App
#########################
def appStarted(app):
    app.mode = 'playerSelectionMode'
    #########################
    # Player Selection Mode
    #########################
    titleScreenUrl = 'https://steamcdn-a.akamaihd.net/steam/apps/1128810/capsule_616x353.jpg?t=1604115364'
    app.titleScreen = app.loadImage(titleScreenUrl)
    app.imageWidth, app.imageHeight = app.titleScreen.size
    titleScreeenScaleFactor = app.height / app.imageHeight
    app.scaledTitleScreen = app.scaleImage(app.titleScreen, titleScreeenScaleFactor)
    app.middleX = app.width * .5
    app.middleY = app.height * .5
    app.boxWidth = app.width * .20
    app.boxHeight = app.height * .25
    app.topBoxY = .43 * app.height
    app.players = 0
    #########################
    # Game Mode
    #########################
        #########################
        # Game Mode - Images
        #########################
    mapUrl = 'https://i.stack.imgur.com/sKx7n.jpg'
    app.map = app.loadImage(mapUrl)
    app.mapWidth, app.mapHeight = app.map.size
    mapScaleFactor = min(app.height / app.mapHeight, app.width / app.mapWidth)
    app.scaledMap = app.scaleImage(app.map, mapScaleFactor)
        #########################
        # Game Mode - Mechanics
        #########################
    app.player1 = Player(0, [])
    app.player2 = Player(0, [])
    app.player3 = Player(0, [])
    app.player4 = Player(0, [])
    app.countryDictionary = {}
    app.currentCountry = None
    app.secondCountry = None

def runRisk():
    width = 1500
    height = 750
    runApp(width=width, height=height)

runRisk()