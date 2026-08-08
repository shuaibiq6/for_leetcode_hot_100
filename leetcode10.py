# 20题有效括号
#定义的stack只存左括号
#拿stack中的值跟mapping中的key做对应识别
def isValid(s:str) -> bool:
    stack = []
    mapping = {')':'(','[':']','{':'}'}             #根据右括号对左括号实现匹配
    for i in s:                                     #遍历参数字符串中的每一个字符
        if i in mapping:                            #如果识别到右括号：i对应字典中的key（右括号）如果不是则作为左括号压入栈底
            if not stack or stack[-1] != mapping[i]:#如果栈为空或者栈顶左括号跟mapping中的value值（左括号）不匹配则返回false，如果匹配则弹出这个左括号
                return False                        
            stack.pop()
        else:
            stack.append(i)
    return len(stack) == 0