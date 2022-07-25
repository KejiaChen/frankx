from argparse import ArgumentParser
from frankx import Affine, JointMotion, LinearMotion, LinearRelativeMotion, Robot
from threading import Thread
import time


def home(robot):
    robot.set_default_behavior()
    robot.recover_from_errors()
    robot.set_dynamic_rel(0.15)

    # Joint motion
    # robot.move(JointMotion([-1.811944, 1.179108, 1.757100, -2.14162, -1.143369, 1.633046, -0.432171]))
    robot.move(JointMotion([0.03976535462339719, -0.08233591717772797, -0.04743333797444377, -2.0550680074848047, -0.019504090294408277, 1.9364382128980424, 0.8217949675089783]))
    print("Homing finished")


def move(robot):
    robot.set_default_behavior()
    robot.recover_from_errors()

    # Reduce the acceleration and velocity dynamic
    robot.set_dynamic_rel(0.15)

    # Define and move forwards
    way = Affine(0.0, 0.2, 0.0)
    motion_forward = LinearRelativeMotion(way)
    robot.move(motion_forward)

    # And move backwards using the inverse motion
    motion_backward = LinearRelativeMotion(way.inverse())
    robot.move(motion_backward)
    print("finished time", time.time())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-l', '--list', help='FCI IPs of the robots', type=lambda s: ["192.168.5."+item for item in s.split(',')])
    args = parser.parse_args()

    # list of hosts
    host_list = args.list
    robot_list = []
    for host in host_list:
        print("Connecting to %s" %host)
        # Connect to the robot
        robot_list.append(Robot(host))
    
    thread1 = Thread(target=home, args=(robot_list[0],))
    thread2 = Thread(target=home, args=(robot_list[1],))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    thread1 = Thread(target=move, args=(robot_list[0],))
    thread2 = Thread(target=move, args=(robot_list[1],))
    thread1.start()
    thread2.start()

    
