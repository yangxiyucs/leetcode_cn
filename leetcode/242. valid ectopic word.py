# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
# 通过次数75,895提交次数129,603
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-anagram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #-------------------
        # d = collections.defaultdict(int)
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #   d[s[i]] += 1
        #   d[t[i]] -= 1
        # for val in d.values():
        #     if val != 0:
        #         return False
        # return True

        #-----------------
        # return sorted(s) == sorted(t)

        #------------------
        #内存占用低
        if len(s) != len(t): return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较字符元素个数比较字符的个数
                if s.count(i) != t.count(i):return False
            return True
        else:
            return False
