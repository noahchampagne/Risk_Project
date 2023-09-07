# Created By: Noah Champagne

from cmu_112_graphics import *
import math, copy, random

class Country(object):
    def __init__(self, name):
        self.name = name
        self.xCord = 0
        self.yCord = 0
        self.radius = 0
        self.owner = None
        self.troops = 1
        self.continent = None
    def __repr__(self):
        return f'{self.name} owned by {self.owner}'

class Player(object):
    def __init__(self, playerNum, troopsToPlace, countriesOwned):
        self.troopsToPlace = troopsToPlace
        self.countriesOwned = countriesOwned
        self.playerNum = playerNum
    def __repr__(self):
        return f'Player {self.playerNum}'

def giveCountriesOwners(app, playerList):
    for index, country in enumerate(app.countryDictionary):
        app.countryDictionary[country].owner = playerList[index]

def randomizeCountries(app, playerCount):
    #Creates randomized list of players to later assign to countries
    twoPlayersList = [1, 2] * 21
    random.shuffle(twoPlayersList)
    threePlayersList = [1, 2, 3] * 14
    random.shuffle(threePlayersList)
    playerOptions = [1,2,3,4]
    extraCountries = random.sample(playerOptions, k = 2)
    fourPlayersList = [1, 2, 3, 4] * 10 + extraCountries
    random.shuffle(fourPlayersList)

    #Assigns an initial owner to each country
    if playerCount == 1:
        pass
    elif playerCount == 2:
        giveCountriesOwners(app, twoPlayersList)
    elif playerCount == 3:
        giveCountriesOwners(app, threePlayersList)
    elif playerCount == 4:
        giveCountriesOwners(app, fourPlayersList)
        
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

    
    #Sets the initial amount of troops a player has to place
    app.player1.troopsToPlace -= len(app.player1.countriesOwned)
    app.player2.troopsToPlace -= len(app.player2.countriesOwned)
    app.player3.troopsToPlace -= len(app.player3.countriesOwned)
    app.player4.troopsToPlace -= len(app.player4.countriesOwned)

