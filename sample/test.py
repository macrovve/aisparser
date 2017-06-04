from aisparser import Parser
p = Parser()

vdm = p.parse(
    '20160812 - 01:40:20	\g:3-4-01864,n:08021,c:0000000162*52\!ARVDM,1,1,,A,16:`e0mP1:8N3OD=oj:QFwvR0p9J,0*38'
)
print(vdm.channel)
print(vdm.latitude)
print(vdm.longitude)
print(vdm.cog)
print(vdm.total_num)
print(vdm.true_heading)

vdm = p.parse(
    '20160323 - 02:27:16	!AIVDM,2,1,6,A,569E7;P000008d5N221QF1T4pN3V22222222221@;0L,0*3D'
)
vdm = p.parse(
    '20160323 - 02:27:16	!AIVDM,2,2,6,A,5;4rR0=SPCRRCQp8888888888880,2*17')
print('call_sign', vdm.call_sign)
print('name', vdm.name)
print('maximum_draught', vdm.maximum_draught)
print('imo_number', vdm.imo_number)
