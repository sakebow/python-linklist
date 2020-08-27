from Node import *
import random
# 链表
class Link:
  # 初始化 / 不需要参数，自带空的头节点
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    pass

  # 尾插法插入数据
  def insert_tail(self, index, data):
    if self.tail is None:
      self.insert_head(index, data)
    else:
      node = Node(data, None, index)
      self.tail.next = node
      self.tail = node
      self.length += 1
    pass
  
  # 头插法插入数据 
  def insert_head(self, index, data):
    node = Node(data, self.head, index)
    self.head = node
    self.length += 1
    # 当只有一个元素的时候，确定尾节点
    if self.length == 1:
      self.tail = node
      pass
    pass
  
  # 输出链表
  def output(self):
    if self.head is None:
      print('Nothing')
      return
      pass
    else:
      node = self.head
      while node is not None:
        print(f'{node.index}: {node.data}', end=' ')
        node = node.next
        pass
      print()
      pass
    pass
  
  # 随机生成链表
  def random_link(self, n):
    size = random.randint(0, n)
    for i in range(0, size):
      self.insert_tail(i + 1, LETTERS[random.randint(0, LETTERS_LEN - 1)])
      pass
    pass
  
  # 读取固定的链表
  def read_file(self, filepath):
    index = 1
    with open(filepath, 'r') as lines:
      for line in lines:
        self.insert_tail(index, line.rstrip('\n'))
        index += 1
        pass
      pass
    pass
  
  # 通过索引获得指定节点
  def get_node(self, index):
    node = self.head
    for i in range(1, index):
      node = node.next
      pass
    pass
    return node
  
  # 匹配内容删除节点
  def delete_node_by_data(self, data):
    # 强行改为有头节点的链表
    node = Node('a', self.head, 0)
    # 保持标识，最后需要删除
    stayHead = node
    # 游标，规定temp为必删项，node为上一项
    temp = self.head
    while temp is not None:
      if temp is self.head and temp.data == data:
        node.next = self.head = temp.next
        if temp is self.tail:
          self.tail = self.head = node.next
          pass
        del temp
        temp = node.next
        self.length -= 1
        pass
      elif temp is not self.head and temp.data == data:
        node.next = temp.next
        if temp is self.tail:
          self.tail = node
          pass
        del temp
        temp = node.next
        self.length -= 1
        pass
      else:
        temp = temp.next
        node = node.next
      pass
    del stayHead
    pass
  
  # 使用索引删除节点
  def delete_node_by_index(self, index):
    if self.head is None:
      return
      pass
    elif index == 1:
      node = self.head
      self.head = self.head.next
      if self.head is None:
        self.tail = self.head
        pass
      pass
      del node
    else:
      node = self.get_node(index - 1)
      temp = node.next
      if temp is self.tail:
        node.next = None
        self.tail = node
        del temp
        pass
      else:
        node.next = temp.next
        del temp
      pass
    pass