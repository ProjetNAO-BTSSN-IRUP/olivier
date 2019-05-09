# -*- encoding: UTF-8 -*-
""" Record some sensors values and write them into a file.

"""
import os
import sys
import time

from naoqi import ALProxy

# MEMORY_VALUE_NAMES is the list of ALMemory values names you want to save.
ALMEMORY_KEY_NAMES = [
"Device/SubDeviceList/HeadYaw/Position/Sensor/Value",
"Device/SubDeviceList/HeadYaw/Position/Actuator/Value",
]

ROBOT_IP = "192.168.1.43"


def record_data(nao_ip):
    """
    Record the data from ALMemory.
    Returns a matrix of values
    """
    print "Recording data ..."
    print "Ip de NAO = " + nao_ip
    memory = ALProxy("ALMemory", nao_ip, 9559)
    data = list()
    for i in range (1, 100):
        line = list()
        for key in ALMEMORY_KEY_NAMES:
            value = memory.getData(key)
            line.append(value)
        data.append(line)
        time.sleep(0.05)
    return data


def main():
    """
    Parse command line arguments,
    run recordData and write the results
    into a csv file
    """
    if len(sys.argv) < 2:
        nao_ip = ROBOT_IP
    else:
        nao_ip = sys.argv[1]

    motion = ALProxy("ALMotion", nao_ip, 9559)
    # Set stiffness on for Head motors
    motion.setStiffnesses("Head", 1.0)
    # Will go to 1.0 then 0 radian
    # in two seconds

    motion.post.angleInterpolation(
        ["HeadYaw"],
        [3.0, -3.0],
        [1, 2],
        False
    )

    data = record_data(nao_ip)
    # Gently set stiff off for Head motors
    motion.setStiffnesses("Head", 0.0)

    output = os.path.abspath("record.csv")

    with open(output, "w") as fp:
        for line in data:
            fp.write("; ".join(str(x) for x in line))
            fp.write("\n")

    print "Results written to", output


if __name__ == "__main__":
    main()