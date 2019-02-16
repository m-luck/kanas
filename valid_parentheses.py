
def valid_parentheses(string):
    print(string) 
    ind_open = -1 # Index of open parentheses
    open_status = {} # Will track if the opened has been closed
    Q = [] # Will be a queue since closing parentheses naturally is LIFO
    opened = 0 # To check symmetry at end
    closed = 0 # To check symmetry at end
    open = False # Prevent a closing before opening
    if len(string) == 0:
        return True 
    for char in string:
        if char == "(":
            ind_open += 1
            open_status[ind_open] = "open"
            print("opening",ind_open)
            Q.append(ind_open)
            opened += 1
            open = True
        elif char == ")":
            closed += 1
            if open == False:
                return False
            if len(Q) != 0:
                print("closing",Q[-1])
                open_status[Q[-1]] = "closed"
                del Q[-1] # Pop off queue
    if opened != closed:
        return False
            
    print(string, open_status)
     
    result = True
    for ind in open_status:
        result = False if open_status[ind] == "open" or ind == -1 else result
    return result
        
