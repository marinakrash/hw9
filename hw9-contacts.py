ACTION=True
contacts_book = {}

def add(name, phone):
    if name not in contacts_book.keys():
        contacts_book[name] = phone

def change(name, phone):
    if name in contacts_book.keys():
        new = {name:phone}
        contacts_book.update(new)
    else:
        print('Nothing to change')

def good_bye():
    a="Good bye!"
    global ACTION
    ACTION = False
    return a

def hello():
    a="How can I help you?"
    return a

def phone(name):
    return contacts_book[name]

def show_all():
    return contacts_book

OPERATIONS={'hello': hello, 'add': add, 'change': change, 'phone': phone, 'show all': show_all, 'good bye': good_bye,
            'close': good_bye, 'exit': good_bye}

def handle(operator):
    return OPERATIONS[operator]

def input_error(func):
    def inner(command):
        lcommand = command.lower()
        if lcommand in OPERATIONS.keys():
            result = func(command)
            return result
        else:
            try:
                lcommand = command.lower()
                commands = lcommand.split(' ')
                OPERATIONS[commands[0]]
                commands[1]
                commands[2]
            except ValueError:
                print('Command is not a string')
            except KeyError:
                print('Input valid command')
            except IndexError:
                print('Input correct data')
            else:
                result = func(command)
                return result
    return inner

@input_error
def command_checker(command):
    lcommand = command.lower()
    if lcommand in OPERATIONS.keys():
        handler = handle(lcommand)
        result = handler()
        return result
    else:
        lcommand = command.lower()
        commands = lcommand.split(' ')
        operator = commands[0]
        args = (commands[1], commands[2])
        handler = handle(operator)
        result = handler(*args)
        return result

if __name__ == '__main__':
    while ACTION:
        command = input ('Operator action: ')
        print(command_checker(command))




