def is_complete(numbers):
    try:
        if len(set(numbers)) != 9:
            return False
        if sorted(numbers)[0] != 1:
            return False
        for n in numbers:
            if type(n) != int:
                return False
        if sum(numbers) != 45:
            return False
    except TypeError:
        return False

    return True


def done_or_not(board):
    for row in board:
        if is_complete(row):
            return 'Try again!'
    return 'Finished'

def get_region(board, sr, sc):
    sr *= 3
    sc *= 3
    return board[sr][sc:sc + 3] + board[sr + 1][]
