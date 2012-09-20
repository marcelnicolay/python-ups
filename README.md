python-ups
==========

UPS shipping interface

Using
=======
    from ups.client import UPSClient
    from ups.model import Package, Address

    
    credentials = {
        'username': '',
        'password': '',
        'access_license': '',
        'shipper_number': ''
    }

    shipper = Address(name='shipper address name', city='rio de janeiro',
        address='', state='', zip='',
        country='brazil')
    recipient = Address(name='shipper address name', city='rio de janeiro',
        address='', state='', zip='',
        country='brazil')

    packages = [Package(2, 3, 4, 5)]

    ups = UPSClient(credentials)
    response = ups.rate(packages=packages, packaging_type='2a',
        shipper=shipper, recipient=recipient)