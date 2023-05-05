from circuit import Circuit
cid = input("What is the CID? ")

c = Circuit(cid)
print(f"c.cid: {c.cid}")
print(f"c.aside_nid: {c.aside_nid}")
print(f"c.aside_router: {c.aside_router}")

# display circuit using gfx via c
# ask for which details
# show more graphics and details etc etc
