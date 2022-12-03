from imdb import IMDb
import random
print('''\033[95m
  __  __         _       ___                       _   _           
 |  \/  |_____ _(_)___  / __|_  _ __ _ __ _ ___ __| |_(_)_ _  __ _ 
 | |\/| / _ \ V / / -_) \__ \ || / _` / _` / -_|_-<  _| | ' \/ _` |
 |_|  |_\___/\_/|_\___| |___/\_,_\__, \__, \___/__/\__|_|_||_\__, |
                                 |___/|___/                  |___/ 

''')

class ChooseMovie(object):
    def __init__(self):
        self.cursor = IMDb()
        self.top250 = self.cursor.get_top250_movies()

    def __repr__(self):
        num = int(random.randint(0, 249))
        return str(f"{num}: {self.top250[num]}")


if __name__ == '__main__':
    print("\n", "\033[94m [*] I will suggest you","'", ChooseMovie(),"'","\n")

input("\033[91 Enter To Exit")
