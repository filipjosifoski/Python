import sys
import pyperclip
PASSWORDS = {'email' : 'email12312412', 'blog' : 'blog523523', 'treto' : 'tretotO'}

if len(sys.argv) < 2:
    print("Usage: python3 main.py [account]")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for account' + account + 'copied to clipboard.')
else:
    print('Account' + account + ' not found ')

