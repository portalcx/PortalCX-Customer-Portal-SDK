# PortalCX-Customer-Portal-SDK
Official Python SDK for creating and managing customer portals in PortalCX.

## Description

This project is a collection of shared code used across multiple Azure Function Apps at PortalCX. It provides various utility functions and API base classes to simplify development and maintenance of these applications.

## Installation

To install the shared code package, run the following command:

```bash
pip install git+https://github.com:portalcx/PortalCX-Customer-Portal-SDK.git
```

## Usage
To use the shared code in your Azure Function App, simply import the necessary modules from the package. For example, to use the APIBase class:

```python
from shared_code.api.api_base import APIBase

class MyAPI(APIBase):
    # Your API implementation goes here
```

## Contributing
We welcome contributions to this project! To get started, follow these steps:

  1. Fork the repository
  2. Create a new branch for your feature or bug fix
  3. Write tests for your changes
  4. Implement your changes
  5. Run the tests and make sure they pass
  6. Submit a pull request

## License
This project is licensed under the MIT License.
