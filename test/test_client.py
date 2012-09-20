import unittest
from ups.client import UPSClient
from ups.model import Address


class UPSClientTestCase(unittest.TestCase):

    def test_rate_service(self):
        credentials = {
            'username': '',
            'password': '',
            'access_license': ''
        }

        shipper = Address()
        recipient = Address()

        ups = UPSClient(credentials)
        response = ups.rate(shipper=shipper, recipient=recipient)