def troopsToGive(app):
    northAmericaCount = 0
    southAmericaCount = 0
    europeCount = 0
    africaCount = 0
    asiaCount = 0
    australiaCount = 0
    possibleTroops = (len(app.currentPlayer.countriesOwned) // 3)
    for country in app.currentPlayer.countriesOwned:
        if country.continent == 'North America':
            northAmericaCount += 1
        elif country.continent == 'South America':
            southAmericaCount += 1
        elif country.continent == 'Europe':
            europeCount += 1
        elif country.continent == 'Africa':
            africaCount += 1
        elif country.continent == 'Asia':
            asiaCount += 1
        elif country.continent == 'Australia':
            australiaCount += 1
    if northAmericaCount == 9:
        possibleTroops += 5
    if southAmericaCount == 4:
        possibleTroops += 2
    if europeCount == 7:
        possibleTroops += 5
    if africaCount == 6:
        possibleTroops += 3
    if asiaCount == 12:
        possibleTroops += 7
    if australiaCount == 4:
        possibleTroops += 2
    app.currentPlayer.troopsToPlace = (max(3, possibleTroops))

#########################
# Player Selection Mode
#########################
def playerSelectionMode_mousePressed(app, event):
    if ((app.middleX - app.boxWidth) < event.x < app.middleX and
        app.topBoxY < event.y < (app.topBoxY + app.boxHeight)):
        app.players = 1
        app.mode = 'inititalPhase'
        app.player1.troopsToPlace = 45
        randomizeCountries(app, app.players)
    if ((app.middleX - app.boxWidth) < event.x < app.middleX + app.boxWidth and
        app.topBoxY < event.y < (app.topBoxY + app.boxHeight)):
        app.players = 2
        app.mode = 'inititalPhase'
        app.player1.troopsToPlace = 25
        app.player2.troopsToPlace = 25
        randomizeCountries(app, app.players)
    if ((app.middleX - app.boxWidth) < event.x < app.middleX and
        app.topBoxY + app.boxHeight < event.y < (app.topBoxY + (2 * app.boxHeight))):
        app.players = 3
        app.mode = 'inititalPhase'
        app.player1.troopsToPlace = 35
        app.player2.troopsToPlace = 35
        app.player3.troopsToPlace = 35
        randomizeCountries(app, app.players)
    if (app.middleX < event.x < app.middleX + app.boxWidth and
        app.topBoxY + app.boxHeight < event.y < (app.topBoxY + (2 * app.boxHeight))):
        app.players = 4
        app.mode = 'inititalPhase'
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
# Initial Placement Mode
#########################
def inititalPhase_keyPressed(app, event):
    pass

def CountryPressed(app, mouseX, mouseY):
    for country in app.currentPlayer.countriesOwned:
        if ((((mouseX - country.xCord) ** 2 +
            (mouseY - country.yCord) ** 2) ** .5)
            < country.radius):
            app.currentCountry = country
            return True
    return False

def inititalPhase_mousePressed(app, event):
    if CountryPressed(app, event.x,event.y):
        app.currentCountry.troops += 1
        app.currentPlayer.troopsToPlace -= 1
        app.playerIndex += 1
        app.currentPlayer = app.playerList[(app.playerIndex % 4)]
        if app.currentPlayer.troopsToPlace == 0:
            app.playerIndex += 1
            app.currentPlayer = app.playerList[(app.playerIndex % 4)]
            if app.currentPlayer.troopsToPlace == 0:
                app.playerIndex += 1
                app.currentPlayer = app.playerList[(app.playerIndex % 4)]
                if (app.player1.troopsToPlace + app.player2.troopsToPlace +
                app.player3.troopsToPlace + app.player4.troopsToPlace) == 0:
                    app.mode = 'stage1'
                    app.playerIndex = random.randrange(4)
                    app.currentPlayer = app.playerList[(app.playerIndex % app.players)]
                    troopsToGive(app)
                    
def inititalPhase_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.width * .59, app.height * .5,
                        image=ImageTk.PhotoImage(app.scaledMap))
    
    #Draws the country's UI circles
    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        xCord = countryObject.xCord
        yCord = countryObject.yCord
        radius = countryObject.radius
        colorListIndex = countryObject.owner - 1
        canvas.create_oval( xCord - radius, yCord - radius,
                            xCord + radius, yCord + radius,
                            outline = app.colorList[colorListIndex], width = 3,
                            fill = app.colorList[colorListIndex])
        canvas.create_text( xCord, yCord, fill = 'white',
                            text = f'Troops: {countryObject.troops}')

    #Displays each player's troops to place
    for i in range(app.players):
        if i == 0:
            canvas.create_text(100, 100, fill = 'white', 
            text = f'Player 1 has {app.player1.troopsToPlace} troops to place')
        elif i == 1:
            canvas.create_text(100, 120, fill = 'white', 
            text = f'Player 2 has {app.player2.troopsToPlace} troops to place')
        elif i == 2:
            canvas.create_text(100, 140, fill = 'white', 
            text = f'Player 3 has {app.player3.troopsToPlace} troops to place')
        elif i == 3:
            canvas.create_text(100, 160, fill = 'white', 
            text = f'Player 4 has {app.player4.troopsToPlace} troops to place')

    #Displays who's turn it is
    canvas.create_text(130, 50, font = 'Arial 32',
                        fill = app.colorList[app.playerIndex % app.players],
                        text = f"Player {(app.playerIndex % app.players) + 1}'s Turn")
    
#########################
# Stage 1
#########################
def stage1_keyPressed(app, event):
    pass

def stage1_mousePressed(app, event):
    if CountryPressed(app, event.x,event.y):
        app.currentCountry.troops += 1
        app.currentPlayer.troopsToPlace -= 1
        if app.currentPlayer.troopsToPlace == 0:
            app.currentCountry = None
            app.mode = 'stage2'

def stage1_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.width * .59, app.height * .5,
                        image=ImageTk.PhotoImage(app.scaledMap))
    
    #Draws the country's UI circles
    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        xCord = countryObject.xCord
        yCord = countryObject.yCord
        radius = countryObject.radius
        colorListIndex = countryObject.owner - 1
        canvas.create_oval( xCord - radius, yCord - radius,
                            xCord + radius, yCord + radius,
                            outline = app.colorList[colorListIndex], width = 3,
                            fill = app.colorList[colorListIndex])
        canvas.create_text( xCord, yCord, fill = 'white',
                            text = f'Troops: {countryObject.troops}')

    #Displays who's turn it is
    canvas.create_text(130, 50, font = 'Arial 32',
                        fill = app.colorList[app.playerIndex % app.players],
                        text = f"Player {(app.playerIndex % app.players) + 1}'s Turn")

    #Displays each player's troops to place
    for i in range(app.players):
        if i == 0:
            canvas.create_text(100, 100, fill = 'white', 
            text = f'Player 1 has {app.player1.troopsToPlace} troops to place')
        elif i == 1:
            canvas.create_text(100, 120, fill = 'white', 
            text = f'Player 2 has {app.player2.troopsToPlace} troops to place')
        elif i == 2:
            canvas.create_text(100, 140, fill = 'white', 
            text = f'Player 3 has {app.player3.troopsToPlace} troops to place')
        elif i == 3:
            canvas.create_text(100, 160, fill = 'white', 
            text = f'Player 4 has {app.player4.troopsToPlace} troops to place')

