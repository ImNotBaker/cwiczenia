while True:
    a = input('Czy masz ochotę napić się piwa?    ').lower()
    if a=='tak':
        while True:
            b = input('18 jest?    ').lower()
            if b=='tak':
                print('Możesz!')
                
            elif b=='nie':
                print('Nie możesz')
                
            else:
                print('Odpowiedz tak lub nie' )
            break    
    elif a=='nie':
        print('No trudno')
        
    else:
        print('Odpowiedz tak lub nie')
    
        


        
        
        
