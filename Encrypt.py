
code = {'A': '!','B': '@','C': '#','D': '$','E': '%','F': '^','G': '&','H': '*'
        ,'I': '1','J':'2','K':'3','L': '4','M': '5','N': '6','O': '7','P': '8',
        'Q': '9','R': '0','S': '!1','T': '@2','U': '#3','V':'$4','W': '()','X':';','Y': ':','Z': '...',
        'a':'11','b': '12','c':'13','d':'14','e':'15','f':'16','g':'17','h':'18','i':'19',
        'j':'20','k': '21','l':'22','m':'23','n':'39' ,'o':'24', 'p':'25', 'q':'26', 'r':'27', 's':'28','t':'29',
        'u':'30', 'v':'31','w': '40', 'x':'32', 'y': '33','z':'34', ' ': '35', '.': '36', ',':'37',':': '38'}

infile = open('info_security.txt','r')
file_to_encrypt = infile.read()
outfile = open('Encrypted_file.txt','w')

for i in file_to_encrypt:
    if i in code:
        Encrypted = code[i]
        outfile.write(Encrypted)
        print(Encrypted, end='')


    else:
        print('cannot be encrypted')

infile.close()
outfile.close()

















