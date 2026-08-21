class RunMemory:
    def __init__(self): self._items=[]
    def append(self,item): self._items.append(item)
    def snapshot(self): return list(self._items)
