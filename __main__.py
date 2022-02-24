import re

def string_re_check(string):
    return bool(re.search(r'[^a-zA-Z]', string))

def string_check(word):
    global loop
    try:
        if not string_re_check(word):
            if len(word) == 5:
                print(word)
                loop=0;
            else:
                print('errore lunghezza ' + str(len(word)))
        else:
                print('errore caratteri')
    except:
        print('errore generale')

def main():
    global loop
    loop=1
    while loop==1:
    
        # prendere in input la parola
        
        word=input('inserisci parola da 5 lettere: ')
        string_check(word)
        
    
    # indovinare la parola 'word'
    for i in range(6):
        test=input('inserisci tentativo: ')
        
    




if __name__ == '__main__':
    main()
