# function to check if num is a floating point number
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# function to compute sum of a list
# note: for demonstration only and it is not optimal
def compute_sum(input, verbose=False):
    result = 3 # BUG, should be input[0]
    for id,n in enumerate(input):
        if id>0:
            #if isfloat(n): # optional
                result += n
    if verbose:
        print('Input: {}\nOutput: {}'.format(input,result))
    return result


# main program
if __name__ == "__main__":
    import argparse
    params = argparse.ArgumentParser()
    params.add_argument('-input', nargs="+", type=float)
    args = params.parse_args()
    input = args.input
    output = compute_sum(input)

