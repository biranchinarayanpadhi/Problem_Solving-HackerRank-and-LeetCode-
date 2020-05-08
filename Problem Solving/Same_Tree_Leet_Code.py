# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: TreeNode, root2: TreeNode) -> bool:
        q1=[]
        q2=[]
        q1.append(root1)
        q2.append(root2)
        current=None
        while len(q1)!=0 and len(q2)!=0:
            
            count_ele1=len(q1)
            count_ele2=len(q2)
            
            while count_ele1!=0  or count_ele2!=0:
                current1=q1.pop()
                current2=q2.pop()

                if (current1 is None or current2 is None) and (current1 is not None or current2 is not None ):
                    return False
                if current1 is not None and current2 is not None:
                    if current1.val != current2.val:
                        return False
                    else:
                        q1.append(current1.left)
                        q1.append(current1.right)
                        q2.append(current2.left)
                        q2.append(current2.right)
                else:
                    break
                    
                count_ele1-=1
                count_ele2-=1
        

        return True
                
                