import time
import os

os.environ["BLINKA_MCP2221"] = "1"


import board

import adafruit_drv2605
import busio

# Reference link:
# https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221/windows
# https://www.adafruit.com/product/2305
# https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout/python-circuitpython

def testing(int):
    # Initialize the I2C bus 初始化 I2C 总线
    i2c = busio.I2C(board.SCL, board.SDA)

    # Creating DRV2605L Objects 创建 DRV2605L 对象
    drv = adafruit_drv2605.DRV2605(i2c)

    # Testing vibration effects 测试振动效果
    print("Testing vibration effects...")

    # Trigger different types of vibration effects 触发不同类型的振动效果
    #drv.sequence[0] = adafruit_drv2605.Effect(1)  # 振动类型 1，强度 255
    drv.sequence[0] = adafruit_drv2605.Effect(int)  # Vibration type 1, intensity 255 振动类型 1，强度 255
    drv.play()

    # Wait a while. 等待一段时间
    time.sleep(1)

    # Stop Vibration 停止振动
    drv.stop()

    # print("Vibration test completed.")


