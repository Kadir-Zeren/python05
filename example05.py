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

text = 'ClaRusway'
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text)

print(text.replace('W', '***'))
print(text.replace('W', '***').lower())
print(text.replace('W', '**').lower().upper())


sentence = "I live and work in Virginia"
title_sentence = sentence.title()
print(title_sentence)
changed_sentence = sentence.replace("i",'+')
print(changed_sentence)
print(sentence) 

text = 'the better the family, the better the society'
text = text.title()
print (text)

sentence = "I live and work in Virginia"
swap_case = sentence.swapcase()
print(swap_case)
print(swap_case.capitalize()) 

text = 'S0d0me and G0m0re'
print(text. replace('0', 'o'))

isim = '    Ali    '
print(isim.strip())
meslek ='\n codder \t'
print(meslek.strip())
print(meslek.rstrip())

space_string = " listen first"
print(space_string.strip ( )) 

source_string = "interoperability"
print(source_string.strip("yi"))

text='abcdabcd'
print(text.strip('a'))
print(text.strip('ab'))
print(text.strip('ba'))
print(text.strip('bad'))

print(text.strip('badc'))
print(text)
print(text.strip('c'))

print(None or 1)

a = " "
b = "False"
c = True
d = ""
print(a or b or c and not d)

print("None or True and 1")

A = True
B = False
logic = (A or B) and (not A)
print(logic)

source_string = "interoperabilitv"
print(source_string.lstrip("in"))

space_string="      listen first       "
print(space_string.rstrip())

source_string = "interoperability"
print(source_string.strip("yi"))

source_string = "interoperability"
print(source_string.rstrip("yt"))

source_string = "interoperability"
print(source_string.rstrip("yt"))

source_string = "interoperability"
print(source_string.rstrip("ty"))

text = 'tyou can learn almost everything in pre-classz'
print(text.strip('tz'))

print(text.strip('tz'). upper())
print(text.rstrip('z'))
print(text.rstrip('z').lstrip('t'))
print(text.rstrip('z').lstrip('t'). upper())
print(text.rstrip('z').lstrip('t').upper())

text = text.rstrip('z').lstrip('t').upper()
print (text)


text = 'In God wee Trust'
print(text. replace( 'wee', 'we'))

text = 'In God wee Trust'
print(text.replace("ee", "e"))
text1 = text[:9]
text2 = text[10:]
print(text1 + text2)