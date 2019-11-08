# Common function.


def p_list(dict_success, dict_failure):
    success_percent_list = []
    for key in dict_success:
        if dict_success[key] + dict_failure[key] != 0:
            success_percent_list.append(
                dict_success[key] / (dict_success[key] + dict_failure[key]) * 100)
        else:
            success_percent_list.append(0)
    return success_percent_list
