from qeos.cleos import Cleos


ce = Cleos(url='http://localhost:8000')


resp = ce.get_info()
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')