# AIS Parser

## Quick Start
Parse one line at a time

```python
from aisparser import Parser
p=Parser()
vdm=p.parse('20160812 - 01:40:20	\g:3-4-01864,n:08021,c:0000000162*52\!ARVDM,1,1,,A,16:`e0mP1:8N3OD=oj:QFwvR0p9J,0*38')
print(vdm.type_)
print(vdm.msg_id)
print(vdm.channel)
print(vdm.latitude)
print(vdm.longitude)
print(vdm.cog)
```

Parse from file
```python 
from aisparser import Parse
p=Parse()
for record in p.from_file(filename):
    print(record.msg_id)
```   



## TODO
- [ ] Easy tool for parsing from file
- [ ] Full support for VDM
- [ ] Upload to PYPI

 