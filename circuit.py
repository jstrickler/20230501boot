
class Circuit:
    def __init__(self, cid):
        self._cid = cid
        circuit_info = self._find_info()
        # populate properties from the data returned by self._find_info()
        self._aside_nid = circuit_info['aside_nid']
        self._aside_router = circuit_info['aside_router']



    def _find_info(self):
        # use self._cid to find info
        return {'aside_nid': "THE NID", 'aside_router': "THE ROUTER"}

    @property
    def cid(self):
        return self._cid

    @property
    def aside_nid(self):
        return self._aside_nid
    
    @property
    def aside_router(self):
        return self._aside_router
    

if __name__ == "__main__":
    
    c = Circuit('my cid ....')
    print(f"c.cid: {c.cid}")
    print(f"c.aside_nid: {c.aside_nid}")
    print(f"c.aside+router: {c.aside_router}")

    