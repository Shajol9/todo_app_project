import os

script_dir = os.path.dirname(os.path.abspath(__file__))
todo_file_path = os.path.join(script_dir,'todo.txt')


def get_todo(filepath = todo_file_path):    # use of default parameter in a function defination
    """
    Reads a text file and returens it's 
    content line by line as list of items.
    """
    with open(filepath, 'r') as local_file:
        todos = local_file.readlines()
    return todos


def write_doto( todo_list, filepath = todo_file_path):
    """ 
    Writes a list to a text file line by line.
    """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todo_list)

