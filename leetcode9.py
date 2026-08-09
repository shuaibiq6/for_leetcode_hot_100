#155题最小栈 
#有数字存入时stack和min_stack同时存入
# stack按照顺序存
# min_stack则将要存入的数和已有的数做比较，存入最小的，如果已有则再存一遍
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []        #定义两个栈，min_stack是辅助栈
        
    def push(self,val:int) -> None:
        self.stack.append(val)     #实现stack的正常入栈
        cur_min = val              #用cur_min获取val的值
        if self.min_stack:         #如果min_stack有数，就把cur_min赋值为min_stack栈最小的数                 
            cur_min = min(val,self.min_stack[-1])#把引入的参数和已有的栈顶做比较
        self.min_stack.append(cur_min)#如果min栈没数字，存入其中更小的一个，栈顶一直更新，新来的数字也只能存栈顶，保证栈顶始终是最小的
        
    def pop(self) -> None:#取走栈顶
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:#查看栈顶
        return self.stack[-1]
    
    def getMin(self) -> int:#查询栈里最小的值
        return self.min_stack[-1]