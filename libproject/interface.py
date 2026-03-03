def menu(title,cor):
    print('-'*(len(title)+6))
    print(f'\033[{cor}m{title:^{len(title)+6}}\033[0m')
    print('-'*(len(title)+6))

def linha():
    print('-'*30)

def txt(txt,cor):
    print(f'\033[{cor}m{txt}\033[0m')