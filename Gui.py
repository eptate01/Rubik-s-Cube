from tkinter import *
from math import floor
import random
import math
import matplotlib.pyplot as plt
Amt_Moves = 24
current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
solved_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
numTurns = int(input("For randomizer, how many random turns would you like? (difficulty) "))

def draw(label, label_state): #for the gui, this assigns the label for every square in the gui. draw function only assigns label, it doesn't update the window
    for i in range(len(label)):
        for j in range(len(label[0])):
            label[i][j]["text"] = "  "
            value = label_state[11*i + j]
            match value:
                case 0:
                    label[i][j]["bg"] = "#000000"
                case 1:
                    label[i][j]["bg"] = "#006400"
                case 2:
                    label[i][j]["bg"] = "#5D478B"
                case 3:
                    label[i][j]["bg"] = "#FFFF00"
                case 4:
                    label[i][j]["bg"] = "#87CEFF"
                case 5:
                    label[i][j]["bg"] = "#FF0000"
                case 6:
                    label[i][j]["bg"] = "#008080"
                case 7:
                    label[i][j]["bg"] = "#FF69B4"
                case 8:
                    label[i][j]["bg"] = "#ADFF2F"
                case 9:
                    label[i][j]["bg"] = "#FF6103"
                case 10:
                    label[i][j]["bg"] = "#00FFFF"
                case 11:
                    label[i][j]["bg"] = "#808A87"

def turn(): #this function is also for the gui
    global current_state
    sideToTurn = dropdown.get() #gets value from dropdown in gui
    if sideToTurn == "Choose a side to turn":
        return
    current_state = [current_state[i] for i in MOVES[int(sideToTurn)]] #this is the code that turns the megaminx everywhee else in the code
    
    draw(label, current_state)

def randomizer(): #this randomizer function is only for the gui randomize button, not the Astar randomize
    global current_state
    for i in range(numTurns): #numturns is a global variable in main. The user gives this when they run the code
        current_state = [current_state[i] for i in MOVES[int(random.randint(0, 23))]]
        draw(label, current_state)
    
def Astar_randomizer(new_state, turns): #randomizer for Astar
    for i in range(turns):
        move = int(random.randint(0, 23))
        print("move ", i, ": ", move)
        new_state = [new_state[i] for i in MOVES[move]]
    return new_state
        
def hueristic(state): #hueristic goes through every face and checks if it matches the center state (I only keep track of colors so this function works)
    counter = 0
    for i in range(132):
        if solved_state[i] != state[i]:
            counter += 1
    return math.ceil(counter/15) #15 faces can be different at one time, and round up

def Astar(starting_state):
    nodesVisited = 0
    solved_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    open_set = set() #this is a set of all the states that haven't been looped through or can be looped through with a lesser g value. the states are saved as tuples, not lists
    open_set.add(tuple((starting_state)))
    closed_set = set() # a set of states that have been gone through
    g = {} #this is a dictionary giving the g values for every state
    g[tuple((starting_state))] = 0

    parents = {} #dictionary of the parent node
    parents[tuple((starting_state))] = None #starting state does not have a parent_node
    temp_state = starting_state
    while len(open_set) > 0: #while the open_set is not null
        next = None #next is the node you are currently working on

        #PRIORITY QUEUE
        for i in open_set:
            if next == None or g[tuple((i))] + hueristic(i) < g[tuple((next))] + hueristic(next):
                next = i
        nodesVisited += 1 #you just started a visit to a node

        if (next == tuple(solved_state)): #if this node is a solved state
            moves = []

            while parents[tuple((next))]: #find the moves that got to this solved state
                moves.append(findMove(parents[tuple(next)],next ))
                next = parents[tuple(next)]
            moves.reverse()
            print('Moves: ', moves)
            return moves, nodesVisited
        else:
            for i in range(0,24):
                temp_state = [next[j] for j in MOVES[i]] #preform the moves
                temp_state_tuple = tuple(([next[j] for j in MOVES[i]])) #store move as a tuple
                if temp_state_tuple not in open_set and temp_state_tuple not in closed_set: #if this state has not been reached, add it to open_set
                    open_set.add(temp_state_tuple)
                    parents[temp_state_tuple] = next
                    g[temp_state_tuple] = g[tuple((next))]+1
                else: #if the state has been reached, check if it has a lower g value than the other time it was reached. If it has a lower g value then add it to open_set
                    if g[temp_state_tuple] + hueristic(temp_state_tuple) > g[tuple((next))] + hueristic(temp_state):
                        g[temp_state_tuple] = g[tuple((next))]+1
                        parents[temp_state_tuple] = next

                        if temp_state_tuple in closed_set:
                            closed_set.remove(temp_state_tuple)
                            open_set.add(temp_state_tuple)
        open_set.remove(next) #remove the variable from open_set and add to closed_set
        closed_set.add(next)
        
