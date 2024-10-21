import rospy 
from ros_test.srv import memo 


def test_response(x, y) : 
    rospy.init_node('final_client_node')
    rospy.wait_for_service('answer1')

    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown(): 
        try : 
            string_service = rospy.ServiceProxy('answer1', memo)
            response = string_service(x, y)
            rospy.loginfo(response.result)
            rate.sleep()

        except rospy.ServiceException as e : 
            print('Service Call Failed %d', e)



if __name__ == '__main__': 
    test_response('hello', '30325 RSN')