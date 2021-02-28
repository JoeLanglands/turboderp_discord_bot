"""This is where the bot is daemonised and ran from."""

import sys
import os

import daemonise
from dk_bot import bot

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'auth_token')) as tokenfile:
    auth_token = tokenfile.read()

class DKbotDaemon(daemonise.daemon):
    def run(self):
        bot.run(auth_token)

if __name__=='__main__':
    bot_daemon = DKbotDaemon('/tmp/dkbot_daemon.pid')
    if len(sys.argv) == 2:
            if 'start' == sys.argv[1]:
                bot_daemon.start()
            elif 'stop' == sys.argv[1]:
                bot_daemon.stop()
            elif 'restart' == sys.argv[1]:
                bot_daemon.restart()
            else:
                print("Unknown command")
                sys.exit(0)
    else:
        print(f"Usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)