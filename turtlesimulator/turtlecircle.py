import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleCircle(Node):
    def __init__(self):
        super().__init__('turtlesim')
        self.publisher_=self.create_publisher(Twist, '/turtle1/cmd_vel',10)
        self.radius = 2.0
        self.speed = 2.0
        self.timer_ = self.create_timer(0.1,self.spin_turtle)
        self.get_logger().info('Tutel start')

    def spin_turtle(self):
        msg = Twist()
        msg.linear.x = self.speed
        msg.angular.z = self.speed / self.radius
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = TurtleCircle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()