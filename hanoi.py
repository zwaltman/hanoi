"""
Implementation of a recursive solution to the 'Tower of Hanoi' problem.
"""

def move(from_stack, to_stack, aux_stack, h=None):
    """
    Moves last h elements from from_stack to to_stack
    
    Uses aux_stack as extra space for moving elements around 
    """    
    if h == None:
        h = len(from_stack)

    if h == 0: # 0 <= h <= 2: trivial cases
        pass
    elif h == 1:
        to_stack.append(from_stack.pop()) 
    elif h == 2: # base case 
        aux_stack.append(from_stack.pop()) 
        to_stack.append(from_stack.pop()) 
        to_stack.append(aux_stack.pop())
    elif h > 2: 
        # mimicking h==2 case, move all but bottom element of from_stack to aux_stack, 
        # move bottom element to to_stack, then move top portion to to_stack 
        move(from_stack, aux_stack, to_stack, h-1)  
        to_stack.append(from_stack.pop())
        move(aux_stack, to_stack, from_stack, h-1)

