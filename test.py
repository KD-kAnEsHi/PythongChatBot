def ask_if_input_again(prompt, again = 4, input_prompt ="Would you like to enter another question: yes or no?"):
    print("Would you like to enter another question: yes or no?")
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes', 'yah', 'ya', 'yup'}:            # Check if the input is y, ye, or yes....
            return True
        if reply in {'n', 'no', 'nope', 'nah', 'na'}:                  # Check if the input is n, no, or nope....
            return False    
        
        print()
        print("Invalid user response, please try agains.")
        print(input_prompt)