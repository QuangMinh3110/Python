def hex_dword(x):
    """ print hex with zero-padding for dword value
    Args:
        x (int/dword/): a 4 byte (dword) integer value

    Returns:
       [string]: a string which presents hex format of x (with out 0x prefix)
    Examples:
        hex_dword(65535) = '0000ffff'
        hex_dword(255) = '000000ff'
    """

    # YOUR CODE HERE
    print('hex_dword({}) = {}'.format(x, hex(x)[2::]))
    return print()
hex_dword(194)


def hex_byte(x):
    """ print hex with zero-padding for byte value
    Args:
        x (byte): a byte (BYTE) integer value
    Returns:
        [string]: a string which presents hex format of x (with out 0x prefix)

    Examples:
        hex_byte(32) = '20'
        hex_byte(10) - '0a'
    """

    # YOUR CODE HERE
    print('hex_dword({}) = {}'.format(x, hex(x)[2::]))
    return print()
hex_byte(32)



def hex_line(line):
    """ convert each byte in line (byte array) to character array ~ hex values (byte to byte) of that line
    Args:
        line (byte array): a byte array
    Returns:
        char array: ~ hex values (byte to byte) of that line"""

    # YOUR CODE HERE
    #hex_line(line) = "00 01 02 03 04 05 06 07 1F 09 41 0B 0C 0D 0E 0F"
    newline = []
    for i in range (len(line)):
        newline.append(("{0:0{1}X}".format(line[i],2)))
    print('line = {}'.format(line))
    print('hex_line(line) = {}'.format(' '.join(newline)))

hex_line([0, 1, 2, 3, 4, 5, 6, 7, 0x1F, 9, 0x44, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F])
def get_printable(s):
    """ convert byte array s to printable chracters array which any non-printable characters (ascii chracter < 0x20 in ASCII TABLE) be replaced by a dot chracter
    Args:
        s ([byte array]): a byte array to print

    Returns:
        [string]: a string which contains only printable chracters ( ASCIITABLE charcter from 0x20 )
    """
    output = ''

    # YOUR CODE HERE
    s2 = []
    s3 = []
    for i in range(len(s)):
        s2.append(chr(s[i]))
    for x in range(len(s2)):
        if 0 <= ord((s2[x])) <= 31:
            s2[x] = '.'
        s3.append((s2[x]))
    print('get_printable(s) = {}'.format(' '.join(s3)))
get_printable([0, 1, 2, 3, 4, 5, 6, 7, 0x1F, 9, 0x0A, 0x0B, 0x0C, 0x44, 0x0E, 0x0F])

'''def print_header():
    print ("Offset(h)  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  Decoded text")
print_header()'''

'''def print_data_line(offset, data_line):
    """ print a line of data mapping with header (in print_header())
    Args:
        offset (int): Offset of data (in file)
        data_line (byte array): data of file seperate in byte array (max = 16 members)
    Examples:
        offset = 32
        data = [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 41, 0B, 0C, 0D, 0E, 0F]
        print_header(offset,data)
        00000020   00 01 02 03 04 05 06 07 08 09 41 0B 0C 0D 0E 0F  .........A.....
    """
    # just sample, replace the following line by your code
    print("00000020   00 01 02 03 04 05 06 07 08 09 41 0B 0C 0D 0E 0F  .........A.....")
    # YOUR CODE HERE

def hex_view(data):
    """ print HEX VIEW (which )
    Args:
        data ([type]): [description]
    Examples:
        Offset(h)  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  Decoded text
        00000010   00 01 02 03 04 05 06 07 08 09 41 0B 0C 0D 0E 0F  .........A....
        00000010   00 01 02 03 04 05 06 07 08 09 42 0B 0C 0D 0E 0F  .........B....
        00000020   00 01 02 03 04 05 06 07 08 09 43 0B 0C 0D 0E 0F  .........C....
    """
    # just print a blank link
    print()

    print_header()

    # just print a blank link
    print()

    # YOUR CODE HERE

def hex_file(path):
    """ view hex content of a file (similar to week3#ex2)
    Args:
        path (string): path to file to view content
    """
    pass

sample_data = [n for n in range(255)]
hex_view(sample_data)'''
