"""
Format:

BEGIN:VCARD
VERSION: 2.1|3.0|4.0
<Add data>
END:VCARD

----
# ALL Version
ADR
BDAY
CATEGORIES
EMAIL
FN
GEO
KEY
LOGO
N
NOTE
ORG
PHOTO
REV
ROLE
SOUND
SOURCE
TEL
TITLE
TZ
UID
URL

#
AGENT
ANNIVERSARY
CALADRURI
CALURI
CLASS
CLIENTPIDMAP
FBURL
FN
GENDER
IMPP
KIND
LABEL
LANG
MAILER
MEMBER
NAME
NICKNAME
PRODID
PROFILE
RELATED
SORT-STRING
XML
"""


class VCardBase:
    pass


class VCard21(VCardBase):
    pass


class VCard30(VCardBase):
    pass


class VCard40(VCardBase):
    pass


class VCardConverter:
    def __init__(self, data) -> None:
        self.__data = data

    def build_data(self):
        output = f"""BEGIN:VCARD
VERSION:{self.__data['version']}
N:{self.__data['last_name']};{self.__data['first_name']};;{self.__data['role']}
TEL;cell:{self.__data['phone']}
TEL;home:{self.__data['phone']}
TEL;work:{self.__data['phone']}
TEL;t4tek:{self.__data['phone']}
END:VCARD"""

        return output

    def write_to_vcf(self):
        with open("out.vcf", "w") as f:
            f.write(self.build_data())


if __name__ == "__main__":
    data = {
        "version": "4.0",
        "last_name": "Nguyen",
        "first_name": "Vy",
        "role": "PhD",
        "phone": "+84987654321",
    }
    v = VCardConverter(data)
    print(v.write_to_vcf())
