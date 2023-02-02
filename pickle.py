import sys
import os
import json
import pickle

status = {}
def get_status_count(filename):
    is_exists = os.path.exists('filename.pickle')

    global status

    if is_exists :
        with open('filename.pickle', 'rb') as handle:
            status = pickle.load(handle)

    if filename not in status.keys():
        status[filename] = 0

    status[filename] = status[filename] + 1
    result = status[filename]

    with open('filename.pickle', 'wb') as handle:
        pickle.dump(status, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return result

if __name__ == "__main__":
    filename = sys.argv[1]
    file_count = int(sys.argv[2])
    file_count_till_now = get_status_count(filename)
    if file_count_till_now == file_count:
        print("OK")
