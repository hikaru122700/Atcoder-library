class AVL_Node:
    """ノード

    Attributes:
        key (any): ノードのキー。比較可能なものであれば良い。(1, 4)などタプルも可。
        val (any): ノードの値。
        left (Node): 左の子ノード。
        right (Node): 右の子ノード。
        bias (int): 平衡度。(左部分木の高さ)-(右部分木の高さ)。
        size (int): 自分を根とする部分木の大きさ

    """

    def __init__(self, parent, key):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None
        self.bias = 0
        self.size = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def Rotate_Left(self, node):
        node_right = node.right
        node_right.size = node.size
        node.size -= 1
        if node_right.right is not None:
            node.size -= node_right.right.size
        if node_right.bias == -1:
            node_right.bias = 0
            node.bias = 0
        else:
            # assert node_right.bias==0
            node_right.bias = 1
            node.bias = -1
        node.right = node_right.left
        node_right.left = node
        return node_right

    def Rotate_Right(self, node):
        node_left = node.left
        node_left.size = node.size
        node.size -= 1
        if node_left.left != None:
            node.size -= node_left.left.size
        if node_left.bias == 1:
            node_left.bias = 0
            node.bias = 0
        else:
            # assert node_left.bias==0
            node_left.bias = -1
            node.bias = 1
        node.left = node_left.right
        node_left.right = node
        return node_left

    def Rotate_Left_Right(self, node):
        node_left = node.left
        node_left_right = node_left.right
        # assert node.bias==2
        # assert node_left.bias==-1
        # assert node_left_right.bias in (-1,0,1)
        node_left_right.size = node.size
        node.size -= node_left.size
        if node_left_right.right != None:
            node.size += node_left_right.right.size
        node_left.size -= 1
        if node_left_right.right != None:
            node_left.size -= node_left_right.right.size
        node_left.right = node_left_right.left
        node_left_right.left = node_left
        node.left = node_left_right.right
        node_left_right.right = node
        self.Update_Bias_Double(node_left_right)
        return node_left_right

    def Rotate_Right_Left(self, node):
        node_right = node.right
        node_right_left = node_right.left
        # assert node.bias==-2
        # assert node_right.bias==1
        # assert node_right_left.bias in (-1,0,1)
        node_right_left.size = node.size
        node.size -= node_right.size
        if node_right_left.left != None:
            node.size += node_right_left.left.size
        node_right.size -= 1
        if node_right_left.left != None:
            node_right.size -= node_right_left.left.size
        node_right.left = node_right_left.right
        node_right_left.right = node_right
        node.right = node_right_left.left
        node_right_left.left = node
        self.Update_Bias_Double(node_right_left)
        return node_right_left

    def Update_Bias_Double(self, node):
        # assert node.right.bias*node.left.bias==-2
        # assert node.right.bias>0
        if node.bias == 1:
            node.right.bias = -1
            node.left.bias = 0
        elif node.bias == -1:
            node.right.bias = 0
            node.left.bias = 1
        else:
            node.right.bias = 0
            node.left.bias = 0
        node.bias = 0

    def add(self, key):
        if self.root == None:
            self.root = AVL_Node(None, key)
            return
        v = self.root
        stack = []
        while v != None:
            if key < v.key:
                stack.append((v, 1))
                v = v.left
            elif v.key < key:
                stack.append((v, -1))
                v = v.right
            elif v.key == key:
                return
        p, direction = stack[-1]
        if direction == 1:
            p.left = AVL_Node(p, key)
        else:
            p.right = AVL_Node(p, key)
        while stack:
            v, direction = stack.pop()
            v.bias += direction
            v.size += 1
            vv = None
            if v.bias == 2:
                if v.left.bias == -1:
                    vv = self.Rotate_Left_Right(v)
                else:
                    vv = self.Rotate_Right(v)
                # assert vv!=None
                break
            if v.bias == -2:
                if v.right.bias == 1:
                    vv = self.Rotate_Right_Left(v)
                else:
                    vv = self.Rotate_Left(v)
                # assert vv!=None
                break
            if v.bias == 0:
                break
        if vv != None:
            if len(stack) == 0:
                self.root = vv
                return
            p, direction = stack.pop()
            p.size += 1
            if direction == 1:
                p.left = vv
            else:
                p.right = vv
        while stack:
            p, direction = stack.pop()
            p.size += 1

    def discard(self, key):
        v = self.root
        stack = []
        while v != None:
            if key < v.key:
                stack.append((v, 1))
                v = v.left
            elif v.key < key:
                stack.append((v, -1))
                v = v.right
            else:
                break
        else:
            return False
        if v.left != None:
            stack.append((v, 1))
            lmax = v.left
            while lmax.right != None:
                stack.append((lmax, -1))
                lmax = lmax.right
            v.key = lmax.key
            v = lmax
        c = v.right if v.left == None else v.left
        if stack:
            p, direction = stack[-1]
            if direction == 1:
                p.left = c
            else:
                p.right = c
        else:
            self.root = c
            return True
        while stack:
            pp = None
            p, direction = stack.pop()
            p.bias -= direction
            p.size -= 1
            if p.bias == 2:
                if p.left.bias == -1:
                    pp = self.Rotate_Left_Right(p)
                else:
                    pp = self.Rotate_Right(p)
            elif p.bias == -2:
                if p.right.bias == 1:
                    pp = self.Rotate_Right_Left(p)
                else:
                    pp = self.Rotate_Left(p)
            elif p.bias != 0:
                break
            if pp != None:
                if len(stack) == 0:
                    self.root = pp
                    return True
                p, direction = stack[-1]
                if direction == 1:
                    p.left = pp
                else:
                    p.right = pp
                if pp.bias != 0:
                    break
        while stack:
            p, direction = stack.pop()
            p.size -= 1
        return True

    def Bisect_Right(self, key):
        retu = None
        v = self.root
        while v != None:
            if v.key > key:
                if retu == None or retu > v.key:
                    retu = v.key
                v = v.left
            else:
                v = v.right
        return retu

    def Bisect_Left(self, key):
        retu = None
        v = self.root
        while v != None:
            if v.key < key:
                if retu == None or retu < v.key:
                    retu = v.key
                v = v.right
            else:
                v = v.left
        return retu

    def Find_Kth_Element(self, K):
        v = self.root
        s = 0
        while v != None:
            t = s + v.left.size if v.left != None else s
            if t == K:
                return v.key
            elif t < K:
                s = t + 1
                v = v.right
            else:
                v = v.left
        return None

    def __contains__(self, key):
        v = self.root
        while v != None:
            if key < v.key:
                v = v.left
            elif v.key < key:
                v = v.right
            else:
                return True
        return False

    def __iter__(self):
        stack = [(self.root, True)]
        while stack:
            node, subtree = stack.pop()
            if subtree:
                if node.right != None:
                    stack.append((node.right, True))
                stack.append((node, False))
                if node.left != None:
                    stack.append((node.left, True))
            else:
                yield node.key

    def __bool__(self):
        return self.root != None

    def __len__(self):
        return 0 if self.root == None else self.root.size

    def __str__(self):
        if self.root == None:
            retu = "{}"
        else:
            retu = "{" + ", ".join(str(key) for key in self) + "}"
        return retu
