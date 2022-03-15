# bot code, to run use this: pipenv run python main.py

# Installing packages
from twitchio.ext import commands
import os

# Test function, just to get it working
def test():
    print(os.environ.get("BOT_PREFIX"))
    print("Hi my prefix is: " , os.environ.get("BOT_PREFIX"))

# Main function, everything runs through here
def main():
    test()

# Safety function
if __name__ == "__main__":
    main()
