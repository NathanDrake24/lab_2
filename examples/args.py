def example(color):
    if color == "green":
        return "This is tree"
    elif color == "blue":
        return "This is sky"
    else:
        return "I don't know"


example = None
if example is None:
    print("It's nothing")
else:
    print("It's something")


def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}

my_cat = cat('Alise', 'Grey', 9)
print(my_cat)


def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}


my_cat = cat(color = 'Grey', age = 9, name = 'Alise')
print(my_cat)


def example_args(*args):
    print('Positional argument tuple:', args)

example_args()
example_args(1, 2, 4, 'argument')




