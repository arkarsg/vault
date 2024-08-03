import os

def get_mds(rel_path):
    '''
    Returns all `.md` files in a list
    '''
    abs_path = os.path.abspath(rel_path)
    md_files = []
    for path, directories, files in os.walk(abs_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(path, file))
    return md_files
