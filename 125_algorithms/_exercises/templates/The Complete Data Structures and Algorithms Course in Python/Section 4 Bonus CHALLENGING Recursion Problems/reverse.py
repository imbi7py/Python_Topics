#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# reverse Solution


___ reverse(strng
    __ len(strng) <= 1:
      return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'