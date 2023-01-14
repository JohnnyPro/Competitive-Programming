class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        unionFind = {}
        
        def find(x):
            
            unionFind.setdefault(x,x)
            if x != unionFind[x]:
                unionFind[x] = find(unionFind[x]) # recursively searches for the root
            
            return unionFind[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX>rootY:
                unionFind[rootX] = rootY
            else:
                unionFind[rootY] = rootX
        
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        # Convert the baseStr to its smallest form
        result = []
        for c in baseStr:
            result.append(find(c))
            
        return ''.join(result)