# reminder: dicts maintain insertion order only
# so can only add to new dict the sorted values to get around this

def sort_dict_by_value_looping(d: dict) -> dict:
    dict2 = {}

    sorted_values = sorted(d.values())
    for value in sorted_values:
        assc_key = [k for k,v in d.items() if v==value][0]
        dict2[assc_key] = d.get(assc_key)

    return dict2

def refactor_sort_dict_by_looping(d:dict) -> dict:
    sorted_dict = {}

    for value in sorted(d.values()):
        for key, _value in d.items():
            if _value == value:
                sorted_dict[key] = value
                break
    return sorted_dict

def sort_dict_by_value_pythonic(d: dict) -> dict:
    return {k: v for (k, v) in sorted(d.items(), key=lambda item: item[1])}
