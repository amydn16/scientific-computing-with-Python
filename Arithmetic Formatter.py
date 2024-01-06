def arithmetic_arranger(*arg):

    # List of problems is always 1st argument
    problems = arg[0]

    # Concatenate problems into a string
    prob_str = ''
    for item in problems:
        prob_str = prob_str + item + ' '
    prob_str = prob_str.lower()

    # Split problems list into individual operations
    problems = [item.split(' ') for item in problems]

    # Check for optional second argument
    answer = None
    if len(arg) == 2:
        if arg[1] == True:
            answer = True
        
    # No more than 5 problems allowed
    if len(problems) > 5: 
        return("Error: Too many problems.")

    # Only addition & subtraction allowed
    if ('/' in prob_str) or ('x' in prob_str):
        return("Error: Operator must be '+' or '-'.")

    # Numbers must contain only digits
    if prob_str.islower() == True:
        return("Error: Numbers must only contain digits.")

    # Numbers must not be more than 4 digits long
    for item in problems:
        if (len(item[0]) > 4) or (len(item[2]) > 4):
            return("Error: Numbers cannot be more than four digits.")

    # Initialize 3 lines for operation, 1 more for optional result
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    # Add to each line
    for item in problems:

        # Use longest digit to right-justify lines
        max_len = max(len(item[0]), len(item[2]))
        new_l1 = 2*' ' + (max_len - len(item[0])) * ' ' + item[0]
        new_l2 = item[1] + ' ' + (max_len - len(item[2])) * ' ' + item[2]
        new_l3 = (max_len + 2) * '-'

        # Check if operation is last in the list
        if problems.index(item) < (len(problems) - 1):
            line1 = line1 + new_l1 + 4 * ' '
            line2 = line2 + new_l2 + 4 * ' '
            line3 = line3 + new_l3 + 4 * ' '
        elif problems.index(item) == (len(problems) - 1):
            line1 = line1 + new_l1
            line2 = line2 + new_l2
            line3 = line3 + new_l3

        # Display result if desired
        if answer == True: 
            if item[1] == "+":
                the_ans = str(int(item[0]) + int(item[2]))
            elif item[1] == "-":
                the_ans = str(int(item[0]) - int(item[2]))
            new_l4 = (len(new_l3) - len(the_ans)) * ' ' + the_ans

            # Check if operation is last in the list
            if problems.index(item) < (len(problems) - 1):
                line4 = line4 + new_l4 + 4 * ' '
            elif problems.index(item) == (len(problems) - 1):
                line4 = line4 + new_l4

    # Concatenate lines into a single string
    if answer == None:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3
    elif answer == True:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

    return(arranged_problems)

    

    
                
                
        
        
        
        
        

    
            

    
    

    

    
