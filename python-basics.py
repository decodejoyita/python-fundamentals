# args is a positional/unnamed arguments without value 
# kwargs is a keyword/named arguments name and value also in form of a dictionary
# * args will pick up any number of unnamed arguments and **kwargs will pick up any number of named arguments in form of a dictionary


def multiply(numbers):
    result=1
    for n in numbers:
        result = result * n
    return result

def multiply_2(*numbers):
    result=1
    for n in numbers:
        result = result * n
    return result

#Dynamically take any number of function inputs using *args start with * to collect extra number of inputs

def function(a, b, *args, keyword=True, **kwargs):
    print(a,b)
    print(args)
    print(keyword)
    print(kwargs)

d={'param_a': 43, 'param_b': 42}

if __name__=='__main__':
    print(multiply([4,2]))
    print(multiply_2(4,2,5)) #added a star in front of argument numbers. now no need to pass numbers in form of a list 
    function(1,2,3,4, param=21)
    #While unpacking add a single * and ** to the arguments
    #*[5,3,4] is returning values 
    #**d is returning params
    function(1, 2, *[5, 3, 4], param = 42, **d)
    function(1, 2, [5, 3, 4], param = 42, **d)
    
        
        