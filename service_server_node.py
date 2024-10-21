import rospy 
from ros_test.srv import memo, memoResponse 


def ans_1(request): 
    test = request.a + '  ' + request.b
    return memoResponse(test)


def test_ans() : 
    rospy.init_node('finnal_server_node')
    service1 = rospy.Service('answer1', memo, ans_1)
    
    
if __name__ == '__main__': 
    test_ans() 
    rospy.spin() 