

def give_crunch_label(label, crunch_label_by=5):
    if crunch_label_by is None:
        return label
    
    if type(label) == str:
        return give_crunch_label_single(label, crunch_label_by)
    elif type(label) == dict:
        new_dict = {}
        for key, item in label.items():
            new_dict[key] = give_crunch_label_single(item, crunch_label_by)
        return new_dict
    elif type(label) == list:
        new_list = []
        for s in label:
            new_list.append(give_crunch_label_single(s, crunch_label_by))
        return new_list


import re


def give_crunch_label_single(label, crunch_label_by):
    # Tokens = Wort inklusive nachfolgendem Trennzeichen (Leerzeichen oder "/")
    tokens = re.findall(r"[^ /]+[ /]?", label)

    # Aus "Mitteilungsblatt/Gemeindeblatt der Stadt" wird so:
    # ["Mitteilungsblatt/", "Gemeindeblatt ", "der ", "Stadt"]

    count = 0
    new_label_list = []
    for i, token in enumerate(tokens):
        count += len(token)
        ist_letztes = (i == len(tokens) - 1)
        if count > crunch_label_by and not ist_letztes:
            # Umbruch: Leerzeichen am Ende weg, "/" aber behalten
            new_label_list.append(token.rstrip(" ") + "<br>")
            count = 0
        else:
            new_label_list.append(token)
    return "".join(new_label_list)

if __name__ == "__main__":
    label = "1 - stimme überhaupt nicht zu"
    s = give_crunch_label(label, crunch_label_by=8)
    print(s)