#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# stringifyNumbers Solution

def stringifyNumbers(obj):
    newObj = obj
    for key in obj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) == dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj



obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))

{'num': '1',
 'test': [],
 'data': {'val': '4',
          'info': {'isRight': True, 'random': '66'}
          }
}