from collections import deque

o_priority = {
    # operator priority
    '(': 0,
    '+': 1,
    '-': 1,
    ')': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '^': 3

}


def rpn(string):
    """
    :param string: string containing the phrase to be converted to Reverse Polish Notation.
    :return: queue containing the phrase in reverse RPN. Returns None if an error is encountered.
    """
    print('s')
    rpn_queue = deque()
    operator_stack = deque()
    current_number = ''
    number = False
    for c in string:
        if c in '0123456789.':
            number = True; current_number += c  # append number and continue

        elif c in '+-*/^%()':
            if number: rpn_queue.append(current_number); current_number = ''; number = False  # queue up number and reset

            match c:
                case '(':
                    operator_stack.append(c)

                case ')':
                    for i in range(len(operator_stack)-1, -1, -1):
                        if operator_stack[i] != '(':
                            if i == 0: print('Incorrect input'); return None  # throw error if never met '('
                            rpn_queue.append(operator_stack[-1])
                            operator_stack.pop()  # move operator from stack to queue
                        else:
                            operator_stack.pop()
                            break

                case _:
                    _continue = True
                    while _continue:
                        if len(operator_stack) > 0:
                            o1p = o_priority[c]; o2p = o_priority[operator_stack[-1]]  # priorities of current and last operator
                            if o1p < o2p or (o1p == o2p and c in '+-*/%'):
                                rpn_queue.append(operator_stack[-1]); operator_stack.pop()  # move operator from stack to queue
                            else: _continue = False
                        else: _continue = False

                    operator_stack.append(c)

        else:
            if number: rpn_queue.append(current_number); current_number = ''; number = False  # queue up number and reset
            """ There will be handler for functions here later """
            pass

    while operator_stack:  # empty the operator stack!
        rpn_queue.append(operator_stack[-1])
        operator_stack.pop()

    return rpn_queue


print(rpn('12+1*(2*3+4/5)'))
