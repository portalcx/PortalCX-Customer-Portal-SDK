import os
import unittest
from api.portalcx import PortalCX
from models.customer_portal_create_request import CustomerPortalCreateRequest

class TestPortalCX(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_base_url = os.environ.get("PORTALCX_API_BASE_URL")
        cls.email = os.environ.get("PORTALCX_EMAIL")
        cls.password = os.environ.get("PORTALCX_PASSWORD")

    def test_login(self):
        portal_cx = PortalCX(api_base_url=self.api_base_url)
        auth_token = portal_cx.login(email=self.email, password=self.password)
        self.assertIsNotNone(auth_token)
        self.assertIsInstance(auth_token, str)
    
    def test_create_portal(self):
        portal_cx = PortalCX(api_base_url=self.api_base_url)
        auth_token = portal_cx.login(email=self.email, password=self.password)
        self.assertIsNotNone(auth_token)

        # Prepare sample data
        portal_data = CustomerPortalCreateRequest(
            customerEmail="test@email.com",
            customerName="John Doe",
            customerPhone="1234567899",
            projectName="Home",
            stages=[
                {
                    "name": "Stage 1",
                    "label": "Stage 1 Label",  # Add the missing "label" field
                    "description": "This is a test stage",
                    "order": 1
                },
                {
                    "name": "Stage 2",
                    "label": "Stage 2 Label",  # Add the missing "label" field
                    "description": "This is another test stage",
                    "order": 2
                },
                {
                    "name": "Stage 3",
                    "label": "Stage 3 Label",  # Add the missing "label" field
                    "description": "This is the third test stage",
                    "order": 3
                }
            ],
            address1="123 Test Street",
            city="Test City",
            stateCode="TS",
            zip="12345",
            enableReferrals=True
        )

        response_data = portal_cx.create_portal(portal_data=portal_data)

        self.assertIsNotNone(response_data)
        self.assertIsInstance(response_data, dict)
        if "portalId" in response_data:
            portalId = response_data["portalId"]
            self.assertIsNotNone(portalId)
            self.assertIsInstance(portalId, str)
            self.assertRegex(portalId, r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$')


if __name__ == "__main__":
    unittest.main()
