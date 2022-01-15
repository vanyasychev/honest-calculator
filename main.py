def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        pass

    if string.isdigit():
        return True


def is_integer(s):
    if int(s) == float(s):
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = str()

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and is_integer(v):
        return True
    else:
        return False


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. " \
        "You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5,
            msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

operands = ["+", "-", "*", "/"]

memory = float()
result = float()
while True:
    print(msg_0)
    calc = input().split()
    x, operation, y = calc[0], calc[1], calc[2]

    if x == "M":
        x = memory

    if y == "M":
        y = memory

    if not is_digit(x) or not is_digit(y):
        print(msg_1)
        continue
    elif operation not in operands:
        print(msg_2)
        continue

    if operation in operands:
        check(float(x), float(y), operation)

        if operation == operands[0]:
            result = float(x) + float(y)
        elif operation == operands[1]:
            result = float(x) - float(y)
        elif operation == operands[2]:
            result = float(x) * float(y)
        elif operation == operands[3] and int(y) != 0:
            result = float(x) / float(y)
        else:
            print(msg_3)
            continue

        print(result)

        while True:
            print(msg_4)
            answer = input()

            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10

                    while True:
                        print(msg_list[msg_index])
                        answer = input()

                        if answer == "y":
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                else:
                    memory = result
            elif answer == "n":
                pass

            while True:
                print(msg_5)
                answer = input()

                if answer == "y":
                    break
                elif answer == "n":
                    break
                else:
                    continue

            if answer == "y":
                break
            else:
                break

        if answer == "y":
            continue
        else:
            break
