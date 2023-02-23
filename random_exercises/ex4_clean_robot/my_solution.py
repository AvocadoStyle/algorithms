def clean_robot(S):
    N = len(S)
    M = len(S[0])
    directions = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
    }
    # starts from 0, 0 and right step for the next_i and next_j
    i = 0
    j = 0
    direction = 'right'
    next_i = directions[direction][0]
    next_j = directions[direction][1]
    clean_counter = 1
    S[i] = S[i][0:j] + '1' + S[i][j + 1:]
    while True:
        # check validity
        if i+next_i >= N or j+next_j >= M or j+next_j < 0 or i+next_i < 0 or S[i+next_i][j+next_j] == 'x':
            # change direction
            if direction == 'right':
                # change direction from right -> down clockwise
                direction = 'down'
                next_i = directions[direction][0]
                next_j = directions[direction][1]
            elif direction == 'down':
                # change direction from down -> left clockwise
                direction = 'left'
                next_i = directions[direction][0]
                next_j = directions[direction][1]
            elif direction == 'left':
                # change direction from left -> up clockwise
                direction = 'up'
                next_i = directions[direction][0]
                next_j = directions[direction][1]
            elif direction == 'up':
                # change direction from up -> right clockwise
                direction = 'right'
                next_i = directions[direction][0]
                next_j = directions[direction][1]
        else:
            i += next_i
            j += next_j
            if S[i][j] == '2':
                return clean_counter
            elif S[i][j] == '1':
                # S[i][j] = '2'
                S[i] = S[i][0:j] + '2' + S[i][j+1:]
            elif S[i][j] == '.':
                clean_counter += 1
                # S[i][j] = '1'
                S[i] = S[i][0:j] + '1' + S[i][j+1:]

S1 = [
    "...x..",
    "....xx",
    "..x...",
]


R1 = [
    "...x..",
    "....xx",
    "..x...",
]
R2 = [
    "....x..",
    "x......",
    ".....x.",
    "......."
]
R3 = ['...X.', '.X..X', 'X...X', '..X..']
print(clean_robot(R1))