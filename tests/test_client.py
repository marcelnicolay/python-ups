#coding: utf-8
import unittest
from ups.client import UPSClient
from ups.model import Address, Package


class UPSClientTestCase(unittest.TestCase):

    def test_rate_service(self):
        credentials = {
            'username': '',
            'password': '',
            'access_license': '',
            'shipper_number': ''
        }

        shipper = Address(name='shipper address name', city='rio de janeiro',
            address=u'R. Mexico, 3 - 13º andar', address2='Centro',
            state='', zip='20031144',
            country='BR')

        recipient = Address(name='shipper address name', city='anniston',
            address='', state='AL', zip='36201',
            country='US')

        packages = [Package(2, 3, 4, 5)]

        ups = UPSClient(credentials)
        response = ups.rate(packages=packages, packaging_type='21',
            shipper=shipper, recipient=recipient)

        import pdb;pdb.set_trace()
