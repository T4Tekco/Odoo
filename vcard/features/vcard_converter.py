"""
Ref:
    - https://en.wikipedia.org/wiki/VCard
    - https://www.rfc-editor.org/rfc/rfc6350
Format:

BEGIN:VCARD
VERSION: 2.1|3.0|4.0
<data here>
END:VCARD

----
# ALL Version
- ADR
- BDAY
CATEGORIES
- EMAIL
- FN
GEO
KEY
LOGO
- N:<last_name>;<first_name>;<middle_name>;<honorific_prefixes>;<honorific_suffixes>
NOTE
- ORG
PHOTO
REV
ROLE
SOUND
SOURCE
- TEL
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


class VCard:
    """
    Common (All versions)

    TODO: ADR, BDAY, CATEGORIES, EMAIL, FN, GEO, KEY, LOGO, N, NOTE, ORG, PHOTO
    REV, ROLE, SOUND, SOURCE, TEL, TITLE, TZ, UID, URL

    DONE: FN, N, EMAIL, ORG, TEL, ADR, BDAY, CATEGORIES
    """

    version = ""
    p_single = ("BDAY",)
    p_args = ("EMAIL", "ORG", "TEL", "ADR", "CATEGORIES")

    def __init__(self, data):
        self._data = data

    def _N(
        self,
        first_name: str,
        last_name: str = "",
        middle_name: str = "",
        honorific_prefixes: str = "",
        honorific_suffixes: str = "",
        *args: str,
    ):
        s = ";".join(args)
        return f"N:{last_name};{first_name};{middle_name};{honorific_prefixes};{honorific_suffixes};{s}\n"

    def _FN(self, full_name: str):
        return f"FN:{full_name}\n"

    def _ORG(self, org_name: str = "", *ou: str):
        return f"ORG:{org_name};" + ";".join(ou) + "\n" if org_name else ""

    def _EMAIL(self, *elements):
        """
        element:
        {
            "email": str
            "type": str
        }
        """

        return (
            "".join(f"EMAIL;TYPE={e['type']}:{e['email']}\n" for e in elements)
            if elements
            else ""
        )

    def _TEL(self, *elements):
        """
        type-param-tel = "text" / "voice" / "fax" / "cell" / "video" / "pager" / "textphone" / iana-token / x-name
        ;type-param-tel MUST NOT be used with a property other than TEL.

        element:
        {
            type: str,
            phone: str,
        }
        """

        return (
            "".join(f'TEL;TYPE={",".join(e["type"])}:{e["phone"]}\n' for e in elements)
            if elements
            else ""
        )

    def _ADR(self, *elements):
        """
        street: str,
        locality: str,
        region: str,
        code: str,
        country: str,
        _type: str,

        example:
        [
            ("287 Au Duong Lan", "Q8", "HCM", "70000", "VN","home"),
            ("287 Au Duong Lan", "Q8", "HCM", "70000", "VN","work"),
        ]
        """

        def adr(
            street: str,
            locality: str,
            region: str,
            code: str,
            country: str,
            _type: str,
        ):
            return f"ADR;TYPE={_type}:;;{street};{locality};{region};{code};{country}\n"

        return "".join(adr(*e) for e in elements)

    def _BDAY(self, bday: str):
        """Example BDAY:19700310"""

        return f"BDAY:{bday}\n"

    def _CATEGORIES(self, *categories):
        return f"CATEGORIES:" + ",".join(categories) + "\n"

    def _TITLE(self):
        pass

    def _UID(self):
        pass

    def _URL(self):
        pass

    def _build_data(self):
        if self.version not in ("2.1", "3.0", "4.0"):
            raise ValueError("Version must be '2.1' or '3.0' or '4.0'")

        if not self._data.get("N") or not self._data.get("FN"):
            raise ValueError("Required fields: 'N', 'FN'")

        output = self._N(*self._data["N"]) + self._FN(self._data["FN"])

        for att in self.p_single:
            a = self._data.get(att)
            if a:
                output += getattr(self, f"_{att}")(a)

        for att in self.p_args:
            args = self._data.get(att)
            if args:
                output += getattr(self, f"_{att}")(*args)

        return f"VERSION:{self.version}\n" + output

    def _build_extra_data(self):
        """Override this method for another vcard version"""
        return ""

    def build_data(self):
        return f"BEGIN:VCARD\n{self._build_data()}{self._build_extra_data()}\nEND:VCARD"


class VCard21(VCard):
    version = "2.1"


class VCard30(VCard):
    version = "3.0"


class VCard40(VCard):
    version = "4.0"


V_TYPE = {
    "2.1": VCard21,
    "3.0": VCard30,
    "4.0": VCard40,
}


class Converter:
    def __init__(self, data: dict) -> None:
        if data.get("version") in V_TYPE:
            self.vcard: VCard = V_TYPE.get(data["version"])(data)  # type:ignore
        else:
            raise KeyError("Version ... 2.1 | 3.0 | 4.0")

    def _convert(self):
        return self.vcard.build_data()

    def write_to_vcf(self):
        with open("out.vcf", "w") as f:
            f.write(self._convert())


if __name__ == "__main__":
    data = {
        "version": "4.0",
        "N": ("Vy", "Nguyen", "The", "Dr", "PhD", "H", "C"),
        "FN": "Nguyen The Vy",
        # "ORG": ("T4Tek", "Vua Backend", "Hoang De Odoo"),
        # "EMAIL": (
        #     {"email": "abc@t4tek.co", "type": "work"},
        #     {"email": "abc2@t4tek.co", "type": "home"},
        # ),
        # "TEL": (
        #     {"phone": "+84987654321", "type": ("home", "work", "business")},
        #     {"phone": "+84987654333", "type": ("cell",)},
        # ),
        # "ADR": (
        #     ("287 Au Duong Lan", "", "HCM", "70000", "VN", "home"),
        #     ("287 Au Duong Lan", "", "HCM", "70000", "VN", "work"),
        # ),
        # "BDAY": "20000403",
        # "CATEGORIES": ("IT", "Wibu Lord", "Alime"),
    }

    v = Converter(data)
    v.write_to_vcf()
