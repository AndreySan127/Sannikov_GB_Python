def thesaurus(*args):
    # convert name list to dictionary like {A: [Alex..] , B:[Bob..]}
    out_dict = {}

    for name in args:

        if out_dict.get(name[0]):
            out_dict[name[0]].append(name)
        else:
            out_dict[name[0]] = [name]

    return out_dict


def thesaurus_adv(*args):
    # convert name list to dictionary like second_name[0]:{name[0]: name + second_name}
    out_dict = {}
    for elem in args:
        name, second_name = elem.split()
        if not out_dict.get(second_name[0]):
            out_dict[second_name[0]] = { name[0] : [elem] }
        elif not out_dict[second_name[0]].get(name[0]):
            (out_dict[second_name[0]])[name[0]] = [elem]
        else:
            (out_dict[second_name[0]])[name[0]].append(elem)

    return out_dict
print(thesaurus("Иван", "Мария", "Петр", "Илья"))