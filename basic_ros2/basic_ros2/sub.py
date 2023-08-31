import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'chatter', self.chatter_callback, 10)

    def chatter_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    minimalSub = MinimalSubscriber()
    rclpy.spin(minimalSub)
    minimalSub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