def AstarFunc(): #For Gui Use
    global current_state
    current_state = Astar_randomizer(solved_state, numTurns) #randomize
    draw(label, current_state) #draw
    move, count = Astar(current_state) #get moves from Astar
    for j in move:
        root.update()#update gui
        root.after(2000)#wait before updating a gui so user can see process
        current_state = [current_state[i] for i in MOVES[j]] #make the move recommended by Astar
        draw(label, current_state) #create label so when root updates, the gui has the new state loaded

def AstarLoop(): #For K values
    xaxis = []
    graph = []
    for k in range(3,8): #k-values for how many rotations
        xaxis.append(k)
        averageNodesExpanded = 0
        for i in range(0,3): #run 3 samples for k
            temp_state = Astar_randomizer(solved_state, k)
            moves, NodesExpanded = Astar(temp_state)
            averageNodesExpanded += NodesExpanded
        graph.append(averageNodesExpanded/3) #put the average nodes expanded in a list to graph
    print(xaxis, graph)
    plt.plot(xaxis, graph)
    plt.show()

def findMove(state, end_state):
    for i in range(Amt_Moves):
        if end_state == tuple([state[j] for j in MOVES[i]]):
            return i
    raise Exception("Move Not available")          

COLORS = {
'0': 'black',
'1': 'green',
'2':  'purple',
'3': 'yellow',
'4': 'blue',
'5': 'red',
'6': 'teal',
'7': 'pink',
'8':'lime',
'9': 'orange',
'10': 'aqua',
'11': 'gray'
}

