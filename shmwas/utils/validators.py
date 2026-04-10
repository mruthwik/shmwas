def validate_age(age):
    try:
        return int(age) > 0
    except:
        return False


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10