class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q=[]
        q.append(root)
        res=[]
        while q:
            node_count=len(q)
            while node_count>0:
                current=q.pop(0)
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
                node_count-=1
                if node_count==0:
                    res.append(current.val)
        return (res)
         
                    