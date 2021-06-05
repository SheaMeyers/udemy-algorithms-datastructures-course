def matrix(n):

    result = []
    for _ in range(0, n):
        temp_list = []
        for _ in range(0, n):
            temp_list.append(None)
        result.append(temp_list)
    
    counter = 1
    startColumn = 0
    endColumn = n-1
    startRow = 0
    endRow = n-1

    while (startColumn <= endColumn and startRow <= endRow):
        # Top Row
        for i in range(startColumn, endColumn+1):
            result[startRow][i] = counter
            counter += 1
        startRow += 1
        
        # Right Column
        for i in range(startRow, endRow+1):
            result[i][endColumn] = counter
            counter += 1
        endColumn -= 1
        
        # Bottom Row
        for i in range(endColumn, startColumn-1, -1):
            result[endRow][i] = counter
            counter += 1
        endRow -= 1

        # Right Column
        for i in range(endRow, startRow-1, -1):
            result[i][startColumn] = counter
            counter += 1
        startColumn += 1

    return result
