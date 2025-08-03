import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
import serial

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('arduino_serial_node')
        self.declare_parameter('serial_port', '/dev/ttyACM0') # Adjust port as needed
        self.declare_parameter('baud_rate', 9600)

        self.serial_port = self.get_parameter('serial_port').value
        self.baud_rate = self.get_parameter('baud_rate').value

        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            self.get_logger().info(f"Connected to Arduino on {self.serial_port} at {self.baud_rate} baud.")
        except serial.SerialException as e:
            self.get_logger().error(f"Could not open serial port: {e}")
            rclpy.shutdown()
            return

        self.publisher_ = self.create_publisher(Int32, 'arduino_sensor_data', 10)
        self.timer = self.create_timer(0.1, self.read_serial_data) # Read serial data periodically

    def read_serial_data(self):
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line.startswith("Distanz(cm):"):
                    try:
                        value = int(line.split(':')[1])
                        msg = Int32()
                        msg.data = value
                        self.publisher_.publish(msg)
                        self.get_logger().info(f'Publishing: "{msg.data}"')
                    except ValueError:
                        self.get_logger().warn(f"Invalid sensor value received: {line}")
            except UnicodeDecodeError:
                self.get_logger().warn("Could not decode serial data.")

def main(args=None):
    rclpy.init(args=args)
    arduino_node = MinimalPublisher()
    rclpy.spin(arduino_node)
    arduino_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