#########################
# Stage 2 - Pick Attacking/Defending Countries
#########################
def stage2_keyPressed(app, event):
    if (event.key).isdigit():
        app.migratingTroops = app.migratingTroops + event.key
        app.illegalTroopCount = False
    elif app.typingMove == True and event.key == 'Delete' and len(app.migratingTroops) > 0:
        app.migratingTroops = app.migratingTroops[:-1]
        app.illegalTroopCount = False
    elif event.key == 'Enter':
        if (app.migratingTroops == '' or 
                int(app.migratingTroops) > app.currentCountry.troops - 1):
            app.migratingTroops = ''
            app.illegalTroopCount = True
        else:
            app.currentCountry.troops -= int(app.migratingTroops)
            app.opponentCountry.troops += int(app.migratingTroops)
            app.migratingTroops = ''
            app.currentCountry = None
            app.opponentCountry = None
            app.attackOver = False

def myCountryPressed(app, mouseX, mouseY):
    for country in app.currentPlayer.countriesOwned:
        if ((((mouseX - country.xCord) ** 2 +
            (mouseY - country.yCord) ** 2) ** .5)
            < country.radius and country.troops > 1):
            app.currentCountry = country
            app.opponentCountry = None
            app.attackOption = False
            return True
    return False

def opponentsCountryPressed(app, mouseX, mouseY):
    if app.currentCountry == None:
        return False
    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        if countryObject.name in app.currentCountry.adjacentCountries:
            if countryObject not in app.currentPlayer.countriesOwned:
                if ((((mouseX - countryObject.xCord) ** 2 +
                    (mouseY - countryObject.yCord) ** 2) ** .5)
                    < countryObject.radius):
                    app.opponentCountry = countryObject
                    return True
    return False

def stage2_mousePressed(app, event):
    if app.attackOver == True:
        pass
    #Triggers if player chooses to end turn
    if 30 < event.x < 230 and 240 < event.y < 280 and app.attackOver == False:
        app.currentCountry = None
        app.opponentCountry = None
        app.mode = 'stage4'
    #Triggers if player chooses attack
    myCountryPressed(app, event.x, event.y)
    opponentsCountryPressed(app, event.x, event.y)
    if app.currentCountry != None and app.opponentCountry != None:
        app.attackOption = True
    else:
        app.attackOption = False
    if 30 < event.x < 230 and 180 < event.y < 220 and app.attackOver == False:
        app.mode = 'stage3'

