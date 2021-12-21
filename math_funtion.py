import numpy as np
import math

laser_range=[0.1,0.2,0.3,0.4,0.5]
laser_arr=np.array(laser_range)
result = np.count_nonzero(laser_arr>=0.2)
# 라이다의 각도를 한정지었을때 가까이 있는지 없는지 탐지하는 알고리즘

cvt_radiang=math.radians(90)
cvt_degrees=math.degrees(cvt_radiang)
print(cvt_radiang,cvt_degrees)
# 1.5707963267948966 = 90'