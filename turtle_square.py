import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.state = 0
        self.counter = 0
        self.sides_done = 0  # عداد الأضلاع اللي خلصت

    def timer_callback(self):
        if self.sides_done >= 4:
            # خلصنا 4 أضلاع، نوقف السلحفاة ونطفي البرنامج
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Square completed!')
            rclpy.shutdown()
            return

        msg = Twist()

        if self.state == 0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.counter += 1
            if self.counter >= 20:
                self.state = 1
                self.counter = 0
        else:
            msg.linear.x = 0.0
            msg.angular.z = math.pi / 2
            self.counter += 1
            if self.counter >= 10:
                self.state = 0
                self.counter = 0
                self.sides_done += 1  # خلصنا ضلع كامل

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSquare()
    rclpy.spin(node)
    node.destroy_node()


if __name__ == '__main__':
    main()
