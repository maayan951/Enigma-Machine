

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALLABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

ROTOR_WIRINGS = { 
    'I'   : ['EKMFLGDQVZNTOWYHXUSPAIBRCJ',      # Enigma I
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],     # Permutate
        
    'II'  : ['AJDKSIRUXBLHWTMCQGZNPYFVOE',      # Enigma I
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],     # Permutate
      
    'III' : ['BDFHJLCPRTXVZNYEIWGAKMUSQO',      # Enigma I 
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],     # Permutate
    
    'IV'  : ['ESOVPZJAYQUIRHXLNFTGKDCMWB',      # M3 Army
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],     # Permutate
         
    'V'   : ['VZBRGITYUPSDNHLXAWMJQOFECK',      # M3 Army
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ']      # Permutate   
}

# used to determine when to rotate the next rotor
ROTOR_NOTCHES = {
    'I'   : 'Q',      # Next rotor steps when I moves from Q -> R
    'II'  : 'E',      # Next rotor steps when II moves from E -> F
    'III' : 'V',      # Next rotor steps when III moves from V -> W
    'IV'  : 'J',      # Next rotor steps when IV moves from J -> K
    'V'   : 'Z'       # Next rotor steps when V moves from Z -> A
}

REFLECTOR_WIRINGS = {   
    'Beta' : 'LEYJVCNIXWPBQMDRTAKZGFUHOS',     # Reflector Beta
    'Gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD',     # Reflector Gamma
    'A'    : 'EJMZALYXVBWFCRQUONTSPIKHGD',     # Reflector A
    'B'    : 'YRUHQSLDPXNGOKMIEBFZCWVJAT',     # Reflector B
    'C'    : 'FVPJIAOYEDRZXWGCTKUQSBNMHL',     # Reflector C
    'D'    : 'ENKQAUYWJICOPBLMDXZVFTHRGS',     # Reflector B Thin
    'E'    : 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'      # Reflector C Thin
}