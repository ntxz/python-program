class Deque:
    def __init__(self,iterable=None,maxlen=10):
        if iterable==None:   #队列为空
            self.content=[]  #初始队列内容
            self.current=0  #初始队列大小
        else:
            self.content=list(iterable)
            self.current=len(iterable)
        self.size=maxlen
        if self.size<self.current:
            self.size=self.current
    def __del__(self):
        del self.content
        #修改队列大小
    def setSize(self,size):
        if size<self.current:
            #缩小队列同时删除后边元素
            for i in range(size,self.current)[::-1]:
                del self.content[i]
            self.current=size
        self.size=size
        #右侧入栈
    def appendRight(self,v):
        if self.current<self.size:
            self.content.append(v)
            self.current=self.current+1
        else:
            print('队列已满')
        #左侧入站
    def appendLeft(self,v):
        if self.current<self.size:
            self.content.insert(0,v)
            self.current=self.current+1
        else:
            print('队列已满')
    def popLeft(self):
        if self.content:
            self.current=self.current-1
            return self.content.pop(0)
        else:
            print('队列已空')
    def popRight(self):
        if self.content:
            self.current=self.current-1
            return self.content.pop()
        else:
            print('队列已空')
        #循环移位
    def rorate(self,k):
        if abs(k)<self.current:
            print('k must<='+str(self.current))
            return self.content=self.content[-k:]+self.content[:-k]
#元素翻转   
    def reverse(self):
        self.content=self.content[::-1]
#显示当前队列元素个数
    def __len__(self):
        return self.current
#显示当前队列元素
    def __str__(self):
        return 'Deque(' + str(self.content) + ',maxlen=' + str(self.size) + ')'
    # 队列置空
    def clear(self):
        self.content = []
        self.current = 0

    # 测试队列是否为空
    def isEmpty(self):
        return not self.content

    # 测试队列是否已满
    def isFull(self):
        return self.current == self.size


if __name__ == '__main__':
    print('Please use the file as a module that deque.')    

