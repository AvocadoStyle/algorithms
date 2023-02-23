# def clean_robot(R):
#     N = len(R)
#     M = len(R[0])
#     dirty = '.'
#     blocking_obstacle = 'x'
#     cleaned = set()
#     pos_x = 0
#     pos_y = 0
#     direction_x = 0
#     direction_y = 1
#     cln_pos_counter = 0
#     while True:
#         if R[pos_x][pos_y] == dirty and (pos_x, pos_y) not in cleaned:
#             cleaned.add((pos_x, pos_y))
#             cln_pos_counter += 1
#         next_x = pos_x + direction_x
#         next_y = pos_y + direction_y
#         if 0 <= next_x < N and 0 <= next_y < M and R[next_x][next_y] == dirty:
#             pos_x = next_x
#             pos_y = next_y
#         else:
#             temp_val_opposite = direction_x
#             direction_x = direction_y
#             direction_y = -temp_val_opposite
#             next_x = pos_x + direction_x
#             next_y = pos_y + direction_y
#             if 0 <= next_x < N and 0 <= next_y < M and R[next_x][next_y] == dirty and (next_x, next_y) not in cleaned:
#                 pos_x = next_x
#                 pos_y = next_y
#             else:
#                 break
#     return cln_pos_counter
#
# R1 = [
#     "...x..",
#     "....xx",
#     "..x...",
# ]
# R2 = [
#     "....x..",
#     "x......",
#     ".....x.",
#     "......."
# ]
# R3 = ['...X.', '.X..X', 'X...X', '..X..']
# cleaned = clean_robot(R2)
# print(cleaned)  # prints 8
#
#
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

def solution(S):
    # Implement your solution here
    min_strs = []
    set_of_characters = set()
    slice_string = ''
    for val in S:
        if val in set_of_characters:
            min_strs.append(slice_string)
            slice_string = val
            set_of_characters = set(slice_string)
        else:
            slice_string += val
            set_of_characters.add(val)

    min_strs.append(slice_string)
    return min_strs

print(solution('cycle'))