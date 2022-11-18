import sys
sys.path.insert(0,'..')
from pprint import pprint
from get_mac import get_mac
from requests import get, post
from nested_dict import nested_dict


myList = {
    "a": "apple",
    "b": "banana",
    "c": [
        "cherry",
        "cat"
    ]
}
pprint(myList)

print(get_mac())

response = get("https://my.serverabcdefg.com", fake=True, retry=1)
pprint(response.json())

board = nested_dict(2, list)
board[0][0] = "rook"
board[0][1] = "knight"
board[0][2] = "bishop"
board[0][3] = "queen"
board[0][4] = "king"
board[0][5] = "bishop"
board[0][6] = "knight"
board[0][7] = "rook"
board[1][0] = "pawn"
board[1][1] = "pawn"
board[1][2] = "pawn"
board[1][3] = "pawn"
board[1][4] = "pawn"
board[1][5] = "pawn"
board[1][6] = "pawn"
board[1][7] = "pawn"
pprint(board)

print(f"### end of {__file__} ###")