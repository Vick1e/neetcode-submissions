class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}

            node = node[char]
        node["#"] = True

    def search(self, word: str) -> bool:
        
        def dfs(i,node):
            if i == len(word):
                return "#" in node

            char = word[i]


            #当前不是。
            if char != ".":
                if char not in node:
                    return False

                return dfs(i+1,node[char])


            #当前是。    
            for key in node:

                if key =="#":
                    continue

                if dfs(i+1,node[key]):
                    return True


            return False
        return dfs(0,self.root)

