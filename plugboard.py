
from CONSTANT import ALPHABET

class Plugboard:
    def __init__(self, setting: dict):
        self.setting = self.mapPlugboard(setting)
    
    # region Plugboard getters and setters
    def __getSetting(self):
        return self.__setting
    def __setSetting(self, setting: dict):
        self.__setting = setting
        
    setting = property(__getSetting, __setSetting)
    # endregion
    
    def mapPlugboard(self, plugboard_settings: str) -> dict:
        '''
        Mapping the plugboard settings to a dictionary,\n
        And check if the plugboard settings are valid.\n
        Each key is a letter in the plugboard, and the value is the letter that,
        it is mapped to.\n
        (for example, 'AB' -> 'A': 'B' and 'B': 'A')
        '''
        
        tempPBList = plugboard_settings.split()
        if len(tempPBList) > 10:
            raise ValueError(f"Plugboard settings contains too many settings({len(tempPBList)}>10): {plugboard_settings}")
        for i in range(len(tempPBList)):
            if len(tempPBList[i]) != 2:
                raise ValueError(f"Plugboard settings contains invalid settings: {plugboard_settings}")
        for c in "".join(tempPBList):
            if c not in ALPHABET:
                raise ValueError(f"Plugboard settings contains invalid character: {c}")
            if "".join(tempPBList).count(c) > 1:
                raise ValueError(f"Plugboard settings contains duplicate character: {c}")
        
        plugboard = {}
        
        for plug in tempPBList:
            plugboard[plug[0]] = plug[1]
            plugboard[plug[1]] = plug[0]
            
        for c in ALPHABET:
            if c not in plugboard:
                plugboard[c] = c
            
        return plugboard
        
    
    def getLetter(self, letter: str) -> str:
        return self.setting[letter]
    
    def __str__(self) -> str:
        return f"Plugboard: {self.setting}"
