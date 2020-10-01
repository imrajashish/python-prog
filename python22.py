#Write a Python program to generate (given an integer n) a square matrix filled with elements from 1 to n raised to the power of 2 in spiral order
#https://gist.github.com/Ray1988/6806c1b85af70388a277
def generateMatrix(n):
        if n<=0:
            return [] 

        matrix=[row[:] for row in [[0]*n]*n]
        
        row_st=0
        row_ed=n-1
        
        col_st=0
        col_ed=n-1
        current=1
        
        while (True):
            if current>n*n:
                break
            for c in range (col_st, col_ed+1):
                matrix[row_st][c]=current
                current+=1
            row_st+=1
            for r in range (row_st, row_ed+1):
                matrix[r][col_ed]=current
                current+=1
            col_ed-=1
            for c in range (col_ed, col_st-1, -1):
                matrix[row_ed][c]=current
                current+=1
            row_ed-=1
            for r in range (row_ed, row_st-1, -1):
                matrix[r][col_st]=current
                current+=1
            col_st+=1
        return matrix

print(list(generateMatrix(3)))

# Write a Python program to create a range for floating numbers.
#https://gist.github.com/axelpale/3e780ebdde4d99cbb69ffe8b1eada92c
def frange(x, y, jump=1.0):
    i = 0.0
    x = float(x)  # Prevent yielding integers.
    y = float(y)  # Comparison converts y to float every time otherwise.
    x0 = x
    epsilon = jump / 2.0
    yield x  # yield always first value
    while x + epsilon < y:
        i += 1.0
        x = x0 + i * jump
        yield x

print(list(frange(0.0, 1.0, 0.1)))
