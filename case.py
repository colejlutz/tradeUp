from skinWeapon import skin

class case:
    def __init__(self, name):
        self.name = name

        self.blueSkins = []
        self.blueSkinsCount = 0
        self.purpleSkins = []
        self.purpleSkinsCount = 0
        self.pinkSkins = []
        self.pinkSkinsCount = 0
        self.redSkins = []
        self.redSkinsCount = 0

        self.skinsTotalCount = 0

    case_rarity_order = {
    "Blue":3,
    "Purple":4,
    "Pink":5,
    "Red":6
    }

    def addSkin(self, skin):
        if skin.rarity == "Blue":
            self.blueSkins.append(skin)
            self.blueSkinsCount += 1
            self.skinsTotalCount += 1

        elif skin.rarity == "Purple":
            self.purpleSkins.append(skin)
            self.purpleSkinsCount += 1
            self.skinsTotalCount += 1

        elif skin.rarity == "Pink":
            self.pinkSkins.append(skin)
            self.pinkSkinsCount += 1
            self.skinsTotalCount += 1

        elif skin.rarity == "Red":
            self.redSkins.append(skin)
            self.redSkinsCount += 1
            self.skinsTotalCount += 1

    
