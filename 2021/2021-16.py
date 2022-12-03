import os
import numpy as np

def hex_to_bin(hex : str) -> int:
    '''
    Converts hexadecimal numbers to binary.
    '''
    int_val = int(hex, base=16)
    bin_val = bin(int_val)[2:]
    while len(bin_val) < 4:
        bin_val = '0' + bin_val
    return bin_val


class MessageParser():
    def __init__(self, input) -> None:
        self.message_gen = iter(input.strip())
        self.message_bin = self.input_to_binary(input)
        self.version_count = 0

    def input_to_binary(self, input):
        '''
        Converts all hexadecimal numbers to binary.
        '''
        bin = ''
        for hex in input:
            bin += hex_to_bin(hex)
        return bin

    def parse_meta(self, m : str) -> int:
        '''
        Parse binary digits for version number (first 3) and type ID (next 3).
        Updates version summation. 
        '''
        version = int(m[0:3], base=2)
        type_id = int(m[3:6], base=2)
        self.version_count += version
        return type_id

    def parse_literal_value(self, m) -> int:
        '''
        Parses message of 4 digits as long as leading binary digit is 1.
        '''
        m_parser = m
        digit_bin = ''
        parsed_len = 0
        more_digits = True
        while more_digits:
            if m_parser[0] == '0':
                more_digits = False
            if len(m_parser) >= 5:
                digit_bin += m_parser[1:5]
                parsed_len += 5
            m_parser = m_parser[5:]
        return int(digit_bin, base=2), parsed_len

    def parse_operator(self, m : str, len_type_id : str):
        '''
        Parses the content of an operator package. 
        Returns a tuple (subpackages, ind)
            subpackages : the contents of each of the subpackages
            ind : how many bits have been parsed in this package
        '''
        subpackages = []
        ind = 7 # meta and len_type_id

        if len_type_id:
            nbr_sub = int(m[ind:ind+11], base=2) # Get number of sub-packets.
            ind += 11
            for _ in range(nbr_sub):
                digit, parsed_len = self.parse_next(m[ind:])
                ind += parsed_len
                subpackages.append(digit)
        else: 
            len_sub = int(m[ind:ind+15], base=2) # Get length of sub-packets.
            ind += 15
            while ind < len_sub + 21:
                digit, parsed_len = self.parse_next(m[ind:])
                ind += parsed_len
                subpackages.append(digit)
        return subpackages, ind

    def parse_next(self, m : str):
        '''
        Parses the next package and returns the next content as tuple (digit,ind) or (res, ind)
            res/digit : base-10 number summarizing content
            ind : how many bits have been parsed in this package
        '''
        type_id = self.parse_meta(m)
        ind = 6

        # Literal value (type ID = 4)
        if type_id == 4: 
            digit, parsed_len = self.parse_literal_value(m[ind:])
            ind += parsed_len
            return digit, ind
        
        # Operator (type ID ≠ 4)
        else: 
            len_type_id = int(m[ind])
            subpackages, ind = self.parse_operator(m, len_type_id)

        op = type_id
        if op == 0:
            res = sum(subpackages)
        elif op == 1:
            res = np.prod(subpackages)
        elif op == 2:
            res = min(subpackages)
        elif op == 3:
            res = max(subpackages)
        elif op == 5:
            res = int(subpackages[0] > subpackages[1])
        elif op == 6:
            res = int(subpackages[0] < subpackages[1])
        elif op == 7:
            res = int(subpackages[0] == subpackages[1])
        return res, ind

def main():
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = f.read()
    
    mp = MessageParser(input)
    output = mp.parse_next(mp.message_bin)
    
    print('Ans A:', mp.version_count)
    print('Ans B:', output[0])

if __name__ == '__main__':
    main()