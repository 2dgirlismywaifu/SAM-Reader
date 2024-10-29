# excute samreader.py in same directory
from sam import samreader

reg = "sam.reg"
jd = "098f523c"
skew1 = "99b1ffb6"
gbg = "67aa057f"
data = "d8a3b725"

domain = samreader.LMDomain(reg, jd, skew1, gbg, data)
print(domain)
