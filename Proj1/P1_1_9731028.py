def main():
    # Reading The String
    str = input()

    # Opening dfa file and reading it
    f = open("DFA_Input_1.txt", "r")
    characters = f.readline().split()
    states = f.readline().split()
    state = f.readline().split()[0]
    final_states = f.readline().split()
    V = f.read().splitlines()
    f.close()

    # moving step by step with the dfa graph and characters of the input string
    for char in str:
        if char in characters:
            q = state + " " + char
            for d in V:
                if q in d:
                    state = d.split()[2]
                    break
        else:
            print("not accepted")
            exit(0)

    # Checking is the state we got is compatible with the final state or not
    if state in final_states:
        print("accepted")
    else:
        print("not accepted")


if __name__ == '__main__':
    main()