def stage2_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.width * .59, app.height * .5,
                        image=ImageTk.PhotoImage(app.scaledMap))
    
    #Draws the country's UI circles
    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        xCord = countryObject.xCord
        yCord = countryObject.yCord
        radius = countryObject.radius
        colorListIndex = countryObject.owner - 1
        canvas.create_oval( xCord - radius, yCord - radius,
                            xCord + radius, yCord + radius,
                            outline = app.colorList[colorListIndex], width = 3,
                            fill = app.colorList[colorListIndex])
        canvas.create_text( xCord, yCord, fill = 'white',
                            text = f'Troops: {countryObject.troops}')

    #Displays who's turn it is
    canvas.create_text(130, 50, font = 'Arial 32',
                        fill = app.colorList[app.playerIndex % app.players],
                        text = f"Player {(app.playerIndex % app.players) + 1}'s Turn")

    if app.attackOption == True:
        canvas.create_rectangle(30, 180, 230, 220, fill = 'yellow')
        canvas.create_text(130, 200, fill = 'black', text = f'ATTACK?')

    canvas.create_rectangle(30, 240, 230, 280, fill = 'yellow')
    canvas.create_text(130, 260, fill = 'black', text = f'MOVE TROOPS')

    #Displays attacking country
    if app.attackOver == False:
        canvas.create_text(130, 100, fill = 'red', text = 'Attacking Country:')
        canvas.create_text(130, 110, fill = 'red', text = f'{app.currentCountry}')
        canvas.create_text(130, 150, fill = 'red', text = 'Defending Country:')
        canvas.create_text(130, 160, fill = 'red', text = f'{app.opponentCountry}')
    else:
        canvas.create_text(130, 100, fill = 'red', text = 'Initial Country:')
        canvas.create_text(130, 110, fill = 'red', text = f'{app.currentCountry}')
        canvas.create_text(130, 150, fill = 'red', text = 'Ending Country:')
        canvas.create_text(130, 160, fill = 'red', text = f'{app.opponentCountry}')
        
        canvas.create_rectangle(30, 180, 230, 280, fill = 'yellow')
        canvas.create_text(130, 220, fill = 'black', text = f'Type amount of')
        canvas.create_text(130, 240, fill = 'black', text = f'troops to migrate')

        canvas.create_rectangle(30, 180, 230, 280, fill = 'yellow')
        canvas.create_text(130, 230, fill = 'black',
                            text = (f'Migrating Troops: {app.migratingTroops}'))
    
    if app.illegalTroopCount == True:
        canvas.create_rectangle(30, 180, 230, 280, fill = 'yellow')
        canvas.create_text(130, 220, fill = 'black', text = f'Illegal troop count')
        canvas.create_text(130, 240, fill = 'black', text = f'Try again')

#########################
# Stage 3 - Attacking Period
#########################
def drawDice(app, canvas):
    canvas.create_text(130, 380, text = 'Click Anywhere to Roll Dice', fill = 'white')
    xCord = 30
    yCord = 400
    for i, number in enumerate(app.attackerDice):
        canvas.create_rectangle(xCord + i * 68, yCord,
                                xCord + (i + 1) * 68, yCord + 68,
                                fill = 'white', outline = 'grey', width = 3)
        canvas.create_text(xCord + (i + .5) * 68, yCord + 34, text = number)
    yCord += 80
    for i, number in enumerate(app.defenderDice):
        canvas.create_rectangle(xCord + i * 68, yCord,
                                xCord + (i + 1) * 68, yCord + 68,
                                fill = 'white', outline = 'grey', width = 3)
        canvas.create_text(xCord + (i + .5) * 68, yCord + 34, text = number)
    attackerDiceList = copy.copy(app.attackerDice)
    defenderDiceList = copy.copy(app.defenderDice)
    lostAttackerTroops = 0
    lostDefenderTroops = 0
    for i in range(min(len(defenderDiceList), len(attackerDiceList))):
        if defenderDiceList[-1] >= attackerDiceList[-1]:
            lostAttackerTroops += 1
        else:
            lostDefenderTroops += 1
        attackerDiceList.pop()
        defenderDiceList.pop()
    canvas.create_text(130, 575, fill = 'yellow',
                        text = f'Attacker Lost {lostAttackerTroops} Troops')
    canvas.create_text(130, 590, fill = 'yellow',
                        text = f'Defender Lost {lostDefenderTroops} Troops')

def stage3_keyPressed(app, event):
    pass

