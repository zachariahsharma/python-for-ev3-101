motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_b.run_angle(500, 720, Stop.BRAKE, False)
motor_c.run_angle(500, 720, Stop.BRAKE, True)
motor_b.run_angle(-500, 720, Stop.BRAKE, False)
motor_c.run_angle(-500, 720, Stop.BRAKE, True)