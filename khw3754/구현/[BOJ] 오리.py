sound = input()
count = 0
fullSound = 'quack'

class duck:
    def __init__(self):
        self.sound = 'q'

    def getNext(self):
        return fullSound[len(self.sound) % 5]

    def addSound(self, s):
        self.sound += s
        return self.sound

duckList = []
for oneSound in sound:
    filteredDuck = list(filter(lambda x: x.getNext() == oneSound, duckList))
    if len(filteredDuck) == 0 and oneSound == 'q':
        duckList.append(duck())
    elif len(filteredDuck) == 0 and oneSound != 'q':
        count = -1
        break
    else:
        filteredDuck[0].addSound(oneSound)

notFinishedDuck = list(filter(lambda x: x.getNext() != 'q', duckList))
if count == -1 or len(notFinishedDuck) != 0:
    print(-1)
else:
    print(len(duckList))