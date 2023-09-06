import numpy as np
from PIL import Image, ImageDraw
img = Image.new("RGBA", (500,500))
draw = ImageDraw.Draw(img)
draw.rectangle((0,100,300,300), outline = 'teal', fill = 'orange', width = 25)
draw.rectangle((300,300,400,400), outline = 'white', fill = 'black', width = 25)
img.show()
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
    3: [0,49,2,3,4,5,6,7,8,47,48,11,12,13,14,15,16,17,18,19,20,21,22,1,24,25,26,27,28,29,30,9,10,33,42,43,34,35,36,37,38,39,40,41,44,45,46,95,96,97,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,98,99,100,101,102,103,31,32,23,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131],
    4: [0,58,59,60,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,3,35,36,37,38,39,40,41,1,2,44,53,54,45,46,47,48,49,50,51,52,55,56,57,84,85,86,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,87,88,89,90,91,92,42,43,34,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131],
    5: [0, 1, 2, 14, 15, 16, 6, 7, 8, 9, 10, 11, 12, 13, 67, 68, 69, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 5, 46, 47, 48, 49, 50, 51, 52, 3, 4, 55, 64,65,56, 57, 58, 59, 60, 61, 62, 63, 66, 82, 83, 84, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 53, 54, 45, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    6: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 119, 120, 111, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 16,17,18, 65, 66, 75,76, 67, 68, 69, 70, 71, 72, 73, 74, 77, 78, 79, 62,63,64, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 122, 112, 113, 114, 115, 116, 117, 118, 130, 131, 121, 82, 123, 124, 125, 126, 127, 128, 129, 80, 81],
    7: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 60, 61, 62, 54, 55, 56, 57, 58, 59, 69,70,71, 63, 64, 65, 66, 67, 68, 122,123,124, 72, 73, 74, 75, 76, 77, 86,87,78, 79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 51, 52, 53, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 91, 92, 93, 125, 126, 127, 128, 129, 130, 131],
    8: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 49, 50, 51, 43, 44, 45, 46, 47, 48, 86,87,78, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 126, 79, 80, 81, 82, 83, 84, 85, 124,125, 88, 97,98,89, 90, 91, 92, 93, 94, 95, 96, 99, 100, 101, 40,41,42, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 102,103, 104, 127, 128, 129, 130, 131],
    9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 38,39,40, 32, 33, 34, 35, 36, 37, 97,98,89, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 128, 90, 91, 92, 93, 94, 95, 96, 126,127, 99, 108,109,100, 101, 102, 103, 104, 105, 106, 107, 110, 111, 112, 29,30,31, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 113,114,115, 129, 130, 131],
    10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 27,28,29, 21, 22, 23, 24, 25, 26, 108,109,100, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 18,19,20, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 130, 101, 102, 103, 104, 105, 106, 107, 128,129, 110, 119,120,111, 112, 113, 114, 115, 116, 117, 118, 121, 122, 123, 124, 125, 126, 127, 73,74,75, 131],
    11: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 111,112,113, 74, 75, 76, 77, 71,72,73, 81, 82, 83, 84, 85, 86, 87, 88, 78,79,80, 92, 93, 94, 95, 96, 97, 98, 99, 89,90,91, 103, 104, 105, 106, 107, 108, 109, 110, 100,101,102, 114, 115, 116, 117, 118, 119, 120, 121,130,131, 122, 123, 124, 125, 126, 127, 128, 129],
    12: [0, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 11, 23, 24, 25, 15, 16, 17, 18, 19, 20, 21, 22, 34, 35, 36, 26, 27, 28, 29, 30, 31, 32, 33, 45, 46, 47, 37, 38, 39, 40, 41, 42, 43, 44, 56, 57, 58, 48, 49, 50, 51, 52, 53, 54, 55, 12, 13, 14, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    13: [0, 1, 2, 3, 4, 64, 65, 56, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 12, 13, 22, 23, 24, 5, 6, 7, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 67, 57, 58, 59, 60, 61, 62, 63, 75, 76, 66, 119, 68, 69, 70, 71, 72, 73, 74, 117, 118, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 25, 26, 27, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    14: [0, 1, 2, 3, 4, 5, 6, 20, 21, 12, 10, 11, 117, 13, 14, 15, 16, 17, 18, 19, 115, 116, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 7, 8, 9, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 36, 37, 38, 109, 110, 111, 112, 113, 114, 106, 107, 108, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    15: [0, 23, 2, 3, 4, 5, 6, 7, 8, 31, 32, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 106, 24, 25, 26, 27, 28, 29, 30, 104, 105, 33, 36, 37, 38, 39, 40, 41, 42, 43, 34, 35, 44, 45, 46, 9, 10, 1, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 47, 48, 49, 98, 99, 100, 101, 102, 103, 95, 96, 97, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    16: [0, 42, 43, 34, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 95, 35, 36, 37, 38, 39, 40, 41, 93, 94, 44, 47, 48, 49, 50, 51, 52, 53, 54, 45, 46, 55, 56, 57, 1, 2, 3, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 58, 59, 60, 87, 88, 89, 90, 91, 92, 84, 85, 86, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    17: [0, 1, 2, 53, 54, 45, 6, 7, 8, 9, 10, 11, 12, 13, 3, 4, 5, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 84, 46, 47, 48, 49, 50, 51, 52, 82, 83, 55, 58, 59, 60, 61, 62, 63, 64, 65, 56, 57, 66, 14, 15, 16, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 67, 68, 69, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131],
    18: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 62, 63, 64, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 80, 81, 82, 65, 66, 69, 70, 71, 72, 73, 74, 75, 76, 67, 68, 77, 78, 79, 130, 131, 122, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 18, 112, 113, 114, 115, 116, 117, 118, 16, 17, 121, 111, 123, 124, 125, 126, 127, 128, 129, 119, 120],
    19: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 91, 92, 93, 54, 55, 56, 57, 58, 59, 51, 52, 53, 63, 64, 65, 66, 67, 68, 60, 61, 62, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 78, 79, 88, 89, 90, 122, 123, 124, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 69, 70, 71, 125, 126, 127, 128, 129, 130, 131],
    20: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 102, 103, 104, 43, 44, 45, 46, 47, 48, 40, 41, 42, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 51, 79, 80, 81, 82, 83, 84, 85, 49, 50, 88, 91, 92, 93, 94, 95, 96, 97, 98, 89, 90, 99, 100, 101, 124, 125, 126, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 86, 87, 78, 127, 128, 129, 130, 131],
    21: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 113, 114, 115, 32, 33, 34, 35, 36, 37, 29, 30, 31, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 40, 90, 91, 92, 93, 94, 95, 96, 38, 39, 99, 102, 103, 104, 105, 106, 107, 108, 109, 100, 101, 110, 111, 112, 126, 127, 128, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 97, 98, 89, 129, 130, 131],
    22: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 73, 74, 75, 21, 22, 23, 24, 25, 26, 18, 19, 20, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 128, 129, 130, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 29, 101, 102, 103, 104, 105, 106, 107, 27, 28, 110, 113, 114, 115, 116, 117, 118, 119, 120, 111, 112, 121, 122, 123, 124, 125, 126, 127, 108, 109, 100, 131],
    23: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 78, 79, 80, 74, 75, 76, 77, 89, 90, 91, 81, 82, 83, 84, 85, 86, 87, 88, 100, 101, 102, 92, 93, 94, 95, 96, 97, 98, 99, 111, 112, 113, 103, 104, 105, 106, 107, 108, 109, 110, 71, 72, 73, 114, 115, 116, 117, 118, 119, 120, 121, 124, 125, 126, 127, 128, 129, 130, 131, 122, 123]
}



solved_state = []
test = 13
for i in range(0,132):
    solved_state.append(i)
current_state = [solved_state[i] for i in MOVES[0]]
current_state = [current_state[i] for i in MOVES[3]]

if solved_state == current_state:
    print("solved!!")
else:
    print(current_state)