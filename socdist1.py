def compute_D(blocks, lhs, rhs):

    options = []

    if len(blocks) != 0:
        options.append(len(blocks))

    if lhs > 0:
        options.append(lhs)

    if rhs > 0:
        options.append(rhs)

    return min(options) + 1

def add_cow(blocks, lhs, rhs):

    D = compute_D(blocks, lhs, rhs)

    largest_block = 0
    if len(blocks) > 0:
        largest_block = max(blocks)

    if largest_block >= (D * 2):
        # Split block into D and the rest
        blocks.append(D)
        blocks.append(largest_block - D)
        blocks.remove(largest_block)
    else:
        # Split block in half,  this will decrease D
        newD = int(largest_block / 2)
        blocks.append(newD)
        blocks.append(largest_block - newD)        
        blocks.remove(largest_block)

def solve_file(filename):
    N,data = open(filename).read().splitlines()
    
    blocks = data.split('1')
    gaps = []
    if len(blocks) == 1:
        lhs = int(N)
        rhs = 0
    elif len(blocks) == 2:
        lhs = len(blocks[0])
        rhs = len(blocks[-1])
    else:
        lhs = len(blocks[0])
        rhs = len(blocks[-1])   
        gaps = list(map(len, blocks[1:][:-1]))        

    add_cow(gaps, lhs, rhs)
    add_cow(gaps, lhs, rhs)
    
    return compute_D(gaps, lhs, rhs)


for i in range(1, 16):
    actual_result = solve_file(f'socdist1_tests/{i}.in')
    expected_result = open(f'socdist1_tests/{i}.out').read()
    print(f'socdist1_tests/{i}.in', actual_result, expected_result)

0000000