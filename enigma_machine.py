
from CONSTANT import *
from rotor import *
from reflector import *
from plugboard import *

class EnigmaMachine:
    def __init__(self, rotors: str, ring_settings: str, 
                 reflector: str, plugboard_settings: str, 
                 message: str):
        '''
        rotors: str -> for example, 'I II III'
        ring_settings: str -> for example, '01 01 01' or 'A A A'
        reflector: str -> for example, 'B'
        plugboard_settings: str -> for example, 'AV BS CG DL FU HZ IN KM OW RX'
        message: str -> for example, 'ENIGMA MACHINE TEST'
        '''
        self.rotors = [Rotor(r[0],r[1]) for r in self.mapRotors(rotors, ring_settings)]
        for rotor in self.rotors:
            rotor.setRotorStartingPos(rotor.current_pos)
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard_settings)
        self.message = self.validateMessage(message)
        self.__encryptedMessage = ''

    # region Getters and Setters
    def __getRotors(self):
        return self.__rotors
    def __getReflector(self):
        return self.__reflector
    def __getPlugboard(self):
        return self.__plugboard
    def __getMessage(self):
        return self.__message
    
    def __setRotors(self, rotors):
        self.__rotors = rotors
    def __setReflector(self, reflector: Reflector):
        self.__reflector = reflector
    def __setPlugboard(self, plugboard: Plugboard):
        self.__plugboard = plugboard
    def __setMessage(self, message: str):
        self.__message = message
    
    rotors = property(__getRotors, __setRotors)
    reflector = property(__getReflector, __setReflector)
    plugboard = property(__getPlugboard, __setPlugboard)
    message = property(__getMessage, __setMessage)
    # endregion    

    # region validation/map functions
    def mapRotors(self, rotors:str, ring_settings: str or int):
        '''
        Mapping the rotors names and ring settings to a list of tuples,\n
        And check if the rotor names and ring settings are valid,\n
        Each tuple contains the rotor type and the starting ring setting.\n
        (for example, 
        ('I II III', '01 02 03') ->[\n
                ('I'  , '01')\n
                ('II' , '02')\n
                ('III', '03')\n
                ]
        or
        ('I II III', 'A B C') ->[\n
                ('I'  , '01')\n
                ('II' , '02')\n
                ('III', '03')\n
                ]
        )
        '''
        self.validateRotors(rotors)
        ring_settings = self.validateRingSettings(ring_settings)
        
        rotor_list = []
        for i in range(2,-1,-1):
            rotor_list.append((rotors.split(" ")[i], ring_settings.split(" ")[i]))

        return rotor_list

    def validateRotors(self, rotors: str) -> None:
        if len(rotors.split(" ")) != 3:
            raise ValueError(f"Number of rotors is not 3: {rotors}")
        
        for r in rotors.split(" "):
            if r not in ROTOR_WIRINGS:
                raise ValueError(f"Rotor {r} is not valid")
     
    def validateRingSettings(self, ring_settings: str) -> str:
        if len(ring_settings.split(" ")) != 3:
            raise ValueError(f"Number of ring settings is not 3: {ring_settings}")

        temp = ring_settings.split(" ")
        if temp[0].isnumeric() and temp[1].isnumeric() and temp[2].isnumeric():
            for strNum in temp:
                intNum = 0
                for c in strNum:
                    if c.isdigit():
                        intNum = intNum * 10 + int(c)
                    else:
                        raise ValueError(f"Ring settings contains invalid character: {c}")
                
                if intNum not in range(1, 27):
                    raise ValueError(f"Ring setting {strNum} is not valid")
        elif temp[0] in ALPHABET and temp[1] in ALPHABET and temp[2] in ALPHABET:
            temp = [ring_settings.split(" ")[0], ring_settings.split(" ")[1], ring_settings.split(" ")[2]]
            ring_settings = ''
            for c in range(len(temp)):
                ring_settings += str(ALPHABET.index(temp[c]) + 1)
                if c != len(temp) - 1:
                    ring_settings += ' '
        else:
            raise ValueError(f"Ring settings contains invalid/mixed character: {ring_settings}")
                    
        return ring_settings
                      
    def validateMessage(self, message: str) -> str:
        '''
        Validate that the message contains only letters from the "alphabet", and spaces.\n
        And return the message in upper case.\n
        "alphabet" = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        '''
        
        for c in message:   
            if c not in ALLABC and c not in ''' 0123456789"'?!.,-()\n''':
                raise ValueError(f"Message contains invalid character: {c}")
        
        return message.upper()
    # endregion
   
    def __encryptDecryptLetter(self, letter):
        
        # input 
        scrumbled_letter = letter
        
        # input -> plugboard ->
        scrumbled_letter = self.plugboard.getLetter(scrumbled_letter)
        
        #############################################################################################################
        
        # plugboard -> rotor1
        scrumbled_letter = self.rotors[0].getLetter(scrumbled_letter)
        
        # rotor1 -> rotor2
        scrumbled_letter = self.rotors[1].getLetterFromRotor(self.rotors[0], scrumbled_letter)
        
        # rotor2 -> rotor3
        scrumbled_letter = self.rotors[2].getLetterFromRotor(self.rotors[1], scrumbled_letter)
        
        #############################################################################################################
        
        # rotor3 -> reflector ->
        scrumbled_letter = self.reflector.getReflectorLetter(self.rotors[2], scrumbled_letter)

        #############################################################################################################
        
        # reflector -> rotor3 ->
        scrumbled_letter = self.rotors[2].getReverseLetter(scrumbled_letter)
        
        # rotor3 -> rotor2
        scrumbled_letter = self.rotors[1].getReverseLetterFromRotor(self.rotors[2], scrumbled_letter)
        
        # rotor2 -> rotor1
        scrumbled_letter = self.rotors[0].getReverseLetterFromRotor(self.rotors[1], scrumbled_letter)
        
        # rotor1 -> ALPHABET
        scrumbled_letter = ALPHABET[self.rotors[0].wiring[0].index(scrumbled_letter)]
        
        #############################################################################################################
        
        # ALPHABET -> plugboard ->
        scrumbled_letter = self.plugboard.getLetter(scrumbled_letter)
        
        # plugboard -> output
        return scrumbled_letter
    
    def encryptDecryptMessage(self):
        encrypted_message = ""
        for letter in self.message:
            if letter not in ALPHABET:
                encrypted_message += letter
            else:   
                self.rotors[0].rotate()
                if self.rotors[0].wiring[1][-1] == self.rotors[0].notch:
                    self.rotors[1].rotate()
                if (self.rotors[1].wiring[1][0] == self.rotors[1].notch and 
                    self.rotors[0].wiring[1][-1] != self.rotors[0].notch):
                    self.rotors[2].rotate()
                    self.rotors[1].rotate()

                encrypted_message += self.__encryptDecryptLetter(letter)
                        
            # print(f"{letter} -> {encrypted_message}")
        self.__encryptedMessage = encrypted_message
        return encrypted_message
            
    def __str__(self) -> str:
        return f"\n\t------------------\n" \
               f"\t| Enigma Machine |\n" \
               f"\t------------------\n" \
               f"\nRotors: \n\t{self.rotors[0]}\n\t{self.rotors[1]}\n\t{self.rotors[2]}\n" \
               f"{self.reflector}\n" \
               f"{self.plugboard}\n" \
               f"\nMessage: \n{self.message}\n" \
               f"\nEncrypted Message: \n{self.__encryptedMessage}" \

