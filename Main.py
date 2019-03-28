import re, pyperclip

print('This program is checks if content of your clipboard could be considered a strong password. \nYour clipboard content is:')

StrongPassword1 = re.compile(r'[QWERTYUIOPASDFGHJKLZXCVBNM]')
StrongPassword2 = re.compile(r'[qwertyuiopasdfghjklzxcvbnm]')
StrongPassword3 = re.compile(r'\d')

CheckedPassword = str(pyperclip.paste())

if len(CheckedPassword)>= 8:
    if StrongPassword1.findall(CheckedPassword)!= []:
        if StrongPassword2.findall(CheckedPassword) != []:
            if StrongPassword3.findall(CheckedPassword) != []:
                print('Strong password')
            else:
                print('Not strong password')
        else:
            print('Not strong password')
    else:
        print('Not strong password')
else:
    print('Not strong password')

print('\nFeel free to copy something new to your clipboard and check again')
end = input()
