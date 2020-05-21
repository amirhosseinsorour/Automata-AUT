import codecs


def main():
    # opening nfa file
    f = codecs.open("NFA_Input_2.txt", "r", "utf-8-sig")
    # making nfa file into dfa file
    dfa(f)
    f.close()


# this function returns next state due to nfa txt file which may have 'λ'and the given state & input
def next_states_with_l(state, char, V, characters):
    states = []
    if char in characters + ["λ"]:
        for d in V:
            q = state + " " + char
            if q in d:
                states.append(d.split()[2])
    return states


# this function returns a list which is λ_closure of a state
def l_closure(state, V, characters):
    states = []
    states.append(state)
    for s in states:
        states += next_states_with_l(s, "λ", V, characters)
    return states


# this function returns δ'(state , char) with the formula we already knew
def next_states_without_l(state, char, V, characters):
    l_cl = l_closure(state, V, characters)
    qi = []
    for q in l_cl:
        qi += next_states_with_l(q, char, V, characters)
    qi = list(set(qi))
    qj = []
    for q in qi:
        qj += l_closure(q, V, characters)
    return qj


# this function runs the main algorithm which converts nfa to dfa
def dfa(fin):
    characters = fin.readline().split()
    all_states = fin.readline().split()
    first_state = fin.readline().split()[0]
    final_states = fin.readline().split()
    Vin = fin.read().splitlines()

    fout = codecs.open("DFA_Output_2.txt", "w", "utf-8-sig")
    for char in characters:
        fout.write(char + " ")
    fout.write("\n")

    E = [{first_state}]
    Vout = []
    for state in E:
        for char in characters:
            next_state = []
            for q in state:
                next_state += next_states_without_l(q, char, Vin, characters)

            next_state = set(next_state)
            if next_state.__len__() == 0:
                next_state.add("∅")

            if next_state not in E:
                E.append(next_state)
            Vout.append(vtostring(state, next_state, char))

    for state in E:
        fout.write((etostring(state) + " "))
    fout.write("\n")

    fout.write(first_state + "\n")

    for x in Vin:
        if "λ" in x and first_state not in final_states:
            fout.write(first_state + " ")
            break
    for state in E:
        for final_state in final_states:
            if final_state in state:
                fout.write(etostring(state) + " ")
                break
    fout.write("\n")

    for v in Vout:
        fout.write(v + "\n")

    fout.close()


# this function makes string of a vertice of the dfa graph
def vtostring(state, next_state, char):
    str = ""
    for x in sorted(state):
        str += x
    str += " " + char + " "
    for x in sorted(next_state):
        str += x
    return str


# this function makes string of an edge of the dfa graph
def etostring(state):
    str = ""
    state = sorted(state)
    for q in state:
        str += q
    return str


if __name__ == '__main__':
    main()
