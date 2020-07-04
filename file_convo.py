import os
import glob
from glob import glob

dire1="C:\\Users\\SSN-IT\\Downloads\\Commercials_avi_skandh"
names_1=[y for x in os.walk(dire1) for y in glob(os.path.join(x[0],"*.avi"))]
print(*names_1)
dire="C:\\Users\\SSN-IT\\Downloads\\Commercials_avi_skandh2"
names=[y for x in os.walk(dire) for y in glob(os.path.join(x[0],"*.avi"))]
dire2="C:\\Users\\SSN-IT\\Downloads\\Commercials_avi_skandh2\\"
for i in range(len(names)):
	r=dire2+str(i)+".avi"
	os.rename(names[i],r)

dire="C:\\Users\\SSN-IT\\Downloads\\Commercials_avi_skandh2"
names=[y for x in os.walk(dire) for y in glob(os.path.join(x[0],"*.avi"))]
print(*names)