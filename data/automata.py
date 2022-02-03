class FSA:
    number_of_states = 0
    alphabet_array = []
    transition_array = [[]]
    starting_state = -1
    accepted_states = []

    # parsers for complex strings
    def parse_alphabet(self, str_token):
        str_token = str_token.replace(' ', '')
        return str_token.split(',')

    def parse_accepted(self, str_token):
        str_token = str_token.replace(' ', '')
        str_token = str_token.split(',')
        
        for i in range(len(str_token)):
            str_token[i] = int(str_token[i])

        return str_token

    def parse_transition(self, str_token):
        str_token = str_token.replace(' ', '')
        str_token = str_token.replace('(', '')
        str_token = str_token.replace(')', '')
        return str_token.split(',')

    def transition_diagram (self, str_token):
        parsed_tokens = self.parse_transition(str_token)
        size = self.number_of_states
        new_matrix = [
            [' ' for x in range(size)] for y in range(size)
        ]
        
        for i in range(0, len(parsed_tokens)):
            token = parsed_tokens[i].split(':')
            current_state = int(token[0])
            next_state = int(token[1])

            new_matrix[current_state][next_state] = token[2]  
        return new_matrix

    def find_next_state (self, current_state, alphabet):
        for i in range(self.number_of_states):
            if i == current_state:
                for j in range(self.number_of_states):
                    current_alphabet = self.transition_array[i][j]
                    if current_alphabet == alphabet:
                        return j
        return -1    

    def find_transitions (self, current_state):
        transitions = []
        for j in range (self.number_of_states):
            current_alphabet = self.transition_array[current_state][j]
            if current_alphabet != ' ':
                data = str(j) + ':' + str(current_alphabet)
                transitions.append(data)

        return transitions

    #paramatized constructor
    def __init__(self, tokens):
        self.number_of_states = int(tokens[0])
        self.alphabet_array = self.parse_alphabet(tokens[1])
        self.transition_array = self.transition_diagram(tokens[2])
        self.starting_state = int(tokens[3])
        self.accepted_states = self.parse_accepted(tokens[4])
        return