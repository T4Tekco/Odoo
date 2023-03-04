"""
Ref:
    - https://en.wikipedia.org/wiki/VCard
    - https://www.rfc-editor.org/rfc/rfc6350
Format:

BEGIN:VCARD\n
VERSION: <2.1|3.0|4.0>\n
<data here>\n
END:VCARD\n

----
# ALL Version fields
- ADR
- BDAY
- CATEGORIES
- EMAIL
- FN
- GEO
- KEY
- LOGO
- N:<last_name>;<first_name>;<middle_name>;<honorific_prefixes>;<honorific_suffixes>
- NOTE
- ORG
- PHOTO
- REV
- ROLE
- SOUND
- SOURCE
- TEL
- TITLE
- TZ
- UID
- URL

## V2.1, V3.0 vCard fields 
- AGENT, LABEL, MAILER, PROFILE

## V3.0 vCard fields
- CLASS, NAME, SORT-STRING

## V3.0 and V4.0 vCard fields
- IMPP, NICKNAME, PRODID

## V4.0 vCard fields
- ANNIVERSARY, CALADRURI, CALURI, CLIENTPIDMAP, FBURL, GENDER, KIND, LANG, MEMBER, RELATED, XML
"""
from datetime import datetime
from odoo.addons.vcard.features import ImageExtractor  # type:ignore

# For local manual testing
# from utils import ImageExtractor


class VCard:
    """
    Common (All versions)

    TODO: GEO, SOUND

    """

    version = ""
    p_single = (
        "BDAY",
        "TITLE",
        "ROLE",
        "TZ",
        "REV",
        "SOURCE",
        "KEY",
        "UID",
        "NOTE",
    )
    p_args = ("EMAIL", "ORG", "TEL", "ADR", "CATEGORIES", "URL")
    p_image = ("PHOTO", "LOGO")

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

    def _CATEGORIES(self, *categories):
        return f"CATEGORIES:" + ",".join(categories) + "\n"

    def _URL(self, *elements):
        """
        element
        {
            url: str,
            type: str, eg: home, work, blahblah....
        }
        """

        def url(type, url):
            return f"URL;TYPE={type}:{url}\n"

        return "".join(url(*e) for e in elements)

    def _LOGO_B64(self, data: str, _type="PNG", encoding="BASE64"):
        """
        2.1: LOGO;PNG:http://example.com/logo.png
        2.1: LOGO;PNG;ENCODING=BASE64:[base64-data]
        3.0: LOGO;TYPE=PNG:http://example.com/logo.png
        3.0: LOGO;TYPE=PNG;ENCODING=b:[base64-data]
        4.0: LOGO;MEDIATYPE=image/png:http://example.com/logo.png
        4.0: LOGO;ENCODING=BASE64;TYPE=PNG:[base64-data]
        """
        raise NotImplementedError("Not implemented")

    def _PHOTO_B64(self, data: str, _type="PNG", encoding="BASE64"):
        """
        2.1: PHOTO;JPEG:http://example.com/photo.jpg
        2.1: PHOTO;JPEG;ENCODING=BASE64:[base64-data]
        3.0: PHOTO;TYPE=JPEG;VALUE=URI:http://example.com/photo.jpg
        3.0: PHOTO;TYPE=JPEG;ENCODING=b:[base64-data]
        4.0: PHOTO;MEDIATYPE=image/jpeg:http://example.com/photo.jpg
        4.0: PHOTO;ENCODING=BASE64;TYPE=JPEG:[base64-data]
        """
        raise NotImplementedError("Not implemented")

    def _get_image_b64(self):
        output = ""
        for key in self.p_image:
            image = self._data.get(key)
            if image:
                args = ImageExtractor(image).extract()
                output += getattr(self, f"_{key}_B64")(*args)

        return output

    def _get_line(self, key, value):
        if not value:
            return ""
        return f"{key}:{value}\n"

    def _build_data(self):
        if self.version not in ("2.1", "3.0", "4.0"):
            raise ValueError("Version must be '2.1' or '3.0' or '4.0'")

        if not self._data.get("N") or not self._data.get("FN"):
            raise ValueError("Required fields: 'N', 'FN'")

        output = self._N(*self._data["N"]) + self._FN(self._data["FN"])

        output += "".join(
            self._get_line(att, self._data.get(att)) for att in self.p_single
        )

        for att in self.p_args:
            args = self._data.get(att)
            if args:
                output += getattr(self, f"_{att}")(*args)

        output += self._get_image_b64()

        return f"VERSION:{self.version}\n" + output

    def _build_extra_data(self):
        """Override this method for build more data structure"""
        return ""

    def build_data(self):
        return f"BEGIN:VCARD\n{self._build_data()}{self._build_extra_data()}\nEND:VCARD"


