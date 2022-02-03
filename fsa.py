import sys
import tkinter as tk
from data.automata import FSA

def tokenize(fsa_diagram):
    with open(fsa_diagram) as f:
        content = f.readline()

    tokens = content.split(';')
    return FSA(tokens)

def fetch_string(fsa_test):
    with open(fsa_test) as f:
        content = f.readline()
    return content
    
def check_if_legal (fsa, test_string):
    print('Analyzing the string: ' + test_string)

    current_state = fsa.starting_state
    accepted_states = fsa.accepted_states

    for i in range(len(test_string)):
        next_state = fsa.find_next_state(current_state, test_string[i])
        if next_state != -1:
            current_state = next_state

    for i in range(len(accepted_states)):
        if current_state == accepted_states[i]:
            return True

    return False

def is_accepted (current_state, accepted_states):
    for i in range(len(accepted_states)):
        if current_state == accepted_states[i]:
            return True
    return False

def lisp_automata (fsa):
    f = open('part2.lsp', 'w+')
    num_text = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", 
                "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE"]
    
    #create demo
    f.write("(defun demo()\n\t(setq fp (open \"theString.txt\" :direction :input))\n")
    f.write("\t(setq L (read fp \"done\"))\n\t(princ L)\n\t(FSA L 0)\n)\n\n")

    #create FSA
    f.write("(defun FSA (L S)\n\t(cond ((NULL L) NIL)\n")
    for i in range(len(fsa.accepted_states)):
        f.write("\t\t((EQUAL (FSA_EVAL L S) " + str(fsa.accepted_states[i]) + ")\n")
        f.write("\t\t\t(FORMAT T " + "\"" + r"\n~% Accepted" + "\"))\n")
    f.write("\t\t(T (FORMAT T " + "\"" + r"\n~% Declined" + "\"))\n")
    f.write("\t)\n)\n\n")
    
    #create FSA_EVAL
    f.write("(defun FSA_EVAL (L S)\n\t(print \"" + r"\n" + "\")\n\t(print L)\n")
    f.write("\t(FORMAT T \"" + r"~%  | current_state: ~d" + "\"  s)\n")
    f.write("\t(FORMAT T \"" + r"~%  | current_char: ~s" + "\" (CAR L))\n")
    f.write("\t(cond ((NULL L) S)\n")
    for i in range(fsa.number_of_states):
        f.write("\t\t((EQUAL " + str(i) + " S)\n\t\t\t(FSA_EVAL (CDR L) (") 
        f.write(num_text[i] + "_NEXT (CAR L)))\n\t\t)\n")
    f.write("\t\t(T S)\n\t)\n)\n")

    #create the state_next functions
    for i in range(fsa.number_of_states):
        f.write("(defun " + num_text[i] + "_NEXT (input)\n")
        f.write("\t(cond ((NULL input) NIL)\n")
        
        for j in range(len(fsa.alphabet_array)):
            next_state = fsa.find_next_state(i, fsa.alphabet_array[j])
            if next_state != -1:
                next_char = '' + fsa.alphabet_array[j]
                letter = next_char.upper()
                f.write("\t\t((EQUAL input `" + letter + ") ")
                f.write("(RETURN-FROM " + num_text[i] + "_NEXT " + str(next_state) + "))\n")

        f.write("\t)\n)\n\n")
    
    return

def main(argv):
    fsa_diagram = argv[0]
    test_file = argv[1]

    # create automata object
    fsa_automata = tokenize(fsa_diagram)
    fsa_test_string = fetch_string(test_file)

    # check test string
    is_legal = check_if_legal(fsa_automata, fsa_test_string)
    if is_legal: print('This string is legal under this FSA')
    else: print("This string is not legal under this FSA")

    # create lisp file according to automata 
    lisp_automata(fsa_automata)
    return


if __name__ == '__main__':
    main(sys.argv[1:])