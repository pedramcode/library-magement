import pickle
import os


def load_from_path(path=None):
    if path == None:
        raise Exception("Pass the path to load data")
    
    if not os.path.exists(path):
        with open(path, "wb") as _f:
            pickle.dump([], _f)

    with open(path, "rb") as _f:
        res = pickle.load(_f)
    
    return res


def save_to_path(data=None, path=None):
    if path == None:
        raise Exception("Pass the path to load data")
    if data == None:
        raise Exception("No data to get store")
    
    if not os.path.exists(path):
        raise Exception("Data file not found")

    with open(path, "wb") as _f:
        pickle.dump(data, _f)
