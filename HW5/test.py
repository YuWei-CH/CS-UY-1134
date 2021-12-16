from ArrayStack import ArrayStack

def postfix_calculator():
    end = False
    operators = "+-*/"
    variable_dict = {}
    while end == False:
        user_input = input("-->")
        if user_input == "done()":
            end = True
            break
        user_input = user_input.split()
        args_stack = ArrayStack()
        if len(user_input) == 1:
            try:
                print(int(user_input[0]))
            except:
                print(variable_dict[user_input[0]])
        else:
            equals = False
            ind_equals = None
            expression = None
            variable = None
            for i in range(len(user_input)):
                if user_input[i] == "=":
                    equals = True
                    ind_equals = i
            if equals:
                expression = user_input[ind_equals + 1:]
                variable = user_input[0]
            else:
                expression = user_input
            for token in expression:
                if token not in operators:
                    try:
                        arg = int(token)
                    except:
                        arg = variable_dict[token]
                    args_stack.push(arg)
                else:
                    arg2 = args_stack.pop()
                    arg1 = args_stack.pop()
                    if token == "+":
                        res = arg1 + arg2
                    elif token == "-":
                        res = arg1 - arg2
                    elif token == "*":
                        res = arg1 * arg2
                    elif token == "/":
                        if arg2 == 0:
                            raise ZeroDivisionError
                        else:
                            res = arg1 / arg2
                    args_stack.push(res)
            result = args_stack.pop()
            if not equals:
                print(result)
            else:
                print(variable)
                variable_dict[variable] = result

postfix_calculator()