class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        if root is None:
            return None
        res=[]
        current=root
        q=[]
        
        while True:
            
            if current is not None:
                q.append(current)
                current=current.left
            
            elif len(q)>0:
                current=q.pop()
                res.append(current.val)
                current=current.right
                
            else:
                break
#print(res)       
        return res[k-1]