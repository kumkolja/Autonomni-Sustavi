# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64



class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('kvadriranje_broja')
        self.subscription = self.create_subscription(Int64, 'broj', self.listener_callback, 10,)
        self.subscription  # prevent unused variable warning
        
        self.subscription = self.create_subscription(Int64, 'broj', self.timer_callback, 10,)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Kvadrirani broj: "%d"' % msg.data**2)

    def timer_callback(self, msg):
        self.publisher_ = self.create_publisher(Int64, 'kvadrat_broja', 10)
        kvadrat = Int64()
        kvadrat.data = msg.data**2
        self.publisher_.publish(kvadrat)


def main(args=None):
    rclpy.init(args=args)

    kvadriranje_broja = MinimalSubscriber()

    rclpy.spin(kvadriranje_broja)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    kvadriranje_broja.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
