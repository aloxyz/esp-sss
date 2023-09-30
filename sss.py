import random
#import traceback

FIELD = 2**6

def random_coefficients(degree, constant):
    '''
    Generate random coefficients of a polynomial with a specified constant value
    '''
    
    coeffs = [random.randint(0, FIELD) for _ in range(degree - 1)]
    coeffs.append(constant)

    return coeffs

def eval_polynomial(x, coeffs):
    '''
    Calculate the y value of a given point x and its coefficients
    '''
    
    y = 0

    for degree, coeff in enumerate(coeffs[::-1]):
        y += x ** degree * coeff
    
    return y

def gen_shares(k, n, secret):
    '''
    Generate shares of a secret by picking n random coefficients from the polynomial with a minimum threshold k
    '''

    coeffs = random_coefficients(k, secret)
    shares = []

    for i in range(1, n + 1):
        # Choose a random number 1 < x < FIELD-1
        x = random.randrange(1, FIELD)

        # Append the pair (x, p(x)) where p(x) is the evaluation of the polynomial in x with given coefficients
        shares.append((x, eval_polynomial(x, coeffs)))

    return shares

def lagrange_interpolation(x, points):
    '''
    Interpolate a point x with given points using the Lagrange method
    '''
    
    print('-----LAGRANGE-----')

    size = len(points)                  # Number of points
    
    xs, ys = zip(*points)
    
    sum = 0

    for i, xi in enumerate(xs):           # Summation loop
        prod = 1
        
        for j, xj in enumerate(xs):       # Product loop
            if j != i:
                prod *= (x - xj) / (xi - xj)
                print('({:d} - {:d}) / ({:d} - {:d}) = {:f}'.format(x, xj, xi, xj, prod))
    
        sum += ys[i] * prod
        print('{:d} * {:f} = {:f}'.format(ys[i], prod, sum))

    return round(sum)

def shamir_deconstruct(k, n, secret):
    '''
    Deconstruct the secret in n shares with a k treshold
    '''
    shares = gen_shares(k, n, secret)
    chosen_shares = []
    
    # random.sample(shares, k)
    for i in range(k):
        index = random.randrange(len(shares))
        chosen_shares.append(shares.pop(index))

    return chosen_shares

def shamir_reconstruct(shares):
    '''
    Find the secret given k random shares using Lagrange interpolation
    '''
    return lagrange_interpolation(0, shares)
