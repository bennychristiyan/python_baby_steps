Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
word = "the weather is so nice today"
word[2]
'e'
word[3]
' '
>>> #variable[start:stop:step]
>>> word[0:3:1]
'the'
>>> word[0:3:2]
'te'
>>> word[4:10:1]
'weathe'
>>> word[4:11:1]
'weather'
>>> word[4:]
'weather is so nice today'
>>> word[4::2]
'wahri onc oa'
>>> word[:14]
'the weather is'
>>> word[0:14:1]
'the weather is'
>>> word[0:14]
'the weather is'
>>> word[::-1]
'yadot ecin os si rehtaew eht'
>>>word[27::-1]
'yadot ecin os si rehtaew eht'
