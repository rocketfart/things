class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pre_post(self,list):
        # +12
        def help():
            if list:
                val = list.pop(0)
                root = TreeNode(val)
                root.left = help()
                root.right = help()
                return root

        root = help()
        res = []
        def post(root):
            if root:
                post(root.left)
                post(root.right)
                res.append(root.val)
        post(root)
        return res

def test():
    case = Solution()
    print case.pre_post(['+','1','2'])

if __name__ == '__main__':
    test()



