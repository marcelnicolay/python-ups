import unittest
from ups.client import UPSClient
from ups.model import Address, Package


class UPSClientTestCase(unittest.TestCase):

    def test_rate_service(self):
        credentials = {
            'username': 'energiahoje',
            'password': 'Saude2011',
            'access_license': '1C85473DF5703150',
            'shipper_number': 'energiahoje'
        }

        shipper = Address(name='shipper address name', city='rio de janeiro',
            address='av das america', state='rio de janeiro', zip='22031012',
            country='brazil')
        recipient = Address(name='shipper address name', city='rio de janeiro',
            address='av das america', state='rio de janeiro', zip='22031012',
            country='brazil')

        packages = [Package(2, 3, 4, 5)]

        ups = UPSClient(credentials)
        response = ups.rate(packages=packages, packaging_type='2a',
            shipper=shipper, recipient=recipient)
