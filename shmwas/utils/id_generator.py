current_id = 1000

def generate_id():
    global current_id
    current_id += 1
    return current_id