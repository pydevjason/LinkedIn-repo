def read_txt_file():
    start = True
    exit_program = "exit"
    while start:
        try:
            filename = input("What file would you like to read: ")
            if filename == exit_program:
                break    
            with open(filename, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("That file does not exist, try again") 
            continue
        except UnicodeDecodeError:
            print("I can only read txt files at this time :( sorry")
            continue
        start = False
read_txt_file()
        
