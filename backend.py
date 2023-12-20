from collections import deque
import operator

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

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow
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

    if number: rpn_queue.append(current_number)

    while operator_stack:  # empty the operator stack!
        rpn_queue.append(operator_stack[-1])
        operator_stack.pop()

    return rpn_queue




def calculate(rpn_queue):
    """
    :param rpn_queue: queue containing phrase in reverse polish notation
    :return: float containing the calc result
    """
    if rpn_queue == None:
        return None

    number_stack = deque()
    operator_stack = deque()
    while rpn_queue:
        if rpn_queue[0] in '-+*/^%':
            if len(number_stack) > 1:
                number_stack[-2] = operators[rpn_queue[0]](number_stack[-2], number_stack[-1])
                number_stack.pop()
            else: 
                operator_stack.append(rpn_queue[0])
        else:
            number_stack.append(float(rpn_queue[0]))
        
        rpn_queue.popleft()

    while operator_stack:
        if len(number_stack) > 1:
            number_stack[-2] = operators[rpn_queue[0]](number_stack[-2], number_stack[-1])
            number_stack.pop()
        elif len(operator_stack) > 0:
            print(number_stack)
            print(operator_stack)
            return None

    return number_stack[0]

