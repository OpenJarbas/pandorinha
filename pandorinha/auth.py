from pandora.clientbuilder import SettingsDictBuilder
from json_database import JsonConfigXDG
from pandorinha.exceptions import CredentialsMissing


def get_client(email=None, password=None):

    if not email or not password:
        creds = JsonConfigXDG("pandora", subfolder="pandorinha")
        email = creds.get("email")
        password = creds.get("password")

    if not email or not password:
        raise CredentialsMissing

    client = SettingsDictBuilder({
        "DECRYPTION_KEY": "R=U!LH$O2B#",
        "ENCRYPTION_KEY": "6#26FRL$ZWD",
        "PARTNER_USER": "android",
        "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
        "DEVICE": "android-generic",
    }).build()

    client.login(email, password)
    return client
