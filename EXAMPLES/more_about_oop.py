import sys
from circuit import Circuit
# from somemodule import MyDevice
# from someothermodule import SomeClass, SomeOtherClass
# from yetanothermodule import YetAnotherClass

# for hostname in sys.argv[1:]:
#     md = MyDevice(hostname)
#     x = SomeClass(md.some_property)
#     y = SomeClass(md.some_instance_method())
#     result = YetAnotherClass.some_class_method(y.some_value)
cid = input("What is the CID? ")

c = Circuit(cid)
print(f"c.cid: {c.cid}")
print(f"c.aside_nid: {c.aside_nid}")
print(f"c.aside_router: {c.aside_router}")




