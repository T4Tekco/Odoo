# Table of content

- [Table of content](#table-of-content)
  - [Api Route](#api-route)
  - [Request](#request)
  - [Response](#response)
  - [Types](#types)
    - ["Data" Type](#data-type)
    - ["People" Type](#people-type)
    - ["Address" Type](#address-type)
    - [Date Type](#date-type)
  - [Request example](#request-example)

### Api Route

```
http(s)://www.example.com/jsonrpc/ [POST]
```

### Request

```js
{
  "jsonrpc": "2.0",
  "id": number, // <-- Random
  "method": "call",
  "params": {
    "service": "object",
    "method": "execute",
    "args": [
      "<database_name>",
      "<uid>", // Phải đăng nhập qua rpc, server mới trả về uid
      "<api_key>",
      "res.partner",
      "bcdn",
      Data // Xem "Data" Type ở dưới
    ]
  }
}
```

### Response

```js
{
    "status": "success" | "failure",
    "message": string
}
```

### Types

#### "Data" Type

```js
{
    "company": {
        "name": string,
        "foreign_name": string,
        "short_name": string,
        "identity": string,
        "tax_code": string,
        "date_of_birth": Date,
        "street": string,
        "city": string,
        "zip": string,
        "state_code": string,
        "country_code": string,
        "phone": string,
        "fax": string,
        "email": string,
        "website": string,
        "main_industry_code": string,
        "sub_industries": [string, ...],
        "charter_capital": float,
        "registration_office": string,
        "document_url": string,
    }
    "owners": [People, ...],
    "legal_representatives": [People, ...]
}
```

#### "People" Type

```js
{
    "name": string,
    "position": string,
    "sex": "male" | "female" | "unknown",
    "date_of_birth": Date,
    "nationality_code": string,
    "identity": string,
    "permanent_address": Address,
    "contact_address": Address,
}
```

#### "Address" Type

```js
{
    "street": string,
    "street2": string,
    "city": string,
    "state_code": string,
    "zip": string,
    "country_code": string
}
```

#### Date Type

String format: `%Y-%m-%d`

eg: `2022-12-30`

### Request example

```json
{
  "jsonrpc": "2.0",
  "id": 1000,
  "method": "call",
  "params": {
    "service": "object",
    "method": "execute",
    "args": [
      "MyDatabase",
      123,
      "myapikey",
      "res.partner",
      "bcdn",
      {
        "company": {
          "name": "CÔNG TY TNHH LA LA LA",
          "foreign_name": "LA LA LA Company Limited",
          "short_name": "LA LA LA CO., LTD",
          "identity": "0123456789",
          "tax_code": "",
          "date_of_birth": "2023-03-23",
          "street": "My Street",
          "city": "Thành phố Thủ Đức",
          "state_code": "VN-SG",
          "country_code": "VN",
          "phone": "+84987654321",
          "fax": "1234567",
          "email": "myemail@duck.com",
          "website": "https://duckduckgo.com",
          "main_industry_code": "7410",
          "sub_industries": [
            "4322",
            "4329",
            "4330",
            "4390",
            "4620",
            "4649",
            "4663",
            "8531",
            "8552",
            "7020",
            "7110",
            "4789",
            "8130",
            "4101",
            "4102",
            "4299",
            "4311",
            "4312",
            "4321",
            "4759",
            "4773"
          ],
          "charter_capital": 500000000.0,
          "registration_office": "Phòng Đăng ký kinh doanh Thành phố Hồ Chí Minh",
          "document_url": "https://example.com/path/to/file.pdf"
        },
        "owners": [
          {
            "name": "Nguyễn Văn A",
            "sex": "male",
            "date_of_birth": "2000-10-02",
            "identity": "123456789987",
            "nationality_code": "VN",
            "permanent_address": {
              "street": "Dia Chi Thuong Tru",
              "street2": "",
              "city": "Thành phố Hà Tĩnh",
              "state_code": "VN-23",
              "zip": "",
              "country_code": "VN"
            },
            "contact_address": {
              "street": "Dia Chi Lien Lac",
              "street2": "",
              "city": "Thành phố Thủ Đức",
              "state_code": "VN-SG",
              "zip": "",
              "country_code": "VN"
            }
          }
        ],
        "legal_representatives": [
          {
            "name": "Nguyễn Văn A",
            "sex": "male",
            "position": "Giám đốc",
            "date_of_birth": "2000-10-02",
            "identity": "123456789987",
            "nationality_code": "VN",
            "permanent_address": {
              "street": "Dia Chi Thuong Tru",
              "street2": "",
              "city": "Thành phố Hà Tĩnh",
              "state_code": "VN-23",
              "zip": "",
              "country_code": "VN"
            },
            "contact_address": {
              "street": "Dia Chi Lien Lac",
              "street2": "",
              "city": "Thành phố Thủ Đức",
              "state_code": "VN-SG",
              "zip": "",
              "country_code": "VN"
            }
          }
        ]
      }
    ]
  }
}
```
