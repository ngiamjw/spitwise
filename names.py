def names_sorted():
    original_list = []
    while True:
        info = input("names: ")
        info = info.split()
        if input(f"names are {info}, y/n") == 'y':
            original_list += info
            break

    result_dict = {value: {other_value: 0 for other_value in original_list if other_value != value} for value in original_list}
    return result_dict
