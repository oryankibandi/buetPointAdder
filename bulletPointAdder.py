#! /usr/bin/python3

import pyperclip


text = pyperclip.paste()

print('initial text: ' + text)

lines = text.split(' ')
for i in range(len(lines)):
    lines[i] = '*' + lines[i] + '\n'

text = ' '.join(lines)
print('final text: ' + text)
pyperclip.copy(text)