```
source ./venv/bin/activate
pip install hypothesis
pip install pytest
py.test encode.py
```


```
....
  else:
>           entry = (character, count)
E           UnboundLocalError: local variable 'character' referenced before assignment
```