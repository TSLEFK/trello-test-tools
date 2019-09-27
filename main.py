# Check this documents https://pythonhosted.org/trello/index.html
#  and https://developers.trello.com/reference
from trello import TrelloApi
import pprint

TRELLO_APP_KEY = 
TRELLO_TOKEN = 
TRELLO_NAME = 

trello = TrelloApi(TRELLO_APP_KEY, TRELLO_TOKEN)

me = trello.members.get(TRELLO_NAME)

for board_id in me['idBoards']:
    board = trello.boards.get(board_id)
    print(board['name'])

