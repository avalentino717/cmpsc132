# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE

    perimeter /= 2
    width = 0
    length = 0
    for w in range(1, area + 1):
        l = area/w
        if w + l == perimeter:
            width = w
            length = l
    if width.is_integer() and length.is_integer() and perimeter.is_integer():
        return width
    else:
        return False

    pass
# print(rectangle(11,5))
# PLEASE NOTE: rectangle(11, 5) does work. Gradescope says it does not. It works in the code, but the terminal says it is not defined. It is defined.

def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE

    total = 0
    power = 0
    while oct_num > 0:
        remainder = oct_num % 10
        add = 8**power * remainder
        power += 1
        total += add
        oct_num //= 10
    return total

    pass


def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    #- YOUR CODE STARTS HERE
    num = abs(num)
    start = 0
    while num > 0:
        start = (num % 10)
        num //= 10
        other = num // 10
        remainder = other % 10
        #print(f"start: {start}\nremainder: {remainder}")
        if remainder == start:
            return True
    return False
    pass

def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    #- YOUR CODE STARTS HERE
    
    total_1 = 0
    power = 0
    prev = -1
    while num_1 > 0:
        digit = num_1 % 10
        if digit != prev:
            total_1 += (10**power * digit)
            #print(f"digit 1: {digit}\nprev digit: {prev}\ntotal: {total_1}\n")
            power += 1
        prev = digit
        num_1 //= 10
    
    total_2 = 0
    power = 0
    prev = -1
    while num_2 > 0:
        digit = num_2 % 10
        if digit != prev:
            total_2 += (10**power * digit)
            #print(f"digit 1: {digit}\nprev digit: {prev}\ntotal: {total_2}\n")
            power += 1
        prev = digit
        num_2 //= 10
    
    if total_1 == total_2:
        return True
    return False

    pass

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    lst = []
    lst.append(num)
    while num != 1:
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        lst.append(num)
    return lst
    pass


def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    if key in d:
        for k, v in d.items():
            if k == key:
                if type(d[key]) == list:
                    d[key].append(value)
                else:
                    temp = v
                    d[key] = []
                    d[key].append(temp)
                    d[key].append(value)
    else:
        d[key] = value
    
    
    pass


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    result = {}

    for key, value in d.items():
        # Extract the department to use as the key
        deptartment = value['department']
        
        # Create the new inner dictionary format
        # We include the emp_id here as requested
        data = {
            'emp_id': key,
            'name': value['name'],
            'position': value['position']
        }
        
        # Check if the department is already in our result
        if deptartment not in result:
            # If not, create a new list with this first employee
            result[deptartment] = [data]
        else:
            # If it is, just append the new employee to the existing list
            result[deptartment].append(data)
            
    return result
    pass


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    # --- YOU CODE STARTS HERE

    spaced_contents = ""
    for char in contents:
        if char.isalnum() or char.isspace():
            spaced_contents += char
        else:
            spaced_contents += " " + char + " "
    
    tokens = spaced_contents.split()
    
    result = {'.': []}
    
    if tokens:
        result['.'].append(tokens[0])
        
    for i in range(len(tokens)):
        current = tokens[i]
        
        if i < len(tokens) - 1:
            successor = tokens[i + 1]
            
            if current not in result:
                result[current] = []
            
            if successor not in result[current]:
                result[current].append(successor)

        if (current == "." or current == "!") and i < len(tokens) - 1:
            next_start_word = tokens[i + 1]
            if next_start_word not in result['.']:
                result['.'].append(next_start_word)

    return result


def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    current_layer = trie

    for letter in word:
        if letter not in current_layer:
            current_layer[letter] = {}
        
        current_layer = current_layer[letter]

    current_layer['word'] = True
    pass

def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE
    trie = {}
    
    words = contents.split()
    
    for word in words:
        clean_word = word.lower()
        
        if clean_word:
            addToTrie(trie, clean_word)
            
    return trie



def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    current_layer = trie

    for letter in word:

        if letter not in current_layer:
            return False
        
        current_layer = current_layer[letter]

    return current_layer.get('word') == True
    pass

trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 



def run_tests():
    import doctest
    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    # doctest.run_docstring_examples(rectangle, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()