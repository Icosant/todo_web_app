FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the do-do items list to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    todos = get_todos()
    print(todos)
    print("""this wil only be executed when script is run directly
    and not when it is imported from another script.""")

