
def scale(array):
    array = array.astype('float32')
    array = array / 255.0
    array = array - 0.5
    array = array * 2.0
    return array
