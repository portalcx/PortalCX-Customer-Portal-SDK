import os
import unittest
from api.portalcx import PortalCX

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


if __name__ == "__main__":
    unittest.main()
