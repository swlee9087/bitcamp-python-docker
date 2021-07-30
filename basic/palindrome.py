class Palindrome(object):
    pass


    def str_to_list(self, payload: str) -> []:
        return [i for i in payload if i.isalnum()]


    def isPalindrome(self, ls: []) -> bool:
        """strs = []
        for char in ls:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
    """
        return {"result": True for i in ls if ls.pop(0) != ls.pop()}

"""
if __name__ == '__main__':
    ls = str_to_list("A man, a plan, a canal: Panama")
    print(ls)
    isPal = isPalindrome(ls)
    print(isPal["result"])"""
