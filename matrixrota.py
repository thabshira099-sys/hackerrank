def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    
    num = min(m, n) // 2
    
    for layer in range(num):
        elements = []
        for j in range(layer, n - layer):
            elements.append(matrix[layer][j])
       
        for i in range(layer + 1, m - layer - 1):
            elements.append(matrix[i][n - layer - 1])
       
        for j in range(n - layer - 1, layer - 1, -1):
            elements.append(matrix[m - layer - 1][j])
        
        for i in range(m - layer - 2, layer, -1):
            elements.append(matrix[i][layer])
        
        
        length = len(elements)
        rot = r % length
        rota_elements = elements[rot:] + elements[:rot]
        
        
        idx = 0
        for j in range(layer, n - layer):
            matrix[layer][j] = rota_elements[idx]
            idx += 1
        for i in range(layer + 1, m - layer - 1):
            matrix[i][n - layer - 1] = rota_elements[idx]
            idx += 1
        for j in range(n - layer - 1, layer - 1, -1):
            matrix[m - layer - 1][j] = rota_elements[idx]
            idx += 1
        for i in range(m - layer - 2, layer, -1):
            matrix[i][layer] = rota_elements[idx]
            idx += 1

   
    for row in matrix:
        print(*(row))

            