'''
Translation between English to Japanese
'''

from googletrans import Translator

translator = Translator()

string = input('input(enter \'q\' to exit): ')
while string != 'q':
    result = translator.detect(string)
    if result.lang == 'en':
        result = translator.translate(string, dest='ja')
        output = result.text
    elif result.lang == 'ja':
        result = translator.translate(string, dest='en')
        output = result.text
    else:
        output = 'It is neither English nor Japanese'
    print ('output: ' + output)
    string = input('input(enter \'q\' to exit): ')
