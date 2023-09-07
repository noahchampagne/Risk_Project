# Created By: Noah Champagne

from cmu_112_graphics import *
import math, copy, random

def gameMode_appStarted(app):
    url1 = 'https://cdn.pixabay.com/photo/2019/06/30/20/55/board-of-risk-4308773_1280.png'
    url2 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Risk_board.svg/750px-Risk_board.svg.png'
    url3 = 'https://i.stack.imgur.com/sKx7n.jpg'
    url4 = 'https://w7.pngwing.com/pngs/995/11/png-transparent-risk-playstation-4-board-game-strategy-game-risk-miscellaneous-game-angle.png'
    # ############
    # app.image1 = app.loadImage(url1)
    # app.scaledImage1 = app.scaleImage(app.image1, .88)
    # ############
    app.image2 = app.loadImage(url2)
    app.imageWidth, app.imageHeight = app.image2.size
    scaleFactor = app.height / app.imageHeight
    app.scaledImage2 = app.scaleImage(app.image2, scaleFactor)
    # ############
    # app.image3 = app.loadImage(url3)
    # app.imageWidth, app.imageHeight = app.image3.size
    # scaleFactor = (app.height / app.imageHeight)
    # app.scaledImage3 = app.scaleImage(app.image3, scaleFactor)
    ############

    # img = Image.open(url4)
    # rgba = img.convert(“RGBA”)
    # datas = rgba.getdata()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ RISK TITLE IMAGE ~~~~~~~~~~~~~~~~~~~~~~~~~
    # app.image1 = app.loadImage(url4)
    # app.image1 = app.image1.convert('RGB')
    # app.image2 = Image.new(mode='RGB', size=app.image1.size)
    # for x in range(app.image2.width):
    #     for y in range(app.image2.height):
    #         r,g,b = app.image1.getpixel((x,y))
    #         app.image2.putpixel((x,y),(r,0,0))
    ############
    app.players = 0

def gameMode_keyPressed(app, event, country):
    xCord = event.x
    yCord = event.y
    distance = ((country.xCord - xCord) + (country.yCord - yCord)) ** .5
    # if distance <

def gameMode_mousePressed(app, event):
    pass

def gameMode_timerFired(app):
    pass

def gameMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(875, app.height // 2, image=ImageTk.PhotoImage(app.scaledImage3))
    # canvas.create_image(875, app.height // 8, image=ImageTk.PhotoImage(app.image2))

def appStarted(app):
    app.mode = 'playerSelectionMode'
    titleScreenUrl = 'https://steamcdn-a.akamaihd.net/steam/apps/1128810/capsule_616x353.jpg?t=1604115364'
    app.titleScreen = app.loadImage(titleScreenUrl)
    app.imageWidth, app.imageHeight = app.titleScreen.size
    scaleFactor = app.height / app.imageHeight
    app.scaledTitleScreen = app.scaleImage(app.titleScreen, scaleFactor)


def runRisk():
    # runApp()              1250 853
    runApp(width=1500, height=750)
    # runApp(width=1126, height=750)

# runRisk()

population = [1,2,3,4,5]
# print (random.sample(population, k = 2, counts=None))
# print (random.choices(population, k=3))

# playerOptions = [1,2,3,4]
# extraCountries = random.sample(playerOptions, k = 2)
# FourPlayersList = [1, 2, 3, 4] * 10 + extraCountries
# print(FourPlayersList)
# fourShuffled = random.shuffle(FourPlayersList)
# print(FourPlayersList)

class Country(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
    def loseTroops(self, number):
        self.troops -= number
    def loseBattle(self, other, otherColor):
        self.playerOwner = other
        self.color = otherColor
    def __repr__(self):
        return f'{self.name} owned by {self.owner}'

def randomizeCountries(playerCount):
    countryList = ['Alaska', 'Western Canada', 'Central America',
                    'Eastern United States', 'Greenland', 'Northwest Territory',
                    'Central Canada', 'Eastern Canada', 'Western United States',

                    'Argentina', 'Brazil', 'Peru', 'Venezuela',

                    'Great Britain', 'Iceland', 'Northern Europe',
                    'Scandinavia', 'Southern Europe', 'Ukraine',
                    'Western Europe',

                    'Congo', 'East Africa', 'Egypt', 'Madagascar',
                    'North Africa', 'South Africa',

                    'Afghanistan', 'China', 'India', 'Irkutsk', 'Japan',
                    'Kamchatka', 'Middle East', 'Mongolia', 'Siam', 'Siberia',
                    'Ural', 'Yakutsk'

                    'Eastern Australia', 'Indonesia', 'New Guinea',
                    'Western Australia'     ]
    twoPlayersList = [1, 2] * 21
    random.shuffle(twoPlayersList)
    threePlayersList = [1, 2, 3] * 14
    random.shuffle(threePlayersList)
    playerOptions = [1,2,3,4]
    extraCountries = random.sample(playerOptions, k = 2)
    fourPlayersList = [1, 2, 3, 4] * 10 + extraCountries
    random.shuffle(fourPlayersList)
    # for index in range(len(countryList)):
    #     countryList[index] = Country(countryList[index], FourPlayersList[index])
    # print (countryList)
    # print(countryList)

    # countryObjectList = []
    # for index, country in enumerate(countryList):
    #     # print(country)
    #     country = Country(countryList[index], FourPlayersList[index])
    #     countryObjectList.append(country)
    #     # print(countryname.owner)
    #     # input()
    # print(countryObjectList)
    # print(Alaska)
    # input()
    # print (countryList)
    # print(Alaska.name)
    # countryDictionary = {name: Country(name=name, owner=owner) for name in countryList}
    # print (countryDictionary)

    countryOwnerList = []
    for i in range(len(countryList)):
            countryOwnerList.append((countryList[i],fourPlayersList[i]))
    countryDictionary = {name: Country(name=name, owner=owner) for name,owner in countryOwnerList}
    print(countryDictionary)
    print(countryDictionary['Alaska'].owner)
randomizeCountries(1)