class VCard21(VCard):
    version = "2.1"

    def _LOGO_B64(self, data: str, _type: str, *args):
        """
        2.1: LOGO;PNG;ENCODING=BASE64:[base64-data]
        """
        return f"LOGO;{_type};ENCODING=BASE64:{data}\n"

    def _PHOTO_B64(self, data: str, _type: str, *args):
        """
        2.1: PHOTO;JPEG;ENCODING=BASE64:[base64-data]
        """
        return f"PHOTO;{_type};ENCODING=BASE64:{data}\n"


class VCard30(VCard):
    version = "3.0"

    def _LOGO_B64(self, data: str, _type: str, *args):
        """
        3.0: LOGO;TYPE=PNG;ENCODING=b:[base64-data]
        """
        return f"LOGO;TYPE={_type};ENCODING=b:{data}\n"

    def _PHOTO_B64(self, data: str, _type: str, *args):
        """
        3.0: PHOTO;TYPE=JPEG;ENCODING=b:[base64-data]
        """
        return f"PHOTO;TYPE={_type};ENCODING=b:{data}\n"


class VCard40(VCard):
    """Only-v4.0 fields:
    ANNIVERSARY, CALADRURI, CALURI, CLIENTPIDMAP, FBURL, GENDER,
    KIND, LANG, MEMBER, RELATED, XML"""

    version = "4.0"

    def _LOGO_B64(self, data: str, _type: str, encoding="BASE64"):
        """
        4.0: LOGO;ENCODING=BASE64;TYPE=PNG:[base64-data]
        """
        return f"LOGO;ENCODING={encoding};TYPE={_type}:{data}\n"

    def _PHOTO_B64(self, data: str, _type: str, encoding="BASE64"):
        """
        4.0: PHOTO;ENCODING=BASE64;TYPE=JPEG:[base64-data]
        """
        return f"PHOTO;ENCODING={encoding};TYPE={_type}:{data}\n"


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
        "ORG": ("T4Tek", "Vua Backend", "Hoang De Odoo"),
        "EMAIL": (
            {"email": "abc@t4tek.co", "type": "work"},
            {"email": "abc2@t4tek.co", "type": "home"},
        ),
        "TEL": (
            {"phone": "+84987654321", "type": ("home", "work", "business")},
            {"phone": "+84987654333", "type": ("cell",)},
        ),
        "ADR": (
            ("287 Au Duong Lan", "", "HCM", "70000", "VN", "home"),
            ("287 Au Duong Lan", "", "HCM", "70000", "VN", "work"),
        ),
        "BDAY": "20000403",
        "CATEGORIES": ("IT", "Wibu Lord", "Alime"),
        "ROLE": "Backend Developer",
        "TITLE": "Wibu Lord",
        "TZ": "Vietnam/Ho_Chi_Minh",
        "URL": (
            ("home", "https://elearning.t4tek.tk/"),
            ("work", "https://labs.t4tek.tk/"),
            ("business", "https://github.com/T4Tekco"),
        ),
        "REV": datetime.now().strftime("%Y%m%dT%H%M%SZ"),
        "NOTE": "Hello world",
        "PHOTO": b"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",
        "LOGO": b"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",
    }

    v = Converter(data)
    v.write_to_vcf()
