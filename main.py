from os import listdir, path
from importlib import reload 

ROOT_DIR = path.dirname(path.abspath(__file__))
BASEDIR = ROOT_DIR + "/app"

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def print_list(target, name, parser=''):

    print('')
    print(name.center(20, '-'))

    for item in target:

        if not parser in item and not "__" in item:
            print(item)

    print(''.center(20, '-'))
    print('')

def runQuestion(category):

    questions = listdir(BASEDIR + '/' + category)

    print_list(questions, 'questions', parser='md')

    question = input('> ')

    if question in questions:

        print('')
        print('result'.center(20, '-'))

        try:
            module = getattr(__import__(f'app.{category}', fromlist=[question[:-3]]), question[:-3])
            reload(module)
            target = getattr(module, question[0].upper() + question[1:-3])
            target.run(target)
            del module
        except Exception as e:
            print(e)

        print(''.center(20, '-'))
    else:

        print('\nNo such file!')

if __name__ == '__main__':

    categories = listdir(BASEDIR)

    while True:

        print('\nPlease type the category you want to see or type exit to exit')

        print_list(categories, 'categories', parser='.py')

        operation = input('> ')

        if operation == 'exit':
            break

        if operation in categories:
            runQuestion(operation)
            continue

        print("No such categories, please type again")
