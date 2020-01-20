# -*- coding: utf-8 -*-
"""
Created on Thursday January 16 2020

@author: Daniel Tran
"""

import Dominion
import testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#Create player Objects
players = testUtility.makePlayers(player_names)

#number of curses and victory cards returned in a list
numVictAndCurse = testUtility.getNumVictNumCurse(len(players))

#Get the dictionary of costs to card names
supply_order = testUtility.getSupplyOrder()

#Define box
box = testUtility.getBoxes(numVictAndCurse[0])

#Pick 10 cards from box to be in the supply.
supply = testUtility.getSupply(box)

#Fill in some default dominion cards in the supply, but a bug is introduced where
# the number of victory cards passed in is 1, meaning the first person to
# get enough gold to buy a province wins the game, which isn't much of a game
testUtility.defaultSupply(len(players), supply, 1, numVictAndCurse[1])

#initialize the trash
trash = []

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
