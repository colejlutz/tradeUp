from skinWeapon import skin

class collection:
    def __init__(self, name):
        self.name = name

        self.graySkins = []
        self.graySkinsCount = 0
        self.lightBlueSkins = []
        self.lightBlueSkinsCount = 0
        self.blueSkins = []
        self.blueSkinsCount = 0
        self.purpleSkins = []
        self.purpleSkinsCount = 0
        self.pinkSkins = []
        self.pinkSkinsCount = 0
        self.redSkins = []
        self.redSkinsCount = 0

        self.skinsTotalCount = 0
        self.highestRarity = "Gray" #initialized to lowest Gray

        self.idNumber = -1 #unassigned is -1

collection_rarity_order = {
    "Gray":1,
    "Light Blue":2,
    "Blue":3,
    "Purple":4,
    "Pink":5,
    "Red":6
}

def compareCurrentHighestRarity(self, color):
    currentHighest = self.highestRarity
    if collection_rarity_order(color) > collection_rarity_order(self.highestRarity):
        self.highestRarity = color

def addSkin(self, skin):
    if skin.rarity == "Gray":
        self.graySkins.append(skin)
        self.graySkinsCount += 1
        self.skinsTotalCount += 1

    elif skin.rarity == "Light Blue":
        self.lightBlueSkins.append(skin)
        self.lightBlueSkinsCount += 1
        self.skinsTotalCount += 1
        compareCurrentHighestRarity(self, skin.rarity)

    elif skin.rarity == "Blue":
        self.blueSkins.append(skin)
        self.blueSkinsCount += 1
        self.skinsTotalCount += 1
        compareCurrentHighestRarity(self, skin.rarity)

    elif skin.rarity == "Purple":
        self.purpleSkins.append(skin)
        self.purpleSkinsCount += 1
        self.skinsTotalCount += 1
        compareCurrentHighestRarity(self, skin.rarity)

    elif skin.rarity == "Pink":
        self.pinkSkins.append(skin)
        self.pinkSkinsCount += 1
        self.skinsTotalCount += 1
        compareCurrentHighestRarity(self, skin.rarity)

    elif skin.rarity == "Red":
        self.redSkins.append(skin)
        self.redSkinsCount += 1
        self.skinsTotalCount += 1
        compareCurrentHighestRarity(self, skin.rarity)

    else:
        print("You are not supposed to be here. Rarity compare issue")

