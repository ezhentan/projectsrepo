import json
import datetime as dt

from itertools import islice

#Creating functions
def take(n, iterable):
    return dict(islice(iterable, n))

def adding_word(word): #add_word function for the user to confirm the input
    print(f'''
This is your word added: {word}
        ''')
    if word_low in words['dictionary']:
        word_sentence = words['dictionary'][word_low][0]
        choice = input(f'This is not a new word, and example sentence(s), {word_sentence}, has already been added. Press 1 for Yes to add an additional sentence, press 2 for No: ') #To let the user know that not only are there already sentences present, but also display the existing sentences.
        
        if choice == '1':
            sentence = input('Example sentence: ')
            amount = 1 #automatically adds 1 to the frequency count
            time_current = dt.datetime.now().strftime('%c')
            
            if sentence in words['dictionary'][word_low][0]: #sentence is then not added again to dictionary, but frequency count and revision time are updated
                words['dictionary'][word_low][1] += amount
                words['dictionary'][word_low][2] = time_current
            
            if sentence not in words['dictionary'][word_low][0]: #adding sentence to the dictionary
                words['dictionary'][word_low][0].append(sentence)
                words['dictionary'][word_low][1] += amount
                words['dictionary'][word_low][2] = time_current
    
        elif choice == '2':
            amount = 1
            time_current = dt.datetime.now().strftime('%c')
            words['dictionary'][word_low][1] += amount
            words['dictionary'][word_low][2] = time_current

        else:
            print('Invalid input. Please try again.')
            choice = input('An example sentence, {word_sentence}, has already been added. Press 1 for Yes, press 2 for No: ')
    
    else:
        sentence = input('Example sentence: ')
        amount = 1
        time_current = dt.datetime.today().strftime('%c')
        words['dictionary'][word_low] = [[sentence], amount, time_current] #assigns the new word as a new key in the dictionary, assigns the sentence, frequency count and time as its values

def wordcount(): #function to update amount and time in menu == '2'
    amount = 1
    time_current = dt.datetime.now().strftime('%c')
    for k in selected:
        selected_word = str(k)
    words['dictionary'][selected_word][1] += amount
    words['dictionary'][selected_word][2] = time_current
    return words

#storing the contents of the history.txt file into python
with open('history.txt') as f_contents:
    try:
        words = json.load(f_contents)
    except json.decoder.JSONDecodeError:
        print('json.decoder.JSONDecodeError. Possibly means an extra dictionary.')

#using the dictionary
menu = input('1-record new word and/or new sentence; 2-review word from revision history; q-quit: ')

while menu != 'q':
    if menu == '1':
        with open('history.txt', 'w') as f:
            word = input('Word: ')
            word_low = word.lower()
            adding_word(word_low)
            
            json.dump(words, f, indent = 2)

            menu = input('1-record new word and/or new sentence; 2-review word from revision history; q-quit: ')

    if menu == '2':
        f_review = open('history.txt')
        words = json.load(f_review)
        f_review.close()
        
        for v in words.values():
            all_words = v
            
        revision_option = input('t-revision time; n-revision times: ')
        if revision_option == 't':
            for v in all_words.values():
                new_time = dt.datetime.now().strptime(v[2], '%c')
                v[2] = new_time
          
            time_sort = dict(sorted(all_words.items(), key = lambda x:x[1][2], reverse = True))
            
            for v in time_sort.values():
                v[2] = v[2].strftime('%c')
            
            selected = take(1, time_sort.items())
            print('\n', selected)
            wordcount()

            print('''
Displayed above is the word that you have most recently revised. Would you like to see the next word in the list?''')
            choice = int(input('''Press 1 for Yes, press 2 for No: '''))
            print('')
            i = 1
            while choice != 2:
                if choice == 1:
                    i += 1
                    selected = take(i, time_sort.items())
                    selected_words = list(selected)
                    for k in selected:
                        selected_word = str(k)
                    try:
                        print({k:v for k, v in time_sort.items() if k in selected_words[i - 1]})
                        wordcount()
                        print('''
Would you like to see the next word?''')
                        choice = int(input('Press 1 for Yes, press 2 for No: '))
                        print('')
                    except IndexError:
                        break
                        print('Too many!')
                if i >= len(time_sort.keys()):
                    print('That\'s it!')
            words['dictionary'] = time_sort

            with open('history.txt', 'w') as f_update:
                json.dump(words, f_update, indent = 2)

        elif revision_option == 'n':
            word_sort = dict(sorted(all_words.items(), key = lambda x:x[1][1], reverse = False))
            selected = take(1, word_sort.items())
            print('\n', selected)
            wordcount()
            
            print('''
Displayed above is the word that you have revised the least frequently. Would you like to see the next word in the list?''')
            choice = int(input('''Press 1 for Yes, press 2 for No: '''))
            print('')
            i = 1
            while choice != 2:
                if choice == 1:
                    i += 1
                    selected = take(i, word_sort.items())
                    selected_words = list(selected)
                    for k in selected:
                        selected_word = str(k)
                    wordcount()
                    try:
                        print({k:v for k, v in word_sort.items() if k in selected_words[i - 1]})
                        print('''
Would you like to see the next word?''')
                        choice = int(input('Press 1 for Yes, press 2 for No: '))
                        print('')
                    except IndexError:
                        break
                        print('Too many!')
                    if i >= len(word_sort.keys()):
                        print('That\'s it!')
            words['dictionary'] = word_sort

            with open('history.txt', 'w') as f_update:
                json.dump(words, f_update, indent = 2)
        
        menu = input('1-record new word and/or new sentence; 2-review word from revision history; q-quit: ')
