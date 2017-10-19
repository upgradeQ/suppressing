import keyboard
#generator
def sup():
    for one_iteration in data:
        yield  one_iteration
#weird function name 
s888 = sup()

with open('data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

#bind keys
keyboard.add_hotkey('q',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('w',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('e',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('r',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('t',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('y',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('u',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('i',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('o',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('p',lambda:keyboard.write(str(next(s888),)))


keyboard.add_hotkey('a',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('s',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('d',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('f',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('g',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('h',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('j',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('k',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('l',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey(';',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('\'',lambda:keyboard.write(str(next(s888),)))

keyboard.add_hotkey('z',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('x',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('c',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('v',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('b',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('n',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('m',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey(',',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('.',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('/',lambda:keyboard.write(str(next(s888),)))

keyboard.add_hotkey('[',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey(']',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('1',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('2',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('3',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('4',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('5',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('6',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('7',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('8',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('9',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('0',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('-',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('=',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey(' ',lambda:keyboard.write(str(next(s888),)))
keyboard.add_hotkey('\\',lambda:keyboard.write(str(next(s888),)))


#TODO: exit when index out of range
while True :
    pass
