# Taken from Stack Overflow (http://stackoverflow.com/a/9340596/527489) 
# answer by Oleh Prypin (https://stackoverflow.com/users/241039/oleh-prypin)
#
# licensed under cc by-sa 3.0
# (http://creativecommons.org/licenses/by-sa/3.0/) 
# with attribution required
# (http://blog.stackoverflow.com/2009/06/attribution-required/)

import readline
import shlex

print('Enter a command to do something, e.g. `create name price`.')
print('To get help, enter `help`.')

while True:
    cmd, *args = shlex.split(input('> '))

    if cmd=='exit':
        break

    elif cmd=='help':
        print('...')

    elif cmd=='create':
        print('args: %s' % str(args))
        if len(args) == 1:
            name, cost = args
            cost = int(cost)
            # ...
            print('Created "{}", cost ${}'.format(name, cost))
        else:
            print("'create' cmd requires two arguments")
    # ...

    else:
        print('Unknown command: {}'.format(cmd))
