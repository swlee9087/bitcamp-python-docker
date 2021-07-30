from typing import List

class Reverse(object):
    pass

    def str_to_list(self, payload: str) -> []:
        return [i for i in payload if i.isalnum()]


    def reverse_string(self, ls: []) -> []:
        left, right = 0
        #lens(ls)=-1
        '''while left<right:
            ls[left], ls[right] = ls[right],ls[left]
            left +=1
            right -=1'''
        return ls[::-1]

        # ls.reversed()        <- weird


    def list_to_str(self, ls: []) -> str:
        return ''.join([i for i in ls])

"""
if __name__ == '__main__':
    ls = str_to_list(input("Input "))
    print(list_to_str(reverse_list(ls)))
"""