main_stack = []
min_stack = []

def push(weight):
    main_stack.append(weight)
    if not min_stack or weight <= min_stack[-1]:
        min_stack.append(weight)

def pop():
    if not main_stack:
        return
    weight = main_stack.pop()
    if min_stack and weight == min_stack[-1]:
        min_stack.pop()

def get_min():
    if not min_stack:
        return None
    return min_stack[-1]

while True:
    try:
        command = input().strip()
        if command.startswith("push"):
            _, weight_str = command.split()
            weight = int(weight_str)
            push(weight)
        elif command == "pop":
            pop()
        elif command == "min":
            result = get_min()
            if result is not None:
                print(result)
    except EOFError:
        break