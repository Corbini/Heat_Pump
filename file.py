import pickle
from pathlib import Path


def load_obj(file_name):
    path = Path("data/" + file_name)
    with open(path, "rb") as handle:
        return pickle.load(handle)


def save_obj(obj, file_name):
    path = Path("data/" + file_name)
    with open(path, "wb") as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
