import re
def remove_white_space(str):
    str = re.sub(r'[^\x00-\x7F]+',' ', str)
    str = str.replace('\n', ' ')
    str = str.replace('\r', '')
    str = str.replace('\t', '')
    str = ' '.join(str.split())
    return str

def title(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
            lambda mo: mo.group(0)[0].upper() +
            mo.group(0)[1:].lower(),
            s)
