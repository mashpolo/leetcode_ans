class Trie:
    def __init__(self):
        self.dic={}
    def insert(self,strr):
        a=self.dic
        for i in strr:
            if not i in a:
                a[i]={}
            a=a[i]
        a["end"]=True
    def search(self,strr):
        a=self.dic
        for i in strr:
            if not i in a:
                return False
            a=a[i]
        if "end" in a:
            return True
        else:
            return False
    def startsWith(self,strr):
        a=self.dic
        for i in strr:
            if not i in a:
                return False
            a=a[i]
        return True
 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
