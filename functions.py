# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# TODO_FILE_PATH = os.path.join(script_dir,'todo.txt')

TODO_FILE_PATH = "todo.txt"
def get_todo(filepath = TODO_FILE_PATH):    # use of default parameter in a function defination
    """
    Reads a text file and returens it's 
    content line by line as list of items.
    """
    with open(filepath, 'r') as local_file:
        todos = local_file.readlines()
    return todos


def write_todo( todo_list, filepath = TODO_FILE_PATH):
    """ 
    Writes a list to a text file line by line.
    """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todo_list)

''' This part is inculded to run the script independently.
when this function scripts is called by main it rans in the 
backgroung and the script content gets executed as they are called.
But if the script is ran independently then this particular block 
of code makes the scipt run as main script and exexutes the code
inside this block. '''
 
if __name__ == "__main__":
    print ("Hello")
    print(get_todo()) 
