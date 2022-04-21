import tokenizer
import errorfinder
import stringmatching


def state(x):
    token_queue = tokenizer.token(x)

    curr_state = 1
    state_queue = []
    state_queue.append(1)
    for i in token_queue:
            if i[0] == 'smallerorequal' or i[0] == 'biggerorequal' or i[0] == 'bigger' or i[0] == 'smaller' or i[
                0] == 'equal' or i[0] == 'equalequal':
                i[0] = 'OPERATOR'
    #############################
    for i in range(0,len(token_queue)-2):
        if  token_queue[i][0] == 'NUM':
            if token_queue[i+1][0] == 'ID' or token_queue[i+1][0] == 'NUM':
                token_queue[i][0] = 'Nan'
                del(token_queue[i+1])
                i=i+1
    ################################

    counter = len(token_queue)
    #print(token_queue)

    while counter > 0:
        counter = counter - 1
        # print(curr_state)
        # print(token_queue)
        if curr_state == 1:
            if token_queue[0][0] == 'not':
                state_queue.append(1)
                token_queue.pop(0)

                continue
            elif token_queue[0][0] == 'ID' or token_queue[0][0] == 'NUM':
                token_queue.pop(0)
                state_queue.append(2)
                curr_state = 2
            else:
                token_queue.pop(0)
                state_queue.append(-1)
                curr_state = -1
                break;
        elif curr_state == 2:
            if token_queue[0][0] == 'OPERATOR' or  token_queue[0][0] == 'or' or token_queue[0][0] == 'and':
                token_queue.pop(0)
                state_queue.append(3)
                curr_state = 3
                continue
            else:
                token_queue.pop(0)
                state_queue.append(-1)
                curr_state = -1
                break
        elif curr_state == 3:
            if token_queue[0][0] == 'not':
                token_queue.pop(0)
                state_queue.append(3)
                continue
            elif token_queue[0][0] == 'ID' or token_queue[0][0] == 'NUM':
                token_queue.pop(0)
                state_queue.append(4)
                curr_state = 4
                continue
            else:
                token_queue.pop(0)
                curr_state = -1
                state_queue.append(-1)
                break
        elif curr_state == 4:
            if token_queue[0][0] == 'and':
                token_queue.pop(0)
                curr_state = 5
                state_queue.append(5)
                continue
            elif token_queue[0][0] == 'or':
                token_queue.pop(0)
                state_queue.append(6)
                curr_state = 6
                continue
            else:
                curr_state =-1
                state_queue.append(-1)
                break
        elif curr_state == 5:
            if token_queue[0][0] == 'not':
                token_queue.pop(0)
                state_queue.append(5)
                continue
            elif token_queue[0][0] == 'ID' or token_queue[0][0] == 'NUM':
                token_queue.pop(0)
                state_queue.append(7)
                curr_state = 7
                continue
            else:
                token_queue.pop(0)
                state_queue.append(-1)
                curr_state = -1
                break
        elif curr_state == 6:
            if token_queue[0][0] == 'not':
                state_queue.append(6)
                token_queue.pop(0)
                continue
            elif token_queue[0][0] == 'ID' or token_queue[0][0] == 'NUM':
                token_queue.pop(0)
                state_queue.append(7)
                curr_state = 7
                continue
            else:
                token_queue.pop(0)
                state_queue.append(-1)
                curr_state = -1
                break
        elif curr_state == 7:
            print(curr_state)
            if token_queue[0][0] == 'OPERATOR' or token_queue[0][0] == 'or' or token_queue[0][0] == 'and':
                token_queue.pop(0)
                state_queue.append(3)
                curr_state = 3
                continue
            else:
                token_queue.pop(0)
                state_queue.append(-1)
                curr_state = -1
                break
        else:
            curr_state = -1
            state_queue.append(-1)
            break


    # print(state_queue)
    return state_queue
