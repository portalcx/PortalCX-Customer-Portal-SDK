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
from portalcx import PortalCX

pxc = PortalCX(base_url="https://api.portalcx.com")

auth_token = pxc.login(email="email@email.com", password="password")
```

## Running Tests
To ensure the integrity of the code, it's recommended to run the provided tests. These tests cover a range of scenarios and edge cases to ensure the SDK functions as expected.

To run the tests, navigate to the root directory of the project in your terminal and run the following command:

```bash
python -m pytest
```

## PyTest Flow and Integration Guide

- [API Documentation - Development](https://apidev.portalcx.io/swagger/v1/swagger)
- [API Documentation - Production](https://apidev.portalcx.io/swagger/v1/swagger)

<hr>

<details><summary><h4>1.<a href="https://signup.portalcx.com"> Register For PortalCX</a></h4></summary>

Try PortalCX Free for 14 Days!

</details>

<hr>

<details><summary><h4>2. Login And Save Token</h4></summary>

**URL:** `/api/AuthManagement/Login`

**JSON Schema:**

```json
{
    "/api/AuthManagement/Login": {
        "post": {
            "tags": [
                "AuthManagement"
            ],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserLoginRequest"
                        }
                    },
                    "text/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserLoginRequest"
                        }
                    },
                    "application/*+json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserLoginRequest"
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
    "UserLoginRequest": {
        "required": [
            "email",
            "password"
        ],
        "type": "object",
        "properties": {
            "email": {
                "minLength": 1,
                "type": "string"
            },
            "password": {
                "minLength": 1,
                "type": "string"
            }
        },
        "additionalProperties": false
    }
}
```

</details>

<hr>

<details><summary><h4>3. Create Project Template And Save Template ID</h4></summary>

**URL:** `/api/Admin/Template/CreateTemplate`

**JSON Schema:**

```json
{
    "/api/Admin/Template/CreateTemplate": {
        "post": {
            "tags": [
                "AdminTemplate"
            ],
            "requestBody": {
                "content": {
                    "multipart/form-data": {
                        "schema": {
                            "required": [
                                "CompanyName",
                                "ContactEmail",
                                "ContactPhone",
                                "IsCustomerReferrals",
                                "Title"
                            ],
                            "type": "object",
                            "properties": {
                                "TemplateId": {
                                    "type": "string",
                                    "format": "uuid"
                                },
                                "CompanyId": {
                                    "type": "integer",
                                    "format": "int64"
                                },
                                "Title": {
                                    "type": "string"
                                },
                                "ContactEmail": {
                                    "type": "string"
                                },
                                "ContactPhone": {
                                    "type": "string"
                                },
                                "CompanyName": {
                                    "type": "string"
                                },
                                "Color": {
                                    "type": "string"
                                },
                                "TemplateAppLogoUpload": {
                                    "type": "string",
                                    "format": "binary"
                                },
                                "EmailLogoUpload": {
                                    "type": "string",
                                    "format": "binary"
                                },
                                "IsCustomerReferrals": {
                                    "type": "boolean"
                                },
                                "IsLogoUpdate": {
                                    "type": "boolean"
                                },
                                "IsEmailLogoUpdate": {
                                    "type": "boolean"
                                },
                                "CountryId": {
                                    "type": "integer",
                                    "format": "int64"
                                }
                            }
                        },
                        "encoding": {
                            "TemplateId": {
                                "style": "form"
                            },
                            "CompanyId": {
                                "style": "form"
                            },
                            "Title": {
                                "style": "form"
                            },
                            "ContactEmail": {
                                "style": "form"
                            },
                            "ContactPhone": {
                                "style": "form"
                            },
                            "CompanyName": {
                                "style": "form"
                            },
                            "Color": {
                                "style": "form"
                            },
                            "TemplateAppLogoUpload": {
                                "style": "form"
                            },
                            "EmailLogoUpload": {
                                "style": "form"
                            },
                            "IsCustomerReferrals": {
                                "style": "form"
                            },
                            "IsLogoUpdate": {
                                "style": "form"
                            },
                            "IsEmailLogoUpdate": {
                                "style": "form"
                            },
                            "CountryId": {
                                "style": "form"
                            }
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
    }
}
```
</details>

<hr>

<details><summary><h4>4. Create Stages From Template ID</h4></summary>

>**Note:** In the test workflow, we create 3 stages, each with different options.

**URL:** `/api/Admin/Template/CreateStage`

**JSON Schema:**

```json
{
    "/api/Admin/Template/CreateStage": {
        "post": {
            "tags": [
                "AdminTemplate"
            ],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/TemplateStageCreateRequest"
                        }
                    },
                    "text/json": {
                        "schema": {
                            "$ref": "#/components/schemas/TemplateStageCreateRequest"
                        }
                    },
                    "application/*+json": {
                        "schema": {
                            "$ref": "#/components/schemas/TemplateStageCreateRequest"
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
    "TemplateStageCreateRequest": {
        "required": [
            "stageDescription",
            "stageName",
            "templateId"
        ],
        "type": "object",
        "properties": {
            "templateStageId": {
                "type": "integer",
                "format": "int64"
            },
            "templateId": {
                "type": "string",
                "format": "uuid"
            },
            "stageName": {
                "minLength": 1,
                "type": "string"
            },
            "stageDescription": {
                "minLength": 1,
                "type": "string"
            },
            "stagePromptButtonCopy": {
                "type": "string",
                "nullable": true
            },
            "stagePromptButtonUrl": {
                "type": "string",
                "nullable": true
            }
        },
        "additionalProperties": false
    }
}
```
</details>

<hr>

<details><summary><h4>5. Create Project From Template ID</h4></summary>

**URL:** `/api/Admin/Project/CreateProject`

**JSON Schema:**

```json
{
    "/api/Admin/Project/CreateProject": {
        "post": {
            "tags": [
                "AdminProject"
            ],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/ProjectCreateRequest"
                        }
                    },
                    "text/json": {
                        "schema": {
                            "$ref": "#/components/schemas/ProjectCreateRequest"
                        }
                    },
                    "application/*+json": {
                        "schema": {
                            "$ref": "#/components/schemas/ProjectCreateRequest"
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
    "ProjectCreateRequest": {
        "required": [
            "email",
            "firstName",
            "lastName",
            "phoneNumber",
            "templateId"
        ],
        "type": "object",
        "properties": {
            "projectId": {
                "type": "integer",
                "format": "int64"
            },
            "templateId": {
                "type": "string",
                "format": "uuid"
            },
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
            "phoneNumber": {
                "minLength": 1,
                "type": "string"
            },
            "addressLine1": {
                "type": "string",
                "nullable": true
            },
            "addressLine2": {
                "type": "string",
                "nullable": true
            },
            "city": {
                "type": "string",
                "nullable": true
            },
            "stateCode": {
                "type": "string",
                "nullable": true
            },
            "zip": {
                "type": "string",
                "nullable": true
            },
            "notifyViaEmail": {
                "type": "boolean"
            },
            "notifyViaSMS": {
                "type": "boolean"
            },
            "completeFirstStage": {
                "type": "boolean"
            },
            "countryId": {
                "minimum": 1,
                "type": "integer",
                "format": "int64"
            },
            "projectSubscribers": {
                "type": "array",
                "items": {
                    "$ref": "#/components/schemas/ProjectSubscriberRequestViewModel"
                },
                "nullable": true
            }
        },
        "additionalProperties": false
    }
}
```
</details>

<hr>

<details><summary><h4>6. Get All Stages By Template ID</h4></summary>

**URL:** `/api/Admin/Template/GetAllStagesByTemplateId`

**JSON Schema:**

```json
{
    "/api/Admin/Template/GetAllStagesByTemplateId": {
        "get": {
            "tags": [
                "AdminTemplate"
            ],
            "parameters": [
                {
                    "name": "templateId",
                    "in": "query",
                    "schema": {
                        "type": "string",
                        "format": "uuid"
                    }
                }
            ],
            "responses": {
                "200": {
                    "description": "Success"
                }
            }
        }
    }
}
```
</details>

<hr>

<details><summary><h4>7. Complete Each Stage Until Project Fully Complete by Portal ID and Stage ID/Name</h4></summary>

**URL:** `/api/Admin/Project/CompleteProjectStage`

**JSON Schema:**

```json
{
    "/api/Admin/Project/CompleteProjectStage": {
        "post": {
            "tags": [
                "AdminProject"
            ],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/ProjectStageCompleteRequest"
                        }
                    },
                    "text/json": {
                        "schema": {
                            "$ref": "#/components/schemas/ProjectStageCompleteRequest"
                        }
                    },
                    "application/*+json": {
                        "schema": {
                            "$ref": "#/components/schemas/ProjectStageCompleteRequest"
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
    "ProjectStageCompleteRequest": {
        "required": [
            "completedDate",
            "completedStageLabel",
            "notifyViaEmail",
            "notifyViaSms"
        ],
        "type": "object",
        "properties": {
            "projectId": {
                "type": "integer",
                "format": "int64",
                "nullable": true
            },
            "portalId": {
                "type": "string",
                "nullable": true
            },
            "completedStageLabel": {
                "minLength": 1,
                "type": "string"
            },
            "completedDate": {
                "type": "string",
                "format": "date-time"
            },
            "notifyViaEmail": {
                "type": "boolean"
            },
            "notifyViaSms": {
                "type": "boolean"
            }
        },
        "additionalProperties": false
    }
}
```

</details>

<hr>

<details><summary><h4>8. Delete Project By Project ID</h4></summary>

**URL:** `/api/Admin/Project/DeleteProject`

**JSON Schema:**

```json
{
    "/api/Admin/Project/DeleteProject": {
        "delete": {
            "tags": [
                "AdminProject"
            ],
            "parameters": [
                {
                    "name": "projectId",
                    "in": "query",
                    "schema": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            ],
            "responses": {
                "200": {
                    "description": "Success"
                }
            }
        }
    }
}
```
</details>

<hr>

<details><summary><h4>9. Delete Each Stage By Template Stage ID</h4></summary>

**URL:** `/api/Admin/Template/DeleteStage`

**JSON Schema:**

```json
{
    "/api/Admin/Template/DeleteStage": {
        "delete": {
            "tags": [
                "AdminTemplate"
            ],
            "parameters": [
                {
                    "name": "templateStageId",
                    "in": "query",
                    "schema": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            ],
            "responses": {
                "200": {
                    "description": "Success"
                }
            }
        }
    }
}
```
</details>

<hr>

<details><summary><h4>10. Delete Template</h4></summary>

**URL:** `/api/Admin/Project/DeleteProject`

**JSON Schema:**

```json
{
    "/api/Admin/Template/DeleteTemplate": {
        "delete": {
            "tags": [
                "AdminTemplate"
            ],
            "parameters": [
                {
                    "name": "templateId",
                    "in": "query",
                    "schema": {
                        "type": "string",
                        "format": "uuid"
                    }
                }
            ],
            "responses": {
                "200": {
                    "description": "Success"
                }
            }
        }
    }
}
```
</details>

<hr>

## Contributing
We welcome contributions to this project! To get started, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes.
4. Implement your changes.
5. Run the tests and make sure they pass.
6. Submit a pull request with test output in the summary.

## License
This project is licensed under the MIT License, which means that you are free to use, modify, and distribute the code as long as the original copyright and license notice are included.
