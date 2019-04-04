class Solution1(object):
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '{': '}', '[': ']'}
        ss = []
        for i in s:
            if i in ['(', '{', '[']:
                ss.insert(len(ss), i)
            if i in [')', '}', ']']:
                if ss:
                    p = ss.pop()
                    if i != parentheses[p]:
                        return False
                else:
                    return False
        if ss == []:
            return True
        else:
            return False

class Solution2(object):
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('()', '')
            s = s.replace('[]', '')
        return s == ""
