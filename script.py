import keyboard
import argparse
import win32clipboard

parser = argparse.ArgumentParser()
parser.add_argument('-hk','--hotkeys', help = 'turn hotkeys flag on',
        action='store_true')
args = parser.parse_args()

with open('data.txt', 'r') as myfile:
    data=myfile.read()
clipboard_flag = False
def update_data():
    win32clipboard.OpenClipboard()
    global clipboard_flag
    global clipboard
    clipboard_flag = True
    clipboard = win32clipboard.GetClipboardData()
    

words = []
w = ''

for c in data:
    if c == '<':
        words.append(w)
        w = c
    elif c == '>':
        w += c
        words.append(w)
        w = ''
    else:
        w += c
if not words:
    words = list(data)
def generate():
    for one_iteration in words:
        try:
            if  one_iteration.startswith('<'):
                #slicing element deleting < and > 
                x = one_iteration[1:-1]
                yield  x
            else:
                x =list(one_iteration)
                for r in x:
                    yield r
        except Exception:
            pass
generate_iter = generate()


def hotkeys_off():
    if not clipboard_flag:
        for one_iteration in data:
            yield  one_iteration
    else:
        for one_iteration in clipboard:
            yield one_iteration
one_symbol = hotkeys_off()


def control():
    #and do stuff
    if args.hotkeys :
        a = next(generate_iter)
        if len(a) == 1 :
            return keyboard.write(a)
        else:
            return keyboard.send(a)
    else:
        b = str(next(one_symbol))
        return keyboard.write(b)



def do():
    #bind keys
    keyboard.add_hotkey('q',lambda:control())
    keyboard.add_hotkey('w',lambda:control())
    keyboard.add_hotkey('e',lambda:control())
    keyboard.add_hotkey('r',lambda:control())
    keyboard.add_hotkey('t',lambda:control())
    keyboard.add_hotkey('y',lambda:control())
    keyboard.add_hotkey('u',lambda:control())
    keyboard.add_hotkey('i',lambda:control())
    keyboard.add_hotkey('o',lambda:control())
    keyboard.add_hotkey('p',lambda:control())


    keyboard.add_hotkey('a',lambda:control())
    keyboard.add_hotkey('s',lambda:control())
    keyboard.add_hotkey('d',lambda:control())
    keyboard.add_hotkey('f',lambda:control())
    keyboard.add_hotkey('g',lambda:control())
    keyboard.add_hotkey('h',lambda:control())
    keyboard.add_hotkey('j',lambda:control())
    keyboard.add_hotkey('k',lambda:control())
    keyboard.add_hotkey('l',lambda:control())
    keyboard.add_hotkey(';',lambda:control())
    keyboard.add_hotkey('\'',lambda:control())

    keyboard.add_hotkey('z',lambda:control())
    keyboard.add_hotkey('x',lambda:control())
    keyboard.add_hotkey('c',lambda:control())
    keyboard.add_hotkey('v',lambda:control())
    keyboard.add_hotkey('b',lambda:control())
    keyboard.add_hotkey('n',lambda:control())
    keyboard.add_hotkey('m',lambda:control())
    keyboard.add_hotkey(',',lambda:control())
    keyboard.add_hotkey('.',lambda:control())
    keyboard.add_hotkey('/',lambda:control())

    keyboard.add_hotkey('[',lambda:control())
    keyboard.add_hotkey(']',lambda:control())
    keyboard.add_hotkey('1',lambda:control())
    keyboard.add_hotkey('2',lambda:control())
    keyboard.add_hotkey('3',lambda:control())
    keyboard.add_hotkey('4',lambda:control())
    keyboard.add_hotkey('5',lambda:control())
    keyboard.add_hotkey('6',lambda:control())
    keyboard.add_hotkey('7',lambda:control())
    keyboard.add_hotkey('8',lambda:control())
    keyboard.add_hotkey('9',lambda:control())
    keyboard.add_hotkey('0',lambda:control())
    keyboard.add_hotkey('-',lambda:control())
    keyboard.add_hotkey('=',lambda:control())
    keyboard.add_hotkey(' ',lambda:control())
    keyboard.add_hotkey('\\',lambda:control())
    keyboard.add_hotkey('Ctrl+2',lambda:update_data())
start=False  
while True:
    if start is True:
         keyboard.wait('Ctrl+3')
         do()
         keyboard.wait('Ctrl+4')
         keyboard.unhook_all()
         continue
    #control + 3 to start "typing" control + 4 to stop    
    keyboard.wait('Ctrl+3')
    do()
    keyboard.wait('Ctrl+4')
    keyboard.unhook_all()
    #start again
    start = True
    continue
    #to wait ctrl+3



