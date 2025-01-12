def custom_email_validator(value):
    """
    Custom email validator.
    :param value:
    :return bool:
    """
    if not re.match(r'^[a-zA-Z][\w.-]+@gmail\.com$', value):
        logger.error("Enter a valid Gmail address that does not start with a digit.")
        print("Here")
        return False
    return True

def phone_number_validator(value):
    """
    Validates a phone number
    :param value:
    :return bool:
    """
    if value.isdigit():
        if value in ['6','7','8','9']:
            return True
    return False