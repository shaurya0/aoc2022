# %%
with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()

class Node(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def size(self):
        raise NotImplemented("")

class Folder(Node):
    def __init__(self, parent, name, children=None):
        Node.__init__(self,parent, name)
        if children is None:
            self.children = []

        self._size = None

    def size(self):
        if self._size is None:
            # print(f"{self.name}:")
            s = 0
            for c in self.children:
                # print(c.name, c.size())
                s += c.size()
            self._size = s
            # self._size = sum([c.size() for c in self.children])
        return self._size

    def has_child(self,name):
        found = False
        for ch in cur_node.children:
            if ch.name == name:
                found = True
                break
        return found

class File(Node):
    def __init__(self, parent, name, size):
        Node.__init__(self,parent, name)
        self._size = size

    def size(self):
        return self._size



root_node = Folder(None, '/')
root_node.parent = root_node
cur_node = root_node

prev_dir = None
for line in lines:
    if line[0] == '$':
        if line[2:4] == 'cd':
            dest = line[5:]
            dest_node = None
            if dest == '..':
                dest_node = cur_node.parent
            elif dest == '/':
                dest_node = root_node
            else:
                for ch in cur_node.children:
                    if isinstance(ch, Folder) and ch.name == dest:
                        dest_node = ch
                        break

            if dest_node is None:
                raise ValueError(f"destination folder {dest} not found")

            cur_node = dest_node
            continue
        if line[2:4] == 'ls':
            continue
    elif line.startswith('dir'):
        folder_name = line.split(' ')[-1]
        if not cur_node.has_child(folder_name):
            folder = Folder(cur_node, folder_name)
            cur_node.children.append(folder)
    elif line[0].isdigit():
        size, file_name =  line.split(' ')
        if not cur_node.has_child(file_name):
            file = File(cur_node, file_name, int(size))
            cur_node.children.append(file)

# %%
visit = [root_node]
visited = []
while len(visit) > 0:
    node = visit.pop()
    visited.append(node)
    appended = False
    for ch in node.children:
        if isinstance(ch, Folder) and ch not in visited:
            appended = True
            visit.append(ch)
    if not appended:
        node.size()

total_size = 0
for v in visited:
    if v.size() <= 100000:
        total_size += v.size()


print(total_size)