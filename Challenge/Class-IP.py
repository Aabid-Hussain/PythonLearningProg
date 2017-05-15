class Dev:
    """ This is class Dev and it has count as
    class variable and ip_address and name as instance variable"""
    count = 0

    def __init__(self, ip_address, name):
        self.ip_address = ip_address
        self.name = name


router = Dev("192.168.1.1", "cisco")
switch = Dev("192.168.10.1", "lg")
if hasattr(router, "prompt"):
    print("prompt already an attribute")
else:
    print("prompt not an attribute")

print (router.ip_address)
print (getattr(router,'ip_address'))
router.prompt = "New Prompt"
print (router.prompt)
print (hasattr(switch, "prompt"))
setattr(router,"prompt","very new prompt")
print (router.prompt)
print (router.__dict__)
print (switch.__dict__)
print (router.__doc__)
print (router.__class__.__name__)
print (router.__module__ )

