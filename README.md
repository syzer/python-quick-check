```bash
source ./venv/bin/activate
pip install hypothesis
pip install pytest
py.test encode.py
```


```python
....
  else:
>           entry = (character, count)
E           UnboundLocalError: local variable 'character' referenced before assignment
```