# Recitation Activity 1

def translate(translation, msg):
    """
        >>> translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """     
    # -- YOUR CODE STARTS HERE
    pass
    new_msg = ''
    new_msg_lst = msg.lower().split()
    temp_list = []

    for i in new_msg_lst:
        '''if i in translation:
            new_msg += (translation[i] + " ")
        else:
            new_msg += (i + " ")'''
        if i in translation:
            temp_list.append(translation[i])
        else:
            temp_list.append(i)
    new_msg = " ".join(temp_list)

    return (new_msg)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
