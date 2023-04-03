from playsound import playsound
import threading

class Circle():
    def __init__(self, obj, colour, sound, status, chances):
        self.obj = obj
        self.colour = colour
        self.sound = sound
        self.status = status
        self.chances = chances

    def music(self):
        playsound(self.sound)

    def change(self, colour, status):
        self.colour = colour
        self.status = status

    def choice(self, left_obj, right_obj, random):
        if random <= self.chances[0]:
            self.change('white', 0)
            left_obj.change('red', 1)
            threading.Thread(target=left_obj.music, daemon=True).start()
        elif random >= self.chances[0]+1 and random <= self.chances[1]:
            self.change('white', 0)
            right_obj.change('red', 1)
            threading.Thread(target=right_obj.music, daemon=True).start()
        else:
            threading.Thread(target=self.music, daemon=True).start()