import os
import pandas as pd
import numpy as np


def read_json(file_path:str, file_name:str):
    with open(file_path + file_name) as issue:
        issue_string = issue.read().replace("\n", "").replace("null", "0").replace("true", "True").replace("false", "False")
        issue_dict = eval(issue_string)
        return issue_dict

def convert_json_to_csv(file_path:str, save_path:str):
    row_list = []
    files = os.listdir(file_path)
    length = len(files)
    index = 1
    error = 0

    for file_name in files:
        try:
            issue_dict = read_json(file_path, file_name)
        except:
            print(f"read error at {index}")
            error += 1
            continue
        if issue_dict['success'] == 'False':
            continue
        temp_list = []
        for issue in issue_dict["issues"]:
            temp_list.append([issue['address'], issue['debug'], issue['description'], file_name[:-4], issue['function'], issue['lineno'], issue['title'], issue['type']])
        row_list.extend(temp_list)
        print(f"{index}/{length} file done.")
        index += 1

    row_numpy_array = np.array(row_list)
    columns = ['address', 'debug', 'description', 'name', 'function', 'lineno', 'title', 'type']
    df = pd.DataFrame(data = row_numpy_array, index = None, columns = columns)
    df.to_csv(save_path)
    print(f"convert complete, {error} out of {length} failed")


if __name__ == '__main__':
    convert_json_to_csv("./contract/eth/gamble_result/", "./scan_result/eth_gamble.csv")