# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Challenge
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------
# Algorithm

# In summary : Form all posible sub_strings from original string, then return length of longest sub_string

# - start from 1st character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string or 
    
    
# - start from 2nd character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string


# ....


# - start from final character, form as long as posible sub string
#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string
# ---------------------------------------------------------------

st. _ "abcbb"

___ longest_non_repeat(st.):
    
    # init start position and max length     
    i_0
    max_length _ 1

    ___ i,c __ enumerate(st.):

        # init counter and sub string value         
        start_at _ i
        sub_str_  # list

        # continue increase sub string if did not repeat character         
        while (start_at < le.(st.)) an. (st.[start_at] not __ sub_str):
            sub_str.ap..(st.[start_at])
            start_at _ start_at + 1

        # update the max length   
        __ le.(sub_str) > max_length:
            max_length _ le.(sub_str)

        print(sub_str)
        
    r_ max_length

longest_non_repeat(st.)


