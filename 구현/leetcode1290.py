class Solution(object):
    def getDecimalValue(self, head):
        cur = head
        ret = 0
        while cur:
            ret = ret * 2 + cur.val
            cur = cur.next
        return ret
