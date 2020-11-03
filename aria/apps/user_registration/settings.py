class UserRegistrationSettings:
    # --------------------------- Email Configuration ----------------------------
    """
    For email configuration you can set your personal
    email server configuration as custom or you can change it
    to gmail mail server.
    """

    """ this mail server is one of these ones : Gmail, Custom
    # Gmail : Pay attention to two factor login in gmail accounts, if you are using
    # a gmail with two factor authentication please try and use another 
    mail server for your security and personal issue.
    # Custom: For this solution please check connection test file in 
    tests folder.
    """

    MAIL_SERVER = 'Gmail'

    # these configs are mutual for gmail and custom mail server
    PASSWORD = 'Hamed@123'
    SENDER_EMAIL = 'h.pourjafar@gmail.com'

    # Below Configs are for when you use a custom mail server
    TLS = False
    EMAIL_PORT = 443
    EMAIL_HOST = 'test host'

    # ----------------------------------------------------------------------------

    # ----------------------------- SMS Configuration ----------------------------
    """
    SMS providers that are allowed in this app are as below:
        KavehNegar
    """

    SMS_SERVER = 'KavehNegar'

    # Sms server general configs
    SMS_HOST = 'https://api.kavenegar.com/v1/verify/lookup.json'
    SMS_PORT = 0

    # SMS Server kaveh negar options
    SMS_API_KEY = '51526948626B36673076494E34745974444C7959744B5637724733395250412B'
    SMS_TEMPLATE_NAME = 'verify'

    # -----------------------------------------------------------------------------

    # ----------------------------- user registration configuration ----------------------------
    USER_NAME_FIELD = 'phone_number'
    CLIENT_ID = ''
    CLIENT_SECRET = ""
    GRANT_TYPE = ''
    AUTHORIZATION_PATH = 'http://localhost:8000/authentication/token/'