def stage3_mousePressed(app, event):
    #Determines attacker and defender dice rolls
    if app.currentCountry.troops == 2:
        app.attackerDice = []
        for i in range(1):
            app.attackerDice.append(random.randrange(1,7))
    elif app.currentCountry.troops == 3:
        app.attackerDice = []
        for i in range(2):
            app.attackerDice.append(random.randrange(1,7))
    else:
        app.attackerDice = []
        for i in range(3):
            app.attackerDice.append(random.randrange(1,7))
    if app.opponentCountry.troops == 1:
        app.defenderDice = []
        for i in range(1):
            app.defenderDice.append(random.randrange(1,7))
    else:
        app.defenderDice = []
        for i in range(2):
            app.defenderDice.append(random.randrange(1,7))
    app.attackerDice.sort()
    app.defenderDice.sort()
    attackerDiceList = copy.copy(app.attackerDice)
    defenderDiceList = copy.copy(app.defenderDice)
    #Compares the dice rolls against eachother
    for i in range(min(len(defenderDiceList), len(attackerDiceList))):
        if defenderDiceList[-1] >= attackerDiceList[-1]:
            app.currentCountry.troops -= 1
            attackerDiceList.pop()
            defenderDiceList.pop()
            if app.currentCountry.troops == 1:
                app.currentCountry = None
                app.opponentCountry = None
                app.attackOption = False
                app.attackerDice = []
                app.defenderDice = []
                app.mode = 'stage2'
        else:
            app.opponentCountry.troops -= 1
            if app.opponentCountry.troops < 1:
                #Reassigns taken country to their new player
                if app.opponentCountry in app.player1.countriesOwned:
                    app.player1.countriesOwned.remove(app.opponentCountry)
                elif app.opponentCountry in app.player2.countriesOwned:
                    app.player2.countriesOwned.remove(app.opponentCountry)
                elif app.opponentCountry in app.player3.countriesOwned:
                    app.player3.countriesOwned.remove(app.opponentCountry)
                elif app.opponentCountry in app.player4.countriesOwned:
                    app.player4.countriesOwned.remove(app.opponentCountry)
                app.opponentCountry.owner = app.currentCountry.owner
                app.currentPlayer.countriesOwned.append(app.opponentCountry)
                troopsToAdd = 1 - app.opponentCountry.troops
                app.opponentCountry.troops += troopsToAdd
                app.currentCountry.troops -= troopsToAdd
                app.attackOver = True
                app.attackOption = False
                if len(app.currentPlayer.countriesOwned) == 42:
                    app.mode = 'gameOver'
                app.attackerDice = []
                app.defenderDice = []
                app.mode = 'stage2'

def stage3_redrawAll(app, canvas):
    
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.width * .59, app.height * .5,
                        image=ImageTk.PhotoImage(app.scaledMap))
    
    #Draws the country's UI circles
    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        xCord = countryObject.xCord
        yCord = countryObject.yCord
        radius = countryObject.radius
        colorListIndex = countryObject.owner - 1
        canvas.create_oval( xCord - radius, yCord - radius,
                            xCord + radius, yCord + radius,
                            outline = app.colorList[colorListIndex], width = 3,
                            fill = app.colorList[colorListIndex])
        canvas.create_text( xCord, yCord, fill = 'white',
                            text = f'Troops: {countryObject.troops}')

    #Displays who's turn it is
    canvas.create_text(130, 50, font = 'Arial 32',
                        fill = app.colorList[app.playerIndex % app.players],
                        text = f"Player {(app.playerIndex % app.players) + 1}'s Turn")

    #Displays attacking country
    canvas.create_text(130, 100, fill = 'red', text = 'Attacking Country:')
    canvas.create_text(130, 110, fill = 'red', text = f'{app.currentCountry}')
    canvas.create_text(130, 150, fill = 'red', text = 'Defending Country:')
    canvas.create_text(130, 160, fill = 'red', text = f'{app.opponentCountry}')

    canvas.create_rectangle(30, 240, 230, 280, fill = 'yellow')
    canvas.create_text(130, 260, fill = 'black', text = f'END TURN')

    drawDice(app, canvas)

#########################
# Stage 4 - Move Troops
#########################
def stage4_keyPressed(app, event):
    if app.typingMove == True and (event.key).isdigit():
        app.movingTroops = app.movingTroops + event.key
        app.illegalTroopCount = False
    elif app.typingMove == True and event.key == 'Delete' and len(app.movingTroops) > 0:
        app.movingTroops = app.movingTroops[:-1]
        app.illegalTroopCount = False
    if app.typingMove == True and event.key == 'Enter':
        if int(app.movingTroops) > app.initialCountry.troops - 1 or int(app.movingTroops) == 0:
            app.movingTroops = ''
            app.illegalTroopCount = True
        else:
            app.initialCountry.troops -= int(app.movingTroops)
            app.endingCountry.troops += int(app.movingTroops)
            app.typingMove = False
            app.movingTroops = ''
            app.playerIndex += 1
            app.currentPlayer = app.playerList[(app.playerIndex % app.players)]
            troopsToGive(app)
            app.initialCountry = None
            app.endingCountry = None
            app.moveOption = False
            app.mode = 'stage1'

def initialCountryPressed(app, mouseX, mouseY):
    for country in app.currentPlayer.countriesOwned:
        if ((((mouseX - country.xCord) ** 2 +
            (mouseY - country.yCord) ** 2) ** .5)
            < country.radius and country.troops > 1):
            app.initialCountry = country
            app.endingCountry = None
            app.moveOption = False
            return True
    return False

