import json
class Automaton:
    def __init__(self, states = None, alphabet = None, transitions = None, initial_state = '', final_states = None):
        self.__states = states or []
        self.__alphabet = alphabet or []
        self.transitions =  transitions or {}
        self.__initial_state = initial_state
        self.__final_states = final_states or []

    def get_states(self):
        return self.__states

    def get_alphabet(self):
        return self.__alphabet

    def get_transitions(self):
        return self.transitions

    def get_initial_state(self):
        return self.__initial_state

    def get_final_states(self):
        return self.__final_states

    def set_states(self, new_states):
        self.__states = new_states    

    def set_alphabet(self, new_alphabet):
        self.__alphabet = new_alphabet

    # def set_transitions(self, new_transitions):
    #     self.__transitions = new_transitions

    def set_initial_state(self, new_initial_state):
        self.__initial_state = new_initial_state

    def set_final_states(self, new_final_states):
        self.__final_states = new_final_states
    
    def __str__(self):
        return  'States: ' + ' '.join([str(elem) for elem in self.__states]) + ' \n' +  'Alphabet: ' + ' '.join([str(elem) for elem in self.__alphabet]) + ' \n' + 'Transitions: ' +  json.dumps(self.transitions) + ' \n' +'Initial state: ' + self.__initial_state + ' \n' + 'Final states: ' +  ' '.join([str(elem) for elem in self.__final_states])
               
    __repr__ = __str__

# <state> ::= <char>|<state><char>
# <char> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" |  "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" |
# "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d" | "e"
#  | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v"
# | "w" | "x" | "y" | "z"
# <is_final> ::= "1" | "0"
# <alphabet> ::= <char>
# <initial_state> ::= <state>
# <final_states> ::= <state>|<final_states><state>


#input file expained: first element in the file is the initial state, and then, line by line: first element is the state, the second validates
# whether the state is final or not, and from the third element we have tuples of label + the next state that the label leads to

a1 = Automaton()
with open('input.txt', "r") as f:
    for line in f:
        a1.set_states = a1.get_states().append(line.split()[0])
        for word in line.split()[2::2]:
            if word not in a1.get_alphabet():
                a1.set_alphabet = a1.get_alphabet().append(word)
        a1.transitions[str(line.split()[0])] =  dict(zip(line.split()[2::2], line.split()[3::2]))
        a1.set_initial_state(a1.get_states()[0]) 
        if line.split()[1] == '1' :
            a1.set_final_states = a1.get_final_states().append(line.split()[0])
        
print(a1)