# runs the bot code, to run use this inside the src directory: pipenv run python main.py

# Importing Bot Class in bot.py
from bot import Bot

def main():
    plain_bot = Bot()
    plain_bot.run()

if __name__ == "__main__":
    main()
