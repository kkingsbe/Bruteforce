import hashlib;

hashedstring = None
def encrypt(input):
    string = "prejudiciously"
    bytestring = string.encode('utf-8')
    hashedstring = hashlib.sha256(bytestring).hexdigest()
    byteinput = input.encode('utf-8')
    hashedinput = hashlib.sha256(byteinput).hexdigest()
    if hashedinput == hashedstring:
        return True
    else:
        return False