MOVES = {0:[0, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 11, 76, 67, 68, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 79, 46, 47, 48, 49, 50, 51, 52, 87, 78, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 54, 45, 69, 70, 71, 72, 73, 74, 75, 53, 77, 122, 123, 80, 81, 82, 83, 84, 85, 86, 131, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 13, 14, 124, 125, 126, 127, 128, 129, 130, 12],
        1: [0, 1, 2, 3, 4, 5, 6, 123, 124, 125, 10, 11, 20, 21, 12, 13, 14, 15, 16, 17, 18, 19, 22, 76, 24, 25, 26, 27, 28, 29, 30, 74, 75, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 7, 8, 9, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 31, 32, 23, 115, 116, 117, 118, 119, 120, 121, 122, 112, 113, 114, 126, 127, 128, 129, 130, 131],
        2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 114, 115, 116, 19, 20, 21, 22, 31, 32, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39, 72, 73, 74, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 16, 17, 18, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 40, 41, 42, 106, 107, 108, 109, 110, 111, 112, 113, 103, 104, 105, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 105, 106, 107, 28, 29, 30, 31, 32, 33, 42, 43, 34, 35, 36, 37, 38, 39, 40, 41, 44, 45, 46, 47, 48, 70, 71, 72, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 25, 26, 27, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 49, 50, 51, 97, 98, 99, 100, 101, 102, 103, 104, 94, 95, 96, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        4: [0, 1, 2, 68, 69, 70, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 96, 97, 98, 37, 38, 39, 40, 41, 42, 43, 44, 53, 54, 45, 46, 47, 48, 49, 50, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 34, 35, 36, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 3, 4, 5, 88, 89, 90, 91, 92, 93, 94, 95, 85, 86, 87, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 64, 65, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 84, 85, 86, 87, 88, 89, 109, 100, 101, 93, 94, 95, 96, 97, 98, 99, 119, 120, 102, 103, 104, 105, 106, 107, 108, 118, 110, 111, 112, 113, 114, 115, 116, 117, 127, 128, 129, 121, 122, 123, 124, 125, 126, 81, 82, 83, 130, 131],
        6: [0, 1, 2, 3, 4, 14, 15, 16, 8, 9, 10, 11, 12, 13, 23, 24, 25, 17, 18, 19, 20, 21, 22, 42, 43, 34, 26, 27, 28, 29, 30, 31, 32, 33, 53, 35, 36, 37, 38, 39, 40, 41, 51, 52, 44, 45, 46, 47, 48, 49, 50, 5, 6, 7, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 75, 76, 67, 68, 69, 70, 71, 72, 73, 74, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        7: [0, 45, 46, 47, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 98, 89, 90, 48, 49, 50, 51, 52, 53, 54, 55, 131, 57, 58, 59, 60, 61, 62, 63, 129, 130, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 86, 87, 78, 79, 80, 81, 82, 83, 84, 85, 88, 65, 56, 91, 92, 93, 94, 95, 96, 97, 64, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 1, 2, 3],
        8: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 107, 108, 109, 39, 40, 41, 42, 43, 44, 45, 46, 36, 37, 38, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 83, 84, 85, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 47, 48, 49, 86, 87, 88, 97, 98, 89, 90, 91, 92, 93, 94, 95, 96, 99, 100, 101, 102, 103, 104, 105, 106, 62, 63, 64, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 116, 117, 118, 30, 31, 32, 33, 34, 35, 36, 37, 27, 28, 29, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 92, 93, 94, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 38, 39, 40, 95, 96, 97, 98, 99, 108, 109, 100, 101, 102, 103, 104, 105, 106, 107, 110, 111, 112, 113, 114, 115, 60, 61, 62, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        10:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 125, 126, 127, 21, 22, 23, 24, 25, 26, 27, 28, 18, 19, 20, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 101, 102, 103, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 29, 30, 31, 104, 105, 106, 107, 108, 109, 110, 119, 120, 111, 112, 113, 114, 115, 116, 117, 118, 121, 122, 123, 124, 58, 59, 60, 128, 129, 130, 131],
        11:[0, 81, 2, 3, 4, 5, 6, 7, 8, 79, 80, 11, 1, 13, 14, 15, 16, 17, 18, 19, 9, 10, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 120, 111, 112, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 56, 57, 58, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 21, 12, 113, 114, 115, 116, 117, 118, 119, 20, 121, 130, 131, 122, 123, 124, 125, 126, 127, 128, 129],
        12: [0, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 11, 131, 122, 123, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 68, 46, 47, 48, 49, 50, 51, 52, 76, 67, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 13, 14, 69, 70, 71, 72, 73, 74, 75, 12, 77, 54, 45, 80, 81, 82, 83, 84, 85, 86, 53, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 78, 79, 124, 125, 126, 127, 128, 129, 130, 87],
        13: [0, 1, 2, 3, 4, 5, 6, 74, 75, 76, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 12, 13, 22, 114, 24, 25, 26, 27, 28, 29, 30, 112, 113, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 31, 32, 23, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 123, 124, 125, 115, 116, 117, 118, 119, 120, 121, 122, 7, 8, 9, 126, 127, 128, 129, 130, 131],
        14: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 72, 73, 74, 19, 20, 21, 22, 25, 26, 27, 28, 29, 30, 31, 32, 23, 24, 33, 34, 35, 36, 37, 38, 39, 103, 104, 105, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 40, 41, 42, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 114, 115, 116, 106, 107, 108, 109, 110, 111, 112, 113, 16, 17, 18, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        15: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 70, 71, 72, 28, 29, 30, 31, 32, 33, 36, 37, 38, 39, 40, 41, 42, 43, 34, 35, 44, 45, 46, 47, 48, 94, 95, 96, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 49, 50, 51, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 105, 106, 107, 97, 98, 99, 100, 101, 102, 103, 104, 25, 26, 27, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        16: [0, 1, 2, 85, 86, 87, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 68, 69, 70, 37, 38, 39, 40, 41, 42, 43, 44, 47, 48, 49, 50, 51, 52, 53, 54, 45, 46, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 3, 4, 5, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 96, 97, 98, 88, 89, 90, 91, 92, 93, 94, 95, 34, 35, 36, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        17: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 65, 56, 57, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 127, 128, 129, 84, 85, 86, 87, 88, 89, 81, 82, 83, 93, 94, 95, 96, 97, 98, 99, 91, 92, 102, 103, 104, 105, 106, 107, 108, 90, 110, 111, 112, 113, 114, 115, 116, 117, 109, 100, 101, 121, 122, 123, 124, 125, 126, 118, 119, 120, 130, 131],
        18: [0, 1, 2, 3, 4, 51, 52, 53, 8, 9, 10, 11, 12, 13, 5, 6, 7, 17, 18, 19, 20, 21, 22, 14, 15, 16, 26, 27, 28, 29, 30, 31, 32, 33, 25, 35, 36, 37, 38, 39, 40, 41, 23, 24, 44, 45, 46, 47, 48, 49, 50, 42, 43, 34, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 69, 70, 71, 72, 73, 74, 75, 76, 67, 68, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        19: [0, 129, 130, 131, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 1, 2, 3, 48, 49, 50, 51, 52, 53, 54, 55, 90, 57, 58, 59, 60, 61, 62, 63, 98, 89, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 78, 79, 88, 46, 47, 91, 92, 93, 94, 95, 96, 97, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 64, 65, 56],
        20: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 47, 48, 49, 39, 40, 41, 42, 43, 44, 45, 46, 83, 84, 85, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 107, 108, 109, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 62, 63, 64, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 89, 90, 99, 100, 101, 102, 103, 104, 105, 106, 36, 37, 38, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        21: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 38, 39, 40, 30, 31, 32, 33, 34, 35, 36, 37, 92, 93, 94, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 116, 117, 118, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 60, 61, 62, 95, 96, 97, 98, 99, 102, 103, 104, 105, 106, 107, 108, 109, 100, 101, 110, 111, 112, 113, 114, 115, 27, 28, 29, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
        22: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 29, 30, 31, 21, 22, 23, 24, 25, 26, 27, 28, 101, 102, 103, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 125, 126, 127, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 58, 59, 60, 104, 105, 106, 107, 108, 109, 110, 113, 114, 115, 116, 117, 118, 119, 120, 111, 112, 121, 122, 123, 124, 18, 19, 20, 128, 129, 130, 131],
        23: [0, 12, 2, 3, 4, 5, 6, 7, 8, 20, 21, 11, 112, 13, 14, 15, 16, 17, 18, 19, 120, 111, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 79, 80, 81, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 9, 10, 1, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 57, 58, 113, 114, 115, 116, 117, 118, 119, 56, 121, 124, 125, 126, 127, 128, 129, 130, 131, 122, 123]}


