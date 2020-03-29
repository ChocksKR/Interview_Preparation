def FirstRepeatedHash(string):
    h = {}  # Create empty hash

    # Traverse each characters in string
    # in lower case order
    for ch in str:

        # If character is already present
        # in hash, return char
        if ch in h:
            return ch;

            # Add ch to hash
        else:
            h[ch] = 0

    return '\0'

def FirstRepeatedOrderN(string):

    # An integer to store presence/absence
    # of 26 characters using its 32 bits.
    checker = 0

    pos = 0
    for i in string:
        val = ord(i) - ord('a');

        # If bit corresponding to current
        # character is already set
        if ((checker & (1 << val)) > 0):
            return pos

            # set bit in checker
        checker |= (1 << val)
        pos += 1

    return -1

# Driver code
string = "abcfdeacf"
i = FirstRepeatedOrderN(string)
if i != -1:
    print ("Char = ", string[i], " and Index = ", i);
else:
    print ("No repeated Char");