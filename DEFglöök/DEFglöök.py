def loe_failist(fail:str):
     """Loeme Failist read ja salvestame järjendisse. Funktsioon
     tagastab järjend
     parem str fail:
     rtype: list
     """

f=open(fail,'r',endcoding="utf-8")
järjend=[]
for riada in f:
    järjend.append(rida.strip())
f.close
return järjend