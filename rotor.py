
from CONSTANT import *

class Rotor:
    def __init__(self, r_type: str, starting_pos: str):
        self.rotor_type = r_type
        self.current_pos = int(starting_pos)
        self.wiring = ROTOR_WIRINGS[r_type].copy()
        self.notch = ROTOR_NOTCHES[r_type]

    # region Rotor getters and setters  
    def __getRotorType(self):
        return self.__rotor_type
    def __getWiring(self):
        return self.__wiring
    def __getCurrentPos(self):
        return self.__current_pos
    def __getNotch(self):
        return self.__notch
    
    def __setRotorType(self, rotor_type: str):
        self.__rotor_type = rotor_type
    def __setWiring(self, wiring: list):
        self.__wiring = wiring
    def __setCurrentPos(self, current_pos: int):
        self.__current_pos = current_pos
    def __setNotch(self, notch: str):
        self.__notch = notch
    
    rotor_type = property(__getRotorType, __setRotorType)
    wiring = property(__getWiring, __setWiring)
    current_pos = property(__getCurrentPos, __setCurrentPos)
    notch = property(__getNotch, __setNotch)
    # endregion

    def shiftRotor(self) -> None:
        '''
        Shift the string to the left by 1 characters.\n
        Return the shifted string.
        '''
        self.wiring[0] = self.wiring[0][1:] + self.wiring[0][:1]
        self.wiring[1] = self.wiring[1][1:] + self.wiring[1][:1]
        
    def setRotorStartingPos(self, pos: int) -> None:
        '''
        Set the starting position of the rotor.
        '''
        self.wiring[0] = self.wiring[0][pos-1:] + self.wiring[0][:pos-1]
        self.wiring[1] = self.wiring[1][pos-1:] + self.wiring[1][:pos-1]
        
    def getNotchNum(self) -> int:
        '''
        Return the notch number of the rotor.
        '''
        return self.wiring[0].index(self.notch)
    
    def rotate(self) -> None:
        '''
        Rotate the rotor by 1 character.
        '''
        self.shiftRotor()
        if self.current_pos % 26 == 0:
            self.current_pos = 1
        else:
            self.current_pos += 1
          
    def getLetter(self, letter: str) -> str:
        return self.wiring[0][ALPHABET.index(letter)]
    
    def getLetterFromRotor(self, rotor, letter: str) -> str:
        return self.getLetter(ALPHABET[rotor.wiring[1].index(letter)])
    
    def getReverseLetter(self, letter: str) -> str:
        return self.wiring[1][ALPHABET.index(letter)]
    
    def getReverseLetterFromRotor(self, rotor, letter: str) -> str:
        return self.getReverseLetter(ALPHABET[rotor.wiring[0].index(letter)])
    
    def __str__(self) -> str:
        return f"Rotor {self.rotor_type.ljust(3)} : {self.wiring} {self.current_pos} {self.notch}"
