# version: Python3
# Objectif : tester les commandes DobotEDU disponibles avec le préfixe `magician.`

from DobotEDU import *

# ========== MOUVEMENT ==========
print("TEST - get_pose()")
pose = magician.get_pose()
print("Position actuelle :", pose)

print("TEST - set_home_cmd()")
magician.set_home_cmd(250, 0, 0, 0)

print("TEST - go_home()")
magician.go_home()
magician.wait(2)

print("TEST - set_ptp_cmd()")
# Déplace vers une position sûre
magician.set_ptp_cmd(250, 0, -20, 0)
magician.wait(2)

# ========== SUCCION / PINCE ==========
print("TEST - set_suction_cup()")
magician.set_suction_cup(True)
magician.wait(1)
magician.set_suction_cup(False)

print("TEST - set_gripper()")
# set_gripper(on: bool, open: bool)
magician.set_gripper(True, False)  # Ferme
magician.wait(1)
magician.set_gripper(True, True)   # Ouvre
magician.wait(1)
magician.set_gripper(False, False) # Coupe l’alim

# ========== I/O ==========
print("TEST - set_digital_output()")
magician.set_digital_output(1, True)
magician.wait(1)
magician.set_digital_output(1, False)

# ========== PWM (ex: moteur tapis) ==========
print("TEST - set_pwm_output()")
magician.set_pwm_output(1, 1000)  # 1kHz PWM sur canal 1
magician.wait(1)
magician.set_pwm_output(1, 0)

# ========== CAPTEURS ==========
print("TEST - get_infrared_sensor_value()")
ir = magician.get_infrared_sensor_value(4)  # GP4
print("Capteur de proximité GP4 :", ir)

print("TEST - get_color_sensor_value()")
r, g, b = magician.get_color_sensor_value(2)  # GP2
print("Capteur couleur RGB GP2:", r, g, b)

# ========== PARAMÈTRES AVANCÉS ==========
print("TEST - set_ptp_joint_params()")
magician.set_ptp_joint_params([100, 100, 100, 100], [100, 100, 100, 100])

print("TEST - set_end_effector_params()")
magician.set_end_effector_params(70, 0, 0)

# ========== TEMPS ==========
print("TEST - wait()")
print("Attente 2 secondes...")
magician.wait(2)

# ========== FIN ==========
print("Fin des tests DobotEDU - Python Lab (magician)")