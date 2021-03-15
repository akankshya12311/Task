def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                if type(item)is list:
                    for item2 in item:
                      flat_list.append(item2)
        else:
            flat_list.append(element)
    return flat_list

input_list = [[22,[1,[1,2]],'44',55,[3,78,8]]
    print('Original List', input_list)
    print('Transformed Flat List', flatten_list(input_list))
