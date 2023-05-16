# PortalCX Customer Portal SDK
The official Python SDK for creating and managing customer portals in PortalCX. This SDK simplifies the process of integrating your applications with the PortalCX API by providing easy-to-use classes and methods.

## Description
The PortalCX Customer Portal SDK is a Python library that provides a set of classes and methods used for interacting with the PortalCX API. This includes creating and managing users, handling authentication, and managing other aspects of customer portals.

## Installation
You can install the PortalCX Customer Portal SDK directly from GitHub using pip. Open your terminal and run the following command:

```bash
pip install git+https://github.com/portalcx/PortalCX-Customer-Portal-SDK.git
```

## Usage
Here is a simple example of how to use the SDK in your application:

```python
from portalcx.api.portalcx import PortalCX

pxc = PortalCX(api_base_url="https://api.portalcx.com")

auth_token = pxc.login(email="email@email.com", password="password")
```

## Running Tests
To ensure the integrity of the code, it's recommended to run the provided tests. These tests cover a range of scenarios and edge cases to ensure the SDK functions as expected.

To run the tests, navigate to the root directory of the project in your terminal and run the following command:

```bash
python -m pytest
```

## Test Flow

- [API Documentation - Development](https://apidev.portalcx.io/swagger/v1/swagger)
- [API Documentation - Production](https://apidev.portalcx.io/swagger/v1/swagger)

1. Register New Customer: `/api/AuthManagement/Register`
<details>
    <summary>Expand For JSON</summary>
```json
"/api/AuthManagement/Register": {
    "post": {
    "tags": [
        "AuthManagement"
    ],
    "requestBody": {
        "content": {
        "application/json": {
            "schema": {
            "$ref": "#/components/schemas/UserRegistrationRequestDto"
            }
        },
        "text/json": {
            "schema": {
            "$ref": "#/components/schemas/UserRegistrationRequestDto"
            }
        },
        "application/*+json": {
            "schema": {
            "$ref": "#/components/schemas/UserRegistrationRequestDto"
            }
        }
        }
    },
    "responses": {
        "200": {
        "description": "Success"
        }
    }
    }
},
"UserRegistrationRequestDto": {
    "required": [
        "companyName",
        "contactPhone",
        "email",
        "firstName",
        "lastName",
        "password"
    ],
    "type": "object",
    "properties": {
        "firstName": {
            "minLength": 1,
            "type": "string"
        },
        "lastName": {
            "minLength": 1,
            "type": "string"
        },
        "email": {
            "minLength": 1,
            "type": "string"
        },
        "password": {
            "minLength": 1,
            "type": "string"
        },
        "companyName": {
            "minLength": 1,
            "type": "string"
        },
        "companyLogoUrl": {
            "type": "string",
            "nullable": true
        },
        "companySecondaryLogoUrl": {
            "type": "string",
            "nullable": true
        },
        "contactPhone": {
            "minLength": 1,
            "type": "string"
        },
        "companyColor": {
            "type": "string",
            "nullable": true
        },
        "companyId": {
            "type": "integer",
            "format": "int64"
        }
    },
    "additionalProperties": false
}
```
</details>


1. Login:  `/api/AuthManagement/Login`
```json
"application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserLoginRequest"
              }
            }
```
1. Create New Template: `/api/Admin/Template/CreateTemplate`
2. 
3. Create Stages based off Template ID
	1. Add stages with all different options
4. Create New Project
5. Ensure Txt's are going out
6. Complete one stage
7.  Update a project with new Name or Email or whatever
8.  Delete project
11. Delete template

## Contributing
We welcome contributions to this project! To get started, follow these steps:

1 - Fork the repository.
2 - Create a new branch for your feature or bug fix.
3 - Write tests for your changes.
4 - Implement your changes.
5 - Run the tests and make sure they pass.
6 - Submit a pull request.

## License
This project is licensed under the MIT License, which means that you are free to use, modify, and distribute the code as long as the original copyright and license notice are included.