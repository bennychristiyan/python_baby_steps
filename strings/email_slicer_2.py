Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "the word is nice today"
>>> word[-1]
'y'
>>> word[-2]
'a'
>>> word[-14]
' '
>>> word.index("word")
4
>>> word.index("today")
17
>>> word[word.index("word"):word.index("today")]
'word is nice '
>>> word[word.index("word"):word.index("e")]
''
