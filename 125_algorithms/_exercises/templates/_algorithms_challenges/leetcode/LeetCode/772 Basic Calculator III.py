#!/usr/bin/python3
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators
, open ( and closing parentheses ) and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-2147483648, 2147483647].

Some examples:
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

Note: Do not use the eval built-in library function.
"""


class Solution:
    ___ calculate(self, s: str) -> int:
        """
        make +, - lower precedence operator as a unary operation
        recursively handle bracket
        """
        s = s + "\0"  # signal the end
        ret, _ = self.eval(s, 0, [])
        r_ ret

    ___ eval(self, s, i, stk
        """
        return the cursor since the cursor advances in recursion
        """
        operand = 0
        prev_op = "+"
        w___ i < le.(s
            c = s[i]
            __ c __ " ":
                pass  # not continue since need trigger i += 1
            ____ c.isdigit(
                operand = operand * 10 + int(c)
            ____ c in ("+", "-", "*", "/", ")", "\0"   # delimiter
                __ prev_op __ "+":
                    stk.append(operand)
                ____ prev_op __ "-":
                    stk.append(-operand)
                ____ prev_op __ "*":
                    prev_operand = stk.p..
                    stk.append(prev_operand * operand)
                ____ prev_op __ "/":
                    prev_operand = stk.p..
                    stk.append(int(prev_operand / operand))

                __ c in ("+", "-", "*", "/"
                    operand = 0
                    prev_op = c
                ____ c in (")", "\0"
                    r_ su.(stk), i
            ____ c __ "(":  # "(" is not delimiter
                operand, i = self.eval(s, i + 1, [])
            ____
                raise

            i += 1


__ __name__ __ "__main__":
    assert Solution().calculate("(( ( ( 4- 2)+ ( 6+ 10 ) )+ 1) /( ( ( 7 + 9 )* ( 5*8) )- ( 5 + ( 2 * 10 ) ) ) )") __ 0
    assert Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3") __ -12
