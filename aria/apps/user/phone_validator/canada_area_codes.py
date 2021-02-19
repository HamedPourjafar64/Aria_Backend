class CanadaAreaCodes:
    area_codes = {
        '204': {
            'province': 'Manitoba'
        },
        '226': {
            'province': 'Ontario',
            'city': 'London'
        },
        '236': {
            'province': 'British Columbia',
            'city': 'Vancouver'
        },
        '249': {
            'province': 'Ontario',
            'city': 'Sudbury'
        },
        '250': {
            'province': 'British Columbia',
            'city': 'Kelowna'
        },
        '289': {
            'province': 'Ontario',
            'city': 'Hamilton'
        },
        '306': {
            'province': 'Saskatchewan',
        },
        '343': {
            'province': 'Ontario',
            'city': 'Ottawa'
        },
        '365': {
            'province': 'Ontario',
            'city': 'Hamilton'
        },
        '367': {
            'province': 'Quebec',
            'city': 'Quebec'
        },
        '403': {
            'province': 'Alberta',
            'city': 'Calgary'
        },
        '416': {
            'province': 'Ontario',
            'city': 'Toronto'
        },
        '418': {
            'province': 'Quebec',
            'city': 'Quebec'
        },
        '431': {
            'province': 'Manitoba',
        },
        '437': {
            'province': 'Ontario',
            'city': 'Toronto'
        },
        '438': {
            'province': 'Quebec',
            'city': 'Montreal'
        },
        '450': {
            'province': 'Quebec',
            'city': 'Granby'
        },
        '506': {
            'province': 'New Brunswick',
        },
        '514': {
            'province': 'Quebec',
            'city': 'Montreal'
        },
        '519': {
            'province': 'Ontario',
            'city': 'London'
        },
        '548': {
            'province': 'Ontario',
            'city': 'London'
        },
        '579': {
            'province': 'Quebec',
            'city': 'Granby'
        },
        '581': {
            'province': 'Quebec',
            'city': 'Quebec'
        },
        '587': {
            'province': 'Alberta',
            'city': 'Calgary'
        },
        '604': {
            'province': 'British Columbia',
            'city': 'Vancouver'
        },
        '613': {
            'province': 'Ontario',
            'city': 'Ottawa'
        },
        '639': {
            'province': 'Saskatchewan'
        },
        '647': {
            'province': 'Ontario',
            'city': 'Toronto'
        },
        '705': {
            'province': 'Ontario',
            'city': 'Sunbury'
        },
        '709': {
            'province': 'Newfoundland/Labrador'
        },
        '778': {
            'province': 'British Columbia',
            'city': 'Vancouver'
        },
        '780': {
            'province': 'Alberta',
            'city': 'Edmonton'
        },
        '782': {
            'province': 'Nova Scotia/PE Island'
        },
        '807': {
            'province': 'Ontario',
            'city': 'Kenora'
        },
        '819': {
            'province': 'Quebec',
            'city': 'Sherbrooke'
        },
        '825': {
            'province': 'Alberta',
            'city': 'Calgary'
        },
        '867': {
            'province': 'North Canada'
        },
        '873': {
            'province': 'Quebec',
            'city': 'Sherbrooke'
        },
        '902': {
            'province': 'Nova Scotia/PE Island'
        },
        '905': {
            'province': 'Ontario',
            'city': 'Hamilton'
        },
    }

    @classmethod
    def check_area_code_validity(cls, code):
        check_instance_type(code=code)
        for area_code in cls.area_codes:
            if area_code == code:
                return True
        return False

    @classmethod
    def get_area_province_name_by(cls, code):
        check_instance_type(code=code)
        for area in cls.area_codes:
            if code == area:
                return cls.area_codes.get(code).get('province')
        return ''

    @classmethod
    def get_area_city_name_by(cls, code):
        check_instance_type(code=code)
        for area in cls.area_codes:
            if code == area:
                return cls.area_codes.get(code).get('city')
        return ''


def check_instance_type(code):
    if isinstance(code, str):
        return
    else:
        raise ValueError('Input value must be type of string')
