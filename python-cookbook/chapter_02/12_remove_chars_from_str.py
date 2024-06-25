s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
print(s)
print(s.translate(remap))

import unicodedata, sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)

s1 = unicodedata.normalize('NFD', s)
print(s1)
print(s1.translate(cmb_chrs))
