import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    #nacteni povolenych klicu
    with open("sequential.json", "r") as f:
        allowed_keys = json.load(f)["allowed_keys"]

    #overeni zda je zdany klic povoleny
    is field not in allowed_keys:
    return None

    #nacteni dat ze souboru file_name
    with open(file_path, "r") as f:
        data = json.load(f)

    # vraceni hodnoty pod zadanym klicem
    return data.get(field, None)



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential data:", sequential_data)
   # pass ????


if __name__ == '__main__':
    main()