#Creating Tkinter-----------------------------------------------------------------------------------------------------------


faces = []
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1000x550")
  
# Add image file
bg = PhotoImage( file = "megaminx.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
  
# Add text
xPos = [280, 150, 200, 365, 415, 680, 285, 600, 550, 680, 810, 760]
yPos = [160, 260, 415, 413, 260, 260, 290, 135, 290, 385, 290, 135]

label = [[0 for col in range(11)] for row in range(12)]

for i in range(0, 6):
    
    label[i][0] = Label( root, text = "{}".format(current_state[11 * i + 0]), bg = "#000000")
    label[i][0].place(x = xPos[i], y = yPos[i])
    
    label[i][1] = Label( root, text = "{}".format(current_state[11 * i + 1]), bg = "#000000")
    label[i][1].place(x = xPos[i], y = yPos[i] - 70)
    
    label[i][2] = Label( root, text = "{}".format(current_state[11 * i + 2]), bg = "#000000")
    label[i][2].place(x = xPos[i] + 30, y = yPos[i] - 50)
    
    label[i][3] = Label( root, text = "{}".format(current_state[11 * i + 3]), bg = "#000000")
    label[i][3].place(x = xPos[i] + 60, y = yPos[i] - 30)
  
    label[i][4] = Label( root, text = "{}".format(current_state[11 * i + 4]), bg = "#000000")
    label[i][4].place(x = xPos[i] + 45, y = yPos[i] + 15)

    label[i][5] = Label( root, text = "{}".format(current_state[11 * i + 5]), bg = "#000000")
    label[i][5].place(x = xPos[i] + 30, y = yPos[i] + 45)
    
    label[i][6] = Label( root, text = "{}".format(current_state[11 * i + 6]), bg = "#000000")
    label[i][6].place(x = xPos[i], y = yPos[i] + 45)

    label[i][7] = Label( root, text = "{}".format(current_state[11 * i + 7]), bg = "#000000")
    label[i][7].place(x = xPos[i] - 30, y = yPos[i] + 45)
   
    label[i][8] = Label( root, text = "{}".format(current_state[11 * i + 8]), bg = "#000000")
    label[i][8].place(x = xPos[i] - 45, y = yPos[i] + 15)
    
    label[i][9] = Label( root, text = "{}".format(current_state[11 * i + 9]), bg = "#000000")
    label[i][9].place(x = xPos[i] - 60, y = yPos[i] - 30)
    
    label[i][10] = Label( root, text = "{}".format(current_state[11 * i + 10]), bg = "#000000")
    label[i][10].place(x = xPos[i] - 30, y = yPos[i] - 50)
    
for i in range(6, 12):
    label[i][0] = Label( root, text = "{}".format(current_state[11 * i + 0]), bg = "#000000")
    label[i][0].place(x = xPos[i], y = yPos[i])
    
    label[i][1] = Label( root, text = "{}".format(current_state[11 * i + 1]), bg = "#000000")
    label[i][1].place(x = xPos[i], y = yPos[i] - 45)
    
    label[i][2] = Label( root, text = "{}".format(current_state[11 * i + 2]), bg = "#000000")
    label[i][2].place(x = xPos[i] + 40, y = yPos[i] - 45)
    
    label[i][3] = Label( root, text = "{}".format(current_state[11 * i + 3]), bg = "#000000")
    label[i][3].place(x = xPos[i] + 50, y = yPos[i] - 10)
    
    label[i][4] = Label( root, text = "{}".format(current_state[11 * i + 4]), bg = "#000000")
    label[i][4].place(x = xPos[i] + 60, y = yPos[i] + 25)
    
    label[i][5] = Label( root, text = "{}".format(current_state[11 * i + 5]), bg = "#000000")
    label[i][5].place(x = xPos[i] + 30, y = yPos[i] + 45)
    
    label[i][6] = Label( root, text = "{}".format(current_state[11 * i + 6]), bg = "#000000")
    label[i][6].place(x = xPos[i], y = yPos[i] + 65)
    
    label[i][7] = Label( root, text = "{}".format(current_state[11 * i + 7]), bg = "#000000")
    label[i][7].place(x = xPos[i] - 30, y = yPos[i] + 45)
    
    label[i][8] = Label( root, text = "{}".format(current_state[11 * i + 8]), bg = "#000000")
    label[i][8].place(x = xPos[i] - 60, y = yPos[i] + 25)
    
    label[i][9] = Label( root, text = "{}".format(current_state[11 * i + 9]), bg = "#000000")
    label[i][9].place(x = xPos[i] - 50, y = yPos[i] - 10)
    
    label[i][10] = Label( root, text = "{}".format(current_state[11 * i + 10]), bg = "#000000")
    label[i][10].place(x = xPos[i] - 40, y = yPos[i] - 45)


# Dropdown menu options
options = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
]  
# datatype of menu text
dropdown = StringVar()
dropdown.set( "Choose a side to turn" )
drop = OptionMenu( root , dropdown , *options )
drop.pack()
# Create button, it will change label text
button = Button( root , text = "Turn Side" , command = turn )
button.pack()
button2 = Button( root , text = "Randomize" , command = randomizer)
button2.pack()
button3 = Button(root, text = "Astar + randomize", command = AstarFunc)
button3.pack()
draw(label, current_state)


# Execute tkinter
root.mainloop()

#END of Tkinter----------------------------------------------------------------------------------------
AstarLoop()
