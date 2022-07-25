from argparse import ArgumentParser

from frankx import Affine, JointMotion, LinearMotion, Robot


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', default='192.168.5.11', help='FCI IP of the robot')
    args = parser.parse_args()

    # Connect to the robot
    robot = Robot(args.host)
    robot.set_default_behavior()
    robot.recover_from_errors()
    robot.set_dynamic_rel(0.15)

    # Joint motion
    # robot.move(JointMotion([-1.811944, 1.179108, 1.757100, -2.14162, -1.143369, 1.633046, -0.432171]))
    robot.move(JointMotion([0.03976535462339719, -0.08233591717772797, -0.04743333797444377, -2.0550680074848047, -0.019504090294408277, 1.9364382128980424, 0.8217949675089783]))

    # # Define and move forwards
    camera_frame = Affine(y=0.05)
    # home_pose = Affine(0.480, 0.0, 0.40)

    # robot.move(camera_frame, LinearMotion(home_pose, 1.75))
