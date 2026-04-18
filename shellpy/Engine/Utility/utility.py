
def clean(data):
    return data.strip(' ')

def tokenizier(data,separator):
    xdata = data.split(separator)
    xdata = [clean(item) for item in xdata]
    return xdata