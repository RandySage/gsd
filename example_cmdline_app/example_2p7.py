import readline
import shlex

print('Enter a command to do something, e.g. `create name price`.')
print('To get help, enter `help`.')

while True:
    cmd = shlex.split(raw_input('> '))
    #cmd = (raw_input('> ')).split(' ')
    print cmd

    if cmd[0]=='exit':
        break

    elif cmd[0]=='help':
        print('...')

    elif cmd[0]=='create':
        if len(cmd) < 2:
            print("'create' cmd requires two arguments")
        else:
            name, cost = args
            cost = int(cost)
            # ...
            print('Created "{}", cost ${}'.format(name, cost))

    # ...

    else:
        print('Unknown command: {}'.format(cmd))
