from time import sleep
from frankx import Affine, JointMotion, ImpedanceMotion, Robot
from argparse import ArgumentParser

if __name__ == '__main__':
    # Connect to the robot
    parser = ArgumentParser()
    parser.add_argument('--host', default='172.16.0.2', help='FCI IP of the robot')
    args = parser.parse_args()

    robot = Robot(args.host)
    robot.set_default_behavior()
    robot.recover_from_errors()

    # Reduce the acceleration and velocity dynamic
    robot.set_dynamic_rel(0.02)

    joint_motion = JointMotion([-1.811944, 1.179108, 1.757100, -2.14162, -1.143369, 1.633046, -0.432171])
    robot.move(joint_motion)
    print("start to use impededance motion")

    # Define and move forwards
    impedance_motion = ImpedanceMotion(200.0, 20.0)
    robot_thread = robot.move_async(impedance_motion)

    sleep(0.05)

    initial_target = impedance_motion.target
    print('initial target: ', initial_target)

    sleep(0.5)

    impedance_motion.target = Affine(y=0.25) * initial_target
    print('set new target: ', impedance_motion.target)

    sleep(2.0)

    impedance_motion.finish()
    robot_thread.join()
    print('motion finished')
