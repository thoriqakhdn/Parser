#TBA TAHAP 2 (Parser)
#input
sentence = input('input kalimat :')
tokens = sentence.lower().split()
tokens.append('EOS')

#symbol
non_terminals = ['S','N','V']
terminals = ['nakke','katte',"je'ne",'snggara','balla','anganre','anginung','nangai',"a'jappa", 'amma']

#parse table
parse_table ={}

parse_table[('S', 'nakke')] = ['N','V','N']
parse_table[('S', 'katte')] = ['N','V','N']
parse_table[('S', 'amma')] = ['N','V','N']
parse_table[('S', "je'ne")] = ['N','V','N']
parse_table[('S', 'snggara')] = ['N','V','N']
parse_table[('S', 'balla')] = ['N','V','N']
parse_table[('S', 'anganre')] = ['error']
parse_table[('S', 'anginung')] = ['error']
parse_table[('S', 'nangai')] = ['error']
parse_table[('S', "a'jappa")] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('N', 'nakke')] = ['nakke']
parse_table[('N', 'katte')] = ['katte']
parse_table[('N', 'amma')] = ['amma']
parse_table[('N', "je'ne")] = ["je'ne"]
parse_table[('N', 'snggara')] = ['snggara']
parse_table[('N', 'balla')] = ['balla']
parse_table[('N', 'anganre')] = ['error']
parse_table[('N', 'anginung')] = ['error']
parse_table[('N', 'nangai')] = ['error']
parse_table[('N', "a'jappa")] = ['error']
parse_table[('N', 'EOS')] = ['error']

parse_table[('V', 'nakke')] = ['error']
parse_table[('V', 'katte')] = ['error']
parse_table[('V', 'amma')] = ['error']
parse_table[('V', "je'ne")] = ['error']
parse_table[('V', 'snggara')] = ['error']
parse_table[('V', 'balla')] = ['error']
parse_table[('V', 'anganre')] = ['anganre']
parse_table[('V', 'anginung')] = ['anginung']
parse_table[('V', 'nangai')] = ['nangai']
parse_table[('V', "a'jappa")] = ["a'jappa"]
parse_table[('N', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idx_token = 0
symbol = tokens[idx_token]

# parsing process
while (len(stack) > 0):
    top = stack [len(stack) - 1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack: ', stack)
                stack.pop()

        else:
            print('error')
            break;
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack: ', stack)
    print()

# conclusion
print()
if symbol == 'EOS' and len(stack) == 0:
    print('Input string ', sentence, ' diterima, sesuai Grammar')
else:
    print('Error, input string: ', sentence, ', tidak diterima, tidak sesuai Grammar')

