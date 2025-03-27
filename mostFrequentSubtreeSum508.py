class Solution(object):
    def findFrequentTreeSum(self, root):
        self.cache={}
        self.frequency={}
        self.highestFrequency=0
        def subtreeSum(node):
            if not node:
                return 0
            if node in self.cache:
                return self.cache[node]
            self.cache[node]=subtreeSum(node.left) + subtreeSum(node.right)+node.val
            return self.cache[node]
        def traversall(node):
            if not node:
                return
            suma=subtreeSum(node)
            if suma in self.frequency:
                self.frequency[suma]+=1
            else:
                self.frequency[suma]=1
            self.highestFrequency=max(self.highestFrequency,self.frequency[suma])
            traversall(node.left)
            traversall(node.right)
        traversall(root)
        ans=[]
        for key in self.frequency:
            if self.frequency[key]==self.highestFrequency:
                ans.append(key)
        return ans
