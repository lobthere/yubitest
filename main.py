#from a lobster

import yubico

c = yubico.yubikey.find_key(debug=False, skip=0)
print(c)