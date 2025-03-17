# Importing Packaging:
import os 

# Welcoming Banner !
from pyfiglet import Figlet
f = Figlet(font='banner')
print('\n')
print(f.renderText('Thinking'))

# Main Script:
print('For Basic Boot: 1')
print('For Advanice Boot: 2')

User = int(input('Choice: '))

if User == 1:
    os.system('python Basic.py')
elif User == 2:
    os.system('python Advanice.py')
else:
    os.system('python test.py')
