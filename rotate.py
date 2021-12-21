import rospy
import math
from geometry_msgs.msg import Twist

def main():
    rospy.init_node("rotate")
    pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

    relative_speed = math.radians(99)
    angular_speed = 1.0
    duration = relative_speed/angular_speed
    time2end = rospy.Time.now() + rospy.Duration(duration)

    
    
    msg = Twist()
    msg.angular.z=angular_speed
    while rospy.Time.now()<time2end:
        pub.publish(msg)
        rospy.sleep(0.01)
        print("rotate")
    
    msg.angular.z=0.0
    pub.publish(msg)
    

if __name__=="__main__":
    main()
    pass