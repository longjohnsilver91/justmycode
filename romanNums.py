class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        inum = str(val)
        inumlen = len(inum)
        inumlist = [str(i) for i in inum]
        # Roman numbers for 4 digits
        if inumlen == 4:
            # Code for roman thousands
            if inumlist[0] is '1':
                inumlist[0] = 'M'
            if inumlist[0] is '2':
                inumlist[0] = 'MM'
            if inumlist[0] is '3':
                inumlist[0] = 'MMM'
            # Code for roman hundreds
            if inumlist[1] is '0':
                inumlist[1] = ''
            elif inumlist[1] is '1':
                inumlist[1] = 'C'
            elif inumlist[1] is '2':
                inumlist[1] = 'CC'
            elif inumlist[1] is '3':
                inumlist[1] = 'CCC'
            elif inumlist[1] is '4':
                inumlist[1] = 'CD'
            elif inumlist[1] == '5':
                inumlist[1] = 'D'
            elif inumlist[1] is '6':
                inumlist[1] = 'DC'
            elif inumlist[1] is '7':
                inumlist[1] = 'DCC'
            elif inumlist[1] is '8':
                inumlist[1] = 'DCCC'
            elif inumlist[1] is '9':
                inumlist[1] = 'CM'
            # Code for roman tens
            if inumlist[2] is '0':
                inumlist[2] = ''
            elif inumlist[2] is '1':
                inumlist[2] = 'X'
            elif inumlist[2] is '2':
                inumlist[2] = 'XX'
            elif inumlist[2] is '3':
                inumlist[2] = 'XXX'
            elif inumlist[2] is '4':
                inumlist[2] = 'XL'
            elif inumlist[2] is '5':
                inumlist[2] = 'L'
            elif inumlist[2] == '6':
                inumlist[2] = 'LX'
            elif inumlist[2] is '7':
                inumlist[2] = 'LXX'
            elif inumlist[2] is '8':
                inumlist[2] = 'LXXX'
            elif inumlist[2] is '9':
                inumlist[2] = 'XC'
            # Code for roman digits
            if inumlist[3] is '0':
                inumlist[3] = ''
            elif inumlist[3] is '1':
                inumlist[3] = 'I'
            elif inumlist[3] is '2':
                inumlist[3] = 'II'
            elif inumlist[3] is '3':
                inumlist[3] = 'III'
            elif inumlist[3] is '4':
                inumlist[3] = 'IV'
            elif inumlist[3] is '5':
                inumlist[3] = 'V'
            elif inumlist[3] is '6':
                inumlist[3] = 'VI'
            elif inumlist[3] is '7':
                inumlist[3] = 'VII'
            elif inumlist[3] is '8':
                inumlist[3] = 'VIII'
            elif inumlist[3] is '9':
                inumlist[3] = 'IX'


        # Roman numbers for 3 digits
        if inumlen == 3:
            # Code for roman tens
            if inumlist[0] is '0':
                inumlist[0] = ''
            elif inumlist[0] is '1':
                inumlist[0] = 'C'
            elif inumlist[0] is '2':
                inumlist[0] = 'CC'
            elif inumlist[0] is '3':
                inumlist[0] = 'CCC'
            elif inumlist[0] is '4':
                inumlist[0] = 'CD'
            elif inumlist[0] == '5':
                inumlist[0] = 'D'
            elif inumlist[0] is '6':
                inumlist[0] = 'DC'
            elif inumlist[0] is '7':
                inumlist[0] = 'DCC'
            elif inumlist[0] is '8':
                inumlist[0] = 'DCCC'
            elif inumlist[0] is '9':
                inumlist[0] = 'CM'
            # Code for roman digits
            if inumlist[1] is '0':
                inumlist[1] = ''
            elif inumlist[1] is '1':
                inumlist[1] = 'X'
            elif inumlist[1] is '2':
                inumlist[1] = 'XX'
            elif inumlist[1] is '3':
                inumlist[1] = 'XXX'
            elif inumlist[1] is '4':
                inumlist[1] = 'XL'
            elif inumlist[1] is '5':
                inumlist[1] = 'L'
            elif inumlist[1] == '6':
                inumlist[1] = 'LX'
            elif inumlist[1] is '7':
                inumlist[1] = 'LXX'
            elif inumlist[1] is '8':
                inumlist[1] = 'LXXX'
            elif inumlist[1] is '9':
                inumlist[1] = 'XC'
            # Code for roman digits
            if inumlist[2] is '0':
                inumlist[2] = ''
            elif inumlist[2] is '1':
                inumlist[2] = 'I'
            elif inumlist[2] is '2':
                inumlist[2] = 'II'
            elif inumlist[2] is '3':
                inumlist[2] = 'III'
            elif inumlist[2] is '4':
                inumlist[2] = 'IV'
            elif inumlist[2] is '5':
                inumlist[2] = 'V'
            elif inumlist[2] is '6':
                inumlist[2] = 'VI'
            elif inumlist[2] is '7':
                inumlist[2] = 'VII'
            elif inumlist[2] is '8':
                inumlist[2] = 'VIII'
            elif inumlist[2] is '9':
                inumlist[2] = 'IX'


        # Roman numbers for 3 digits
        if inumlen == 2:
            # Code for roman digits
            if inumlist[0] is '0':
                inumlist[0] = ''
            elif inumlist[0] is '1':
                inumlist[0] = 'X'
            elif inumlist[0] is '2':
                inumlist[0] = 'XX'
            elif inumlist[0] is '3':
                inumlist[0] = 'XXX'
            elif inumlist[0] is '4':
                inumlist[0] = 'XL'
            elif inumlist[0] is '5':
                inumlist[0] = 'L'
            elif inumlist[0] == '6':
                inumlist[0] = 'LX'
            elif inumlist[0] is '7':
                inumlist[0] = 'LXX'
            elif inumlist[0] is '8':
                inumlist[0] = 'LXXX'
            elif inumlist[0] is '9':
                inumlist[0] = 'XC'
            # Code for roman digits
            if inumlist[1] is '0':
                inumlist[1] = ''
            elif inumlist[1] is '1':
                inumlist[1] = 'I'
            elif inumlist[1] is '2':
                inumlist[1] = 'II'
            elif inumlist[1] is '3':
                inumlist[1] = 'III'
            elif inumlist[1] is '4':
                inumlist[1] = 'IV'
            elif inumlist[1] is '5':
                inumlist[1] = 'V'
            elif inumlist[1] is '6':
                inumlist[1] = 'VI'
            elif inumlist[1] is '7':
                inumlist[1] = 'VII'
            elif inumlist[1] is '8':
                inumlist[1] = 'VIII'
            elif inumlist[1] is '9':
                inumlist[1] = 'IX'

        # Roman numbers for 3 digits
        if inumlen == 1:
            # Code for roman digits
            if inumlist[0] is '0':
                inumlist[0] = ''
            elif inumlist[0] is '1':
                inumlist[0] = 'I'
            elif inumlist[0] is '2':
                inumlist[0] = 'II'
            elif inumlist[0] is '3':
                inumlist[0] = 'III'
            elif inumlist[0] is '4':
                inumlist[0] = 'IV'
            elif inumlist[0] is '5':
                inumlist[0] = 'V'
            elif inumlist[0] is '6':
                inumlist[0] = 'VI'
            elif inumlist[0] is '7':
                inumlist[0] = 'VII'
            elif inumlist[0] is '8':
                inumlist[0] = 'VIII'
            elif inumlist[0] is '9':
                inumlist[0] = 'IX'
        inum = ''.join(inumlist)
        return inum


    @staticmethod
    def from_roman(roman_num : str) -> int:
        rnum = roman_num
        rnum = rnum.replace('CD','400x')
        rnum = rnum.replace('CM','900x')
        rnum = rnum.replace('XL','40x')
        rnum = rnum.replace('IV','4x')
        rnum = rnum.replace('IX','9x')
        rnum = rnum.replace('XC','90x')
        rnum = rnum.replace('M','1000x')
        rnum = rnum.replace('C','100x')
        rnum = rnum.replace('D','500x')
        rnum = rnum.replace('L','50x')
        rnum = rnum.replace('X','10x')
        rnum = rnum.replace('V','5x')
        rnum = rnum.replace('I','1x +')
        rnum = rnum.split('x')
        rnum[-1] = 0
        rnumlist = [int(i) for i in rnum]

        return sum(rnumlist)