# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -

    ALPH = "qwertyuiopasdfghjklzxcvbnm"

    txt = txt.lower()

    letters = {}

    for i in txt:
        if i in ALPH:
            if i in letters:
                letters [i] += 1
            else:
                letters[i] = 1
    return letters

    pass


def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -

    new_d = {}

    for key, value in d.items():
        if value in new_d.keys():
            del new_d[value]
        else:
            new_d[value] = key
    
    return new_d

    pass

'''def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    # - YOUR CODE STARTS HERE -

    #for key, value in d.items():
        #print(f"key:", key, "\nvalue:", value)
    new_d = {}

    for i in d.values():
        for key, value in i.items():
            if value in new_d.values():
                del new_d[key]
            else:
                new_d[key] = value
    #print(d)
    #print(new_d)
    for key, value in new_d.items():
        #print(f"key:", key, "\nvalue:", value)
        #print(value[2])
        value[2] += bonus
    #print(new_d)
    #print(d)
    

    d[year] = new_d

    return d
        
    pass'''
def employee_update(d, bonus, year):
    new_d = {}

    for i in d.values():
        for key, value in i.items():
            if value in new_d.values():
                del new_d[key]
            else:
                new_d[key] = value[:] 

    for key, value in new_d.items():
        value[2] += bonus

    d[year] = new_d

    return d

records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
(employee_update(records,7500,2022))

def run_tests():
    import doctest

    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace frequency with the name of the function you want to test
    #doctest.run_docstring_examples(frequency, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()

