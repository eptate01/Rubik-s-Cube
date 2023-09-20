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

current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
solved_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

x = 0

current_state = [current_state[i] for i in MOVES[x]]
current_state = [current_state[i] for i in MOVES[x]]
current_state = [current_state[i] for i in MOVES[x]]
current_state = [current_state[i] for i in MOVES[x]]
#current_state = [current_state[i] for i in MOVES[x]]
temp = [solved_state[i] for i in MOVES[x+12]]
if current_state == temp:
    print("success")
else:
    print(current_state, temp)
    print("fail")