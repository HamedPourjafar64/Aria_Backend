from aria.apps.user.phone_validator.canada_area_codes import CanadaAreaCodes


def validate_phone_number(phone_number):
    no_parentheses = phone_number.replace('(', '').replace(')', '').replace(' ', '')
    no_dashes = no_parentheses.replace('-', '')
    no_country_code_sign = no_dashes.replace('+1', '')
    area_code = no_country_code_sign[0:3]
    if CanadaAreaCodes().check_area_code_validity(code=area_code) is False:
        return False
    if len(no_country_code_sign) < 10:
        return False
    return True
