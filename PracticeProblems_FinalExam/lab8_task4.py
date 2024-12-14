################################### TASK 4 ###################################
### Starting code ###
def encrypt(message: str, shift: int) -> str:
    '''

    Args:
        message: provides a message to encrypt
        shift: int that is being used to shift the letters by a certain number in an alphabet

    Returns: shifted by a shift int each letter of initial message

    Examples:

        >>> encrypt("ATTACK AT NIGHTFALL",4)
        'EXXEGO EX RMKLXJEPP'
        >>> encrypt("HELLO WORLD", 1)
        'IFMMP XPSME'
        >>> encrypt("PYTHON", -5)
        'KTOCJI'
        >>> encrypt("DEFEND THE CASTLE", 7)
        'KLMLUK AOL JHZASL'

    '''
    
    assert type(message) == str, 'invalid argument type'
    assert type(shift) == int, 'invalid argument type'

    enc_message = ''

    for char in message:
        if char.isalpha():
            shifted = ord(char) + (shift % 26)
            if shifted > ord('Z'):
                shifted -= 26
            elif shifted < ord('A'):
                shifted += 26
            enc_message += chr(shifted)
        else:
            enc_message += char

    return enc_message.strip()
