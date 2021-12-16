from ArrayStack import ArrayStack
d=dict()
while True:
    user_input = str(input("\n--> "))
    if (user_input== "done"):
        break
    args_stack = ArrayStack()
    user_input=user_input.split()
    op="+-*/"
    isEqual= False
    if "=" in user_input:
        temp= user_input.pop(0)
        user_input.pop(1)
        isEqual=True
    for var in user_input:
        if var in op:
            second=args_stack.pop()
            first=args_stack.pop()
            if var== "+":
                result= first+second
            if var== "-":
                result= first-second
            if var== "*":
                result= first*second
            if var== "/":
                result= first/second
            args_stack.push(result)
        if var.isdigit():
            args_stack.push(var)
        else:
            args_stack.push(d[var])
    if isEqual:
        d[temp]=args_stack.pop()
        print(temp)
    else:
        print(args_stack.pop())    




            
       