def endingCountryPressed(app, mouseX, mouseY):
    for country in app.currentPlayer.countriesOwned:
        if country.name in app.initialCountry.adjacentCountries:
            if ((((mouseX - country.xCord) ** 2 +
                (mouseY - country.yCord) ** 2) ** .5) < country.radius):
                app.endingCountry = country
                app.moveOption = True
                return True
    return False

def stage4_mousePressed(app, event):
    #Triggers if player chooses to move
    if (30 < event.x < 230 and 180 < event.y < 220 and
        app.initialCountry != None and app.endingCountry != None):
        app.typingMove = True
    elif 30 < event.x < 230 and 240 < event.y < 280 and app.typingMove == False:
        app.typingMove = False
        app.movingTroops = 0
        app.digitCount = 0
        app.playerIndex += 1
        app.currentPlayer = app.playerList[(app.playerIndex % app.players)]
        troopsToGive(app)
        app.initialCountry = None
        app.endingCountry = None
        app.moveOption = False
        app.mode = 'stage1'
    if app.initialCountry == None:
        initialCountryPressed(app, event.x, event.y)
    else:
        endingCountryPressed(app, event.x, event.y)
    if app.initialCountry != None and app.endingCountry != None:
        app.moveOption = True
    else:
        app.moveOption = False
    
def stage4_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')
    canvas.create_image(app.width * .59, app.height * .5,
                        image=ImageTk.PhotoImage(app.scaledMap))
    
    #Draws the country's UI circles
    for countryName in app.countryDictionary:
        countryObject = app.countryDictionary[countryName]
        xCord = countryObject.xCord
        yCord = countryObject.yCord
        radius = countryObject.radius
        colorListIndex = countryObject.owner - 1
        canvas.create_oval( xCord - radius, yCord - radius,
                            xCord + radius, yCord + radius,
                            outline = app.colorList[colorListIndex], width = 3,
                            fill = app.colorList[colorListIndex])
        canvas.create_text( xCord, yCord, fill = 'white',
                            text = f'Troops: {countryObject.troops}')

    #Displays who's turn it is
    canvas.create_text(130, 50, font = 'Arial 32',
                        fill = app.colorList[app.playerIndex % app.players],
                        text = f"Player {(app.playerIndex % app.players) + 1}'s Turn")

    #Displays initial & ending country
    canvas.create_text(130, 100, fill = 'red', text = 'Initial Country:')
    canvas.create_text(130, 110, fill = 'red', text = f'{app.initialCountry}')
    canvas.create_text(130, 150, fill = 'red', text = 'Ending Country:')
    canvas.create_text(130, 160, fill = 'red', text = f'{app.endingCountry}')

    canvas.create_rectangle(30, 240, 230, 280, fill = 'yellow')
    canvas.create_text(130, 260, fill = 'black', text = f'END TURN?')

    #Displays option to select troop count
    if app.moveOption == True:
        canvas.create_rectangle(30, 180, 230, 220, fill = 'yellow')
        canvas.create_text(130, 200, fill = 'black', text = f'MOVE TROOPS?')

    if app.typingMove == True:
        canvas.create_rectangle(30, 180, 230, 280, fill = 'yellow')
        canvas.create_text(130, 220, fill = 'black', text = f'Please type')
        canvas.create_text(130, 240, fill = 'black', text = f'troops to move')

    if app.typingMove == True:
        canvas.create_rectangle(30, 180, 230, 280, fill = 'yellow')
        canvas.create_text(130, 230, fill = 'black',
                            text = (f'Moving Troops: {app.movingTroops}'))

    if app.illegalTroopCount == True:
        canvas.create_rectangle(30, 180, 230, 280, fill = 'yellow')
        canvas.create_text(130, 220, fill = 'black', text = f'Illegal troop count')
        canvas.create_text(130, 240, fill = 'black', text = f'Try again')

#########################
# gameOver
#########################
def gameOver_keyPressed(app, event):
    if (event.key == 'r'):
        appStarted(app)

def gameOver_mousePressed(app, event):
    pass

def gameOver_redrawAll(app, canvas):
    canvas.create_image(app.middleX, app.middleY,
                        image=ImageTk.PhotoImage(app.scaledWinScreen))
    canvas.create_text(app.width // 2, app.height * .75, font = 'Arial 96',
                        fill = 'red', text = f'{app.currentPlayer}!!!')
    canvas.create_text(app.width // 2, app.height * .15, font = 'Arial 96',
                        fill = 'red', text = 'Press R to restart')

