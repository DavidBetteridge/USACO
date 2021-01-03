import math

class State:
    def __init__(self, N, lhs, gaps, rhs):
        self.N = N
        self.lhs = lhs
        self.gaps = gaps
        self.rhs = rhs

    def D(self):
        if len(self.gaps) > 0:
            return min(self.gaps) + 1
        else:
            return self.N

    def largest_gap(self):
        if len(self.gaps) > 0:
            biggest_gap = max(self.gaps)
        else: 
            biggest_gap = 0

        return biggest_gap            

    def __repr__(self):
        return f'{self.lhs} {self.gaps} {self.rhs} ({self.D()})'

def add_cow(state):

    D = state.D()
    largest_gap = state.largest_gap()

    if largest_gap >= (D * 2):
        # Split block into D and the rest
        state.gaps.append(D)
        state.gaps.append(largest_gap - D)
        state.gaps.remove(largest_gap)
    elif (len(state.gaps) == 0 and state.lhs >= state.rhs) or state.lhs >= D:

        # Special case!
        if len(state.gaps) == 0 and state.rhs == 0:
            state.rhs = state.lhs - 1
        else:
            state.gaps.append(state.lhs - 1)
        state.lhs = 0

    elif (len(state.gaps) == 0 and state.lhs < state.rhs) or state.rhs >= D:        
        state.gaps.append(state.rhs - 1)
        state.rhs = 0        

    else:
        # Split block in half,  this will decrease D
        newD = math.ceil(largest_gap / 2)
        state.gaps.append(newD - 1)
        state.gaps.append(largest_gap - newD )        
        state.gaps.remove(largest_gap)

    return State(state.N, state.lhs, state.gaps, state.rhs)

def solve_file(filename):
    N, data = open(filename).read().splitlines()
    
    blocks = data.split('1')

    if len(blocks) == 1:
        state = State(int(N), len(blocks[0]), [], 0)
    else:
        state = State(int(N), len(blocks[0]), list(map(len, blocks[1:][:-1])), len(blocks[-1]))

    state = add_cow(state)
    
    state = add_cow(state)

    return state.D()

def test(test_number):
    actual_result = solve_file(f'socdist1_tests/{test_number}.in')
    expected_result = open(f'socdist1_tests/{test_number}.out').read()
    print(f'socdist1_tests/{test_number}.in', actual_result, expected_result)

for i in range(1, 16):
    test(i)    
