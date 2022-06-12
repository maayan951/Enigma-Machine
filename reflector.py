
from CONSTANT import *
from rotor import *

class Reflector:
    def __init__(self, wiring: str):
        self.wiring = self.mapReflector(wiring)
    
    # region Reflector getters and setters
    def __getWiring(self):
        return self.__wiring
    
    def __setWiring(self, wiring: str):
        self.__wiring = wiring
        
    wiring = property(__getWiring, __setWiring)
    # endregion
     
    def mapReflector(self, reflector: str) -> str:
        '''
        Mapping the reflector name to the reflector wiring,\n
        And check if the reflector name is valid,
        Return the reflector wiring.\n
        (for example, 'Beta' -> 'LEYJVCNIXWPBQMDRTAKZGFUHOS')
        '''
        
        if reflector not in REFLECTOR_WIRINGS:
            raise ValueError(f"Reflector {reflector} is not valid")
        return REFLECTOR_WIRINGS[reflector] 
    
    def getLetter(self, letter: str) -> str:
        return self.wiring[ALPHABET.index(letter)]
    
    def getReflectorLetter(self, rotor: Rotor, letter: str) -> str:
        return self.getLetter(ALPHABET[rotor.wiring[1].index(letter)])
        
    def __str__(self) -> str:
        return f"Reflector: {self.wiring}"
