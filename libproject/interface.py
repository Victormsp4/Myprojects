def menu(title,cor):
    print('-'*(len(title)+6))
    print(f'\033[{cor}m{title:^{len(title)+6}}\033[0m')
    print('-'*(len(title)+6))

def linha(lenn = 30, color = 96):
    print(f'\033[{color}m-\033[0m'*lenn)

def txt(txt,cor):
    print(f'\033[{cor}m{txt}\033[0m')