import telepot
import sys
from telepot.delegate import per_chat_id, create_open
TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)
