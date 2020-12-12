import fractions

def solution(x, y):
    """Determines number of self replicating bomb cycles necessary to properly destroy target

    Args:
        x (str): m-type bomb count goal
        y (str): f-type bomb count goal

    Returns:
        str: number of generation cycles to blow up the target
    """
    m = int(x)
    f = int(y)
    counter = 0
    if fractions.gcd(m, f) != 1:
        return 'impossible'
    while True:
        if m < f:
            f, m = m, f
        counter += int(m/f)
        if m%f == 0:
            counter -= 1
            break
        m = m%f
    return str(counter)

# import fractions

# # We have one of each different style of a bomb (m, and f). In a generation, each type of bomb can create one of the other kind once. solution() tells us the smallest number of cycles possible to get from one of each to x of one bomb type and y of the other.
# def solution(x, y):
#     m = int(x)
#     f = int(y)
#     counter = 0
#     if fractions.gcd(m, f) != 1:  # because we have to start with (1, 1)
#         return 'impossible'
#     while True:
#         if m < f:
#             # both styles of bomb replicate the same way, regardless of syncing unit availability, so we can just swap sides to get the bigger number first
#             f, m = m, f
#         counter += int(m/f)
#         if m%f == 0:
#             counter -= 1  # (1, 1) doesn't count as a generation, it's given to us
#             break
#         m = m%f
#     return str(counter)

# import math

# def solution(x, y):
#     f, m = sorted((int(x), int(y)))
#     counter = -1
#     if math.gcd(m, f) != 1:
#         return 'impossible'
#     while f != 0:
#         counter += m // f
#         f, m = m % f, f
#     return str(counter)

print(solution('4', '7'))
print(solution('2', '1'))
print()
print(solution('1', '1'))
print(solution('5', '8'))
print(solution('2', '4'))
print(solution('6', '2'))
print(solution('1', '4'))
print(solution('2', '5'))
print(solution('5', '3'))
print(solution('7', '13'))
print(solution('6', '13'))
print(solution('100000000000000000', '3'))