#########################
# Main App
#########################
def createCountries(app):
    countryList = [ 'Alaska', 'Western Canada', 'Central America',
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
                    'Siam', 'Siberia', 'Ural', 'Yakutsk',
                    
                    'Eastern Australia', 'New Guinea',
                    'Indonesia', 'Western Australia'     ]

    #Creates dictionary of countries with just their name
    app.countryDictionary = {name: Country(name=name) for name in countryList}

    countryCoordinates = [  (363, 143, 35), (483, 204, 29), (491, 370, 44),
                            (575, 310, 47), (718, 82, 77), (474, 147, 26),
                            (550, 206, 28), (638, 210, 45), (475, 272, 37),
                            
                            (566, 646, 60), (639, 506, 56),
                            (560, 540, 23), (535, 431, 26),
                            
                            (761, 233, 33), (762, 167, 20), (828, 248, 22),
                            (830, 159, 52), (833, 318, 33), (943, 187, 60),
                            (758, 308, 43),
                            
                            (845, 546, 30), (896, 488, 39), (855, 395, 38),
                            (936, 634, 32), (769, 469, 63), (836, 655, 58),
                            
                            (998, 292, 45), (1108, 329, 43), (1062, 440, 64),
                            (1177, 217, 29), (1288, 300, 42), (1333, 188, 70),
                            (953, 395, 53), (1215, 270, 35), (1150, 420, 28),
                            (1111, 175, 45), (1036, 190, 31), (1219, 137, 39),
                            
                            (1310, 618, 59), (1300, 517, 42),
                            (1175, 504, 59), (1165, 635, 40)     ]
    
    #Assigns each country its x & y coordinates and radius
    for index, country in enumerate(app.countryDictionary):
        app.countryDictionary[country].xCord = countryCoordinates[index][0]
        app.countryDictionary[country].yCord = countryCoordinates[index][1]
        app.countryDictionary[country].radius = countryCoordinates[index][2]
    
    #Assigns each country its adjacentcountries
        adjacentCountriesList = [
                            {'Western Canada', 'Northwest Territory', 'Kamchatka'},
                            {'Alaska', 'Northwest Territory', 'Central Canada', 'Western United States'},
                            {'Eastern United States', 'Western United States', 'Venezuela'},
                            {'Central America', 'Central Canada', 'Eastern Canada', 'Western United States'},
                            {'Northwest Territory', 'Central Canada', 'Eastern Canada', 'Iceland'},
                            {'Alaska', 'Western Canada', 'Greenland', 'Central Canada'},
                            {'Western Canada', 'Eastern United States', 'Greenland', 'Eastern Canada', 'Western United States'},
                            {'Eastern United States', 'Greenland', 'Central Canada'},
                            {'Western Canada', 'Central America', 'Eastern United States', 'Central Canada'},

                            {'Brazil', 'Peru'},
                            {'Peru', 'Argentina', 'Venezuela', 'North Africa'},
                            {'Argentina', 'Brazil', 'Venezuela'},
                            {'Central America', 'Brazil', 'Peru'},

                            {'Iceland', 'Northern Europe', 'Scandinavia', 'Western Europe'},
                            {'Greenland', 'Great Britain', 'Scandinavia'},
                            {'Great Britain', 'Scandinavia', 'Southern Europe', 'Ukraine', 'Western Europe'},
                            {'Great Britain', 'Iceland', 'Northern Europe', 'Ukraine'},
                            {'Egypt', 'North Africa', 'Northern Europe', 'Ukraine', 'Western Europe', 'Middle East'},
                            {'Northern Europe', 'Scandinavia', 'Southern Europe', 'Afghanistan', 'Middle East', 'Ural'},
                            {'Great Britain', 'Northern Europe', 'Southern Europe', 'North Africa'},

                            {'East Africa', 'North Africa', 'South Africa'},
                            {'Congo', 'Egypt', 'Madagascar', 'North Africa', 'Middle East'},
                            {'East Africa', 'North Africa', 'Southern Europe', 'Middle East'},
                            {'East Africa', 'South Africa'},
                            {'Congo', 'East Africa', 'Egypt', 'Brazil', 'Southern Europe', 'Western Europe'},
                            {'Congo', 'East Africa', 'Madagascar'},

                            {'China', 'India', 'Middle East', 'Ural', 'Ukraine'},
                            {'Afghanistan', 'India', 'Mongolia', 'Siam', 'Siberia', 'Ural'},
                            {'Afghanistan', 'China', 'Middle East', 'Siam'},
                            {'Kamchatka', 'Mongolia', 'Siberia', 'Yakutsk'},
                            {'Kamchatka', 'Mongolia'},
                            {'Irkutsk', 'Japan', 'Mongolia', 'Yakutsk', 'Alaska'},
                            {'Afghanistan', 'India', 'Southern Europe', 'Ukraine', 'East Africa', 'Egypt'},
                            {'China', 'Irkutsk', 'Japan', 'Kamchatka', 'Siberia'},
                            {'China', 'India', 'Indonesia'},
                            {'China', 'Irkutsk', 'Mongolia', 'Ural', 'Yakutsk'},
                            {'Afghanistan', 'China', 'Siberia', 'Ukraine'},
                            {'Irkutsk', 'Kamchatka', 'Siberia'},

                            {'New Guinea', 'Western Australia'},
                            {'Eastern Australia', 'Western Australia', 'Indonesia'},
                            {'Western Australia', 'New Guinea', 'Siam'},
                            {'Eastern Australia', 'New Guinea', 'Indonesia'}   ]

    for index, countryName in enumerate(app.countryDictionary):
        countryObject = app.countryDictionary[countryName]
        countryObject.adjacentCountries = adjacentCountriesList[index]

    #Assigns each country its continent
    continentList = (['North America'] * 9 + ['South America'] * 4 +
                    ['Europe'] * 7 + ['Africa'] * 6 +
                    ['Asia'] * 12 + ['Australia'] * 4)
    for index, countryName in enumerate(app.countryDictionary):
        countryObject = app.countryDictionary[countryName]
        countryObject.continent = continentList[index]

def appStarted(app):
    app.mode = 'playerSelectionMode'
    #########################
    # Player Selection Mode
    #########################
    titleScreenUrl = 'https://steamcdn-a.akamaihd.net/steam/apps/1128810/capsule_616x353.jpg?t=1604115364'
    # titleScreenUrl = 'RiskMap.jpeg'
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
    # Stage 1
    #########################
        #########################
        # Stage 1 - Images
        #########################
    mapUrl = 'https://i.stack.imgur.com/sKx7n.jpg'
    app.map = app.loadImage(mapUrl)
    # For No Wifi
    # app.map = app.loadImage('RiskMap.jpeg')
    app.mapWidth, app.mapHeight = app.map.size
    mapScaleFactor = min(app.height / app.mapHeight, app.width / app.mapWidth)
    app.scaledMap = app.scaleImage(app.map, mapScaleFactor)
        #########################
        # Stage 1 - Mechanics
        #########################
    app.player1 = Player(1, 0, [])
    app.player2 = Player(2, 0, [])
    app.player3 = Player(3, 0, [])
    app.player4 = Player(4, 0, [])
    app.playerList = [app.player1, app.player2, app.player3, app.player4]
    app.playerIndex = 0
    app.currentPlayer = app.playerList[0]
    app.countryDictionary = {}
    app.currentCountry = None
    app.opponentCountry = None
    createCountries(app)
    app.attackOption = False
    app.attackerDice = []
    app.defenderDice = []
    app.moveOption = False
    app.initialCountry = None
    app.endingCountry = None
    app.movingTroops = ''
    app.typingMove = False
    app.illegalTroopCount = False
    app.colorList = ['Green', 'Blue', 'Red', 'Grey']
    app.attackOver = False
    app.migratingTroops = ''
    #########################
    # Win Mode
    #########################
    winURL = 'https://thumbs.dreamstime.com/b/screen-winner-gold-award-glowing-green-victory-banner-ui-game-screen-winner-gold-award-glowing-green-victory-banner-ui-220155562.jpg'
    app.winScreen = app.loadImage(winURL)
    app.winWidth, app.winHeight = app.winScreen.size
    winScreeenScaleFactor = app.width / app.winWidth
    app.scaledWinScreen = app.scaleImage(app.winScreen, winScreeenScaleFactor)

def runRisk():
    width = 1500
    height = 750
    runApp(width=width, height=height)

runRisk()