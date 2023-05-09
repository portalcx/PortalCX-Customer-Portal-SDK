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
python -m unittest discover -v
```

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