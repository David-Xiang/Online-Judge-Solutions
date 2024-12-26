#
# @lc app=leetcode.cn id=591 lang=python3
#
# [591] 标签验证器
#


# @lc code=start
class Solution:
    TYPE_TAG_START = 0
    TYPE_TAG_END = 1
    TYPE_TAG_CONTENT = 2
    TYPE_TAG_CDDATA = 3
    TYPE_EOF = 4
    TYPE_UNKNOWN = 5

    def isValid(self, code: str) -> bool:
        self.init(code)
        has_tag = False
        while True:
            token, token_type = self.read()
            print(f"{token} type{token_type}")
            if token_type == self.TYPE_TAG_START:
                if not self.valid_tag(token):
                    return False
                has_tag = True
                self.stk.append(token)
            elif token_type == self.TYPE_TAG_END:
                if not self.valid_tag(token):
                    return False
                if len(self.stk) == 0 or self.stk[-1] != token:
                    return False
                self.stk.pop()
                if len(self.stk) == 0 and self.idx != len(self.code):
                    return False  # multiple roots are not allowed
            elif token_type == self.TYPE_TAG_CONTENT:
                if len(self.stk) == 0:
                    return False
            elif token_type == self.TYPE_TAG_CDDATA:
                if len(self.stk) == 0:
                    return False
            elif token_type == self.TYPE_EOF:
                if len(self.stk) == 0:
                    return has_tag  # 防止空串
                return False
            else:
                return False

    def init(self, code):
        self.stk = []
        self.idx = 0
        self.code = code

    def valid_tag(self, tag):
        if len(tag) > 9 or len(tag) < 1:
            return False
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if not all([i in chars for i in tag]):
            return False
        return True

    def skip_following_blank(self):
        while self.idx < len(self.code) and self.code[self.idx] == " ":
            self.idx = self.idx + 1  # 跳过空格

    def read(self):
        self.skip_following_blank()
        if self.idx == len(self.code):
            return "", self.TYPE_EOF
        if self.code[self.idx] == "<":
            if (
                self.idx + 8 < len(self.code)
                and self.code[self.idx : self.idx + 9] == "<![CDATA["
            ):
                # CDDATA
                # print(f'parse CDDATA, rest is {self.code[self.idx:]}')
                start_idx = self.idx
                self.idx = self.idx + 9
                while self.idx + 3 < len(self.code):
                    # print(self.code[self.idx:self.idx+3])
                    if self.code[self.idx : self.idx + 3] == "]]>":
                        token = self.code[start_idx + 9 : self.idx]
                        self.idx = self.idx + 3
                        self.skip_following_blank()
                        return token, self.TYPE_TAG_CDDATA
                    self.idx = self.idx + 1
                return self.code[start_idx:], self.TYPE_UNKNOWN

            # TAG START AND END
            is_end = False
            if self.idx + 1 < len(self.code) and self.code[self.idx + 1] == "/":
                is_end = True
                self.idx = self.idx + 1
            start_idx = self.idx + 1
            while self.idx < len(self.code) and self.code[self.idx] != ">":
                self.idx = self.idx + 1
            if self.idx < len(self.code) and self.code[self.idx] == ">":
                self.idx = self.idx + 1
                token = self.code[start_idx : self.idx - 1]
                self.skip_following_blank()
                return token, (self.TYPE_TAG_END if is_end else self.TYPE_TAG_START)
            else:
                self.idx = self.idx + 1
                token = self.code[start_idx : self.idx]
                self.skip_following_blank()
                return token, self.TYPE_UNKNOWN

        start_idx = self.idx
        while self.idx < len(self.code):
            if self.code[self.idx] == "<":
                break
            self.idx = self.idx + 1
        token = self.code[start_idx : self.idx]
        self.skip_following_blank()
        return token, self.TYPE_TAG_CONTENT


# @lc code=end


def test():
    solution = Solution()
    assert solution.isValid("<DIV>This is the first line</DIV>") == True
    assert solution.isValid("<DIV>This is the first <b>line</b></DIV>") == False
    assert solution.isValid("<DIV>  unmatched <  </DIV>") == False
    assert (
        solution.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>") == True
    )
    assert (
        solution.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>") == True
    )
    assert solution.isValid("<A>  <B> </A>   </B>") == False
    assert solution.isValid("<DIV>  div tag is not closed  <DIV>") == False
    assert solution.isValid("<DIV>  unmatched <  </DIV>") == False
    assert (
        solution.isValid("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>")
        == False
    )
    assert (
        solution.isValid(
            "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
        )
        == False
    )


if __name__ == "__main__":
    test()
