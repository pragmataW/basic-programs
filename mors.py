import os

alphabet = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    'Ç' : '-.-..',
    'Ğ' : '--.-.',
    'İ' : '.-..-',
    'Ö' : '---.',
    'Ş' : '.--..',
    'Ü' : '..--',
    #!-----------
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    #!------------
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '\'' : '.----.',
    '!' : '-.-.--',
    '/' : '-..-.',
    '(' : '-.--.',
    ')' : '-.--.-',
    '&' : '.-...',
    ':' : '---...',
    ';' : '-.-.-.',
    '=' : '-...-',
    '+' : '.-.-.',
    '-' : '-....-',
    '_' : '..--.-',
    '"' : '.-..-.',
    '$' : '...-..-',
    '@' : '.--.-.',
    '¿' : '..-.-',
    '¡' : '--...-',
    ' ' : ' ',
    '\t' : '\t',
}

def translate(alphabet, pharase):
    try:
        i = 0
        while i <= len(pharase) - 1:
            char = pharase[i]
            print(alphabet[char], end = '')
            i += 1
    except KeyError:
        print(char, end='')
        i += 1
        temp = pharase[i:]
        if len(temp) >= 1:
            translate(alphabet, temp)
    print('')

check = 'a'
while (check != 'q') and (check != 'Q'):
    pharase = input('Mors alfabesinde yazmak istediğiniz ifadeyi giriniz... ')
    pharase = pharase.upper()

    translate(alphabet, pharase)

    check = input('Programı kapatmak için \'q\' karakterine, devam etmek için enter\'a basınız...  ')
    
    os.system('cls')