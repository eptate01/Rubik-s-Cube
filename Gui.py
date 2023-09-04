import numpy as np

COLORS = {
'0': 'white',
'1': 'green',
'2':  'purple',
'3': 'yellow',
'4': 'blue',
'5': 'red',
'6': 'cream',
'7': 'pink',
'8':'lime',
'9': 'orange',
'10': 'aqua',
'11': 'gray'
}

MOVES = {
    0: [0,9,10,1,2,3,4,5,6,7,8,11,56,57,58,15,16,17,18,19,20,21,22,12,13,14,26,27,28,29,30,31,32,33,23,24,25,37,38,39,40,41,42,43,44,34,35,36,48,49,50,51,52,53,54,55,45,46,47,59,60,61,62,63,64,65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    1: [0,1,2,3,4,25,26,27,8,9,10,11,20,21,12,13,14,15,16,17,18,19,22,23,24,117,118,119,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,7,57,58,59,60,61,62,63,5,6,66,56,68,69,70,71,72,73,74,64,65,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,75,76,67,120,121,122,123,124,125,126,127,128,129,130,131],
    2: [0,1,2,3,4,5,6,36,37,38,10,11,9,13,14,15,16,17,18,19,7,8,22,23,24,25,26,27,28,29,30,31,32,33,34,35,106,107,108,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,115,116,117,109,110,111,112,113,114,20,21,12,118,119,120,121,122,123,124,125,126,127,128,129,130,131],
    3 : [0,49,2,3,4,5,6,7,8,47,48,11,12,13,14,15,16,17,18,19,20,21,22,1,24,25,26,27,28,29,30,9,10,33,42,43,34,35,36,37,38,39,40,41,44,45,46,95,96,97,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,98,99,100,101,102,103,31,32,23,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131],
    4: [0,58,59,60,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,3,35,36,37,38,39,40,41,1,2,44,53,54,45,46,47,48,49,50,51,52,55,56,57,84,85,86,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,87,88,89,90,91,92,42,43,34,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131],
    5: [0, 1, 2, 14, 15, 16, 6, 7, 8, 9, 10, 11, 12, 13, 67, 68, 69, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 5, 46, 47, 48, 49, 50, 51, 52, 3, 4, 55, 64,65,56, 57, 58, 59, 60, 61, 62, 63, 66, 82, 83, 84, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 53, 54, 45, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    6: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 119, 120, 111, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 16,17,18, 65, 66, 75,76, 67, 68, 69, 70, 71, 72, 73, 74, 77, 78, 79, 62,63,64, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 122, 112, 113, 114, 115, 116, 117, 118, 130, 131, 121, 82, 123, 124, 125, 126, 127, 128, 129, 80, 81],
    7: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 60, 61, 62, 54, 55, 56, 57, 58, 59, 69,70,71, 63, 64, 65, 66, 67, 68, 122,123,124, 72, 73, 74, 75, 76, 77, 86,87,78, 79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 51, 52, 53, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 91, 92, 93, 125, 126, 127, 128, 129, 130, 131]
}



solved_state = []
test = 7
for i in range(0,132):
    solved_state.append(i)
current_state = [solved_state[i] for i in MOVES[test]]
current_state = [current_state[i] for i in MOVES[test]]
current_state = [current_state[i] for i in MOVES[test]]
current_state = [current_state[i] for i in MOVES[test]]
current_state = [current_state[i] for i in MOVES[test]]
if solved_state == current_state:
    print("solved!!")
else:
    print(current_state)