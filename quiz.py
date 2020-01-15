import data, random

while True:
    
    try:
        selector = str(input(
            'Show-me (0) or tell-me (1)? : '
        ))
        
        if selector not in ['0', '1']:
            raise Exception('Enter 0 or 1.')
        else:
            selector = bool(int(selector))
        
        if selector:
            stText =  'Tell-Me'
            notasked = data.tellme[:]
        
        else:
            stText =  'Show-Me'
            notasked = data.showme[:]

        print('\n\n << ' + stText + ' Questions >>\n')


        while len(notasked) > 0:

            nextQ = random.choice(notasked)
            notasked.remove(nextQ)

            print('{} Q: {}\n'.format(stText, nextQ.question))

            answer = str(input('>>> '))

            if (nextQ.answer):
                print('\n    Answer: ' + nextQ.answer, end = '')
            input()
            
            print('--------\n')
        
        print('\n')
    
    except Exception as e:
        print('Error: ' + str(e))