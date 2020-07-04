import os
import glob
from glob import glob
dire="C:\\Users\\SSN-IT\\Downloads\\Commercials_avi_skandh2"
names=[y for x in os.walk(dire) for y in glob(os.path.join(x[0],"*.avi"))]

for i in names:
	cmd="python detect_video.py --video "+str(i)
	print(cmd)
	os.system(cmd)