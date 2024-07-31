text = 'Clarusway'
print(text[0])
text[:5] +'k' + text[-3:]
yeni_string = text[:5] + 'k' + text[-3:]
print(yeni_string)

var_string = 'Clarusway'
print(var_string.lower())
print(var_string)
var_string = 'ClarusWay'.lower()
print(var_string)

text = 'AaBbCe'
print(text. lower ())
text = text. lower()
print(text)

var_str = 'In God we Trust'
var_str. lower ()
print(var_str)

cumle = 'In God We Trust'
print(cumle. lower())
print (cumle)

yeni_cumle = cumle. lower()
print(yeni_cumle)

cumle = cumle. lower()
print (cumle)
print('t' in cumle)
print('R' in cumle)
print('trust' in cumle)
print('R'not in cumle)


text = 'www.clarusway.com'
print(text. endswith('.com' ))
print(text.startswith('http:'))

text= 'www.clarusway.com'
print(text.endswith('om'))
print(text.startswith('w'))

text = 'aabbcc'
print(text.startswith('a'))
print(text.startswith('aa'))
print(text.startswith('b',2))
print('abcdeabcde'.startswith('c',2,8))

email = "clarusway@clarusway.com is my e-mail address"
print (email.startswith("@", 9))
print(email.endswith("-", 10, 32)) 

text = 'a b c d'
print(len(text))

email = "clarusway@clarusway.com is my e-mail address"
print(email[10:32])

text ='www.clarusway.com'
print (text.endswith('.co'))
print(text.startswith('w.'))

text = 'abcdef'
print(text.startswith('b',-5))

text = """
Data preprocessing is an important task in text classification.
This program counts words in a sentence. It starts with space separated words."""
print("To count words in a sentence: ", text.count(" ") + 1)

text = "abcabcabe"
print(text. find('ca'))
print(text. find('klm' ))
print(text.rfind('a'))
print(text.index('ca'))

text = 'www.clarusway.com'
print(text.index('com'))
print(text.find('com'))

sentence = "I live and work in Virginia"
print(sentence. upper())
print(sentence. lower())
print(sentence.swapcase())
print(sentence) 