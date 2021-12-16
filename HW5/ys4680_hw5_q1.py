from ArrayStack import ArrayStack

def postfix_calculator():

    while_continue = True
    variable_name = []
    variable_value = []

    while while_continue :
        a = input( "-->:" )
        lst = a.split()

        for i in range( len( lst ) ):
            try:
                float( lst[i] )
                lst[i] = int( lst[i] )
            except ValueError:
                pass
            try:
                import unicodedata
                unicodedata.numeric( lst[i] )
                lst[i] = int( lst[i] )
            except (TypeError, ValueError):
                pass

        if ('=' not in lst or lst[0] not in variable_name) and len(lst) > 2:
            for i in range(len(lst)):
                for j in range(len(variable_name)):
                    if lst[i] == variable_name[j]:
                        lst[i] = variable_value[j]
                        break

        if a == 'done()':
            while_continue = False
            break

        elif isinstance(lst[0],str) and '=' in lst:
            operators = '+-*/='
            exp_stack = ArrayStack()
            value_index = None
            if_update = False
            for i in lst:
                if isinstance(i,str) and i not in operators and i not in variable_name:
                    variable_name.append(i)
                elif i in variable_name:
                    for j in range(len(variable_name)):
                        if variable_name[j] == i:
                            value_index = j
                            if_update = True
                elif i == '=':
                    pass
                elif isinstance(i,int):
                    exp_stack.push( int( i ) )
                else:
                    temp2 = exp_stack.pop()
                    temp1 = exp_stack.pop()
                    if isinstance(temp2,str):
                        for i in range(len(variable_name)):
                            if variable_name[i] == temp2:
                                temp2 = variable_value[i]
                    if isinstance( temp1, str ):
                        for i in range(len(variable_name)):
                            if variable_name[i] == temp1:
                                temp2 = variable_value[i]
                    if i == '+':
                        res = temp1 + temp2
                    elif i == '-':
                        res = temp1 - temp2
                    elif i == '*':
                        res = temp1 * temp2
                    elif i == '/':
                        if temp2 == 0:
                            raise ZeroDivisionError
                        else:
                            res = temp1 / temp2
                    exp_stack.push(res)
            if if_update:
                variable_value[value_index] = exp_stack.pop()
                if_update = False
                print(variable_name[value_index])
            else:
                variable_value.append(exp_stack.pop())
                print(variable_name[-1])

        elif isinstance(lst[0],int) and len(lst) > 2:
            operators = '+-*/'
            exp_stack = ArrayStack()
            for i in lst:
                if isinstance(i,int):
                    exp_stack.push( int( i ) )
                else:
                    temp2 = exp_stack.pop()
                    temp1 = exp_stack.pop()
                    if isinstance(temp2,str):
                        for i in range(len(variable_name)):
                            if variable_name[i] == temp2:
                                temp2 = variable_value[i+1]
                    if isinstance( temp1, str ):
                        for i in range(len(variable_name)):
                            if variable_name[i] == temp1:
                                temp2 = variable_value[i + 1]
                    if i == '+':
                        res = temp1 + temp2
                    elif i == '-':
                        res = temp1 - temp2
                    elif i == '*':
                        res = temp1 * temp2
                    elif i == '/':
                        if temp2 == 0:
                            raise ZeroDivisionError
                        else:
                            res = temp1 / temp2
                    exp_stack.push( res )
            result = exp_stack.pop()
            print(result)

        elif lst[0] in variable_name and len( lst ) == 1:
            for i in range(len(variable_name)):
                if variable_name[i] ==  lst[0]:
                    print(variable_value[i])

        elif isinstance(lst[0],int) and len(lst) == 1:
            print(lst[0])

            
'''
postfix_calculator()
'''