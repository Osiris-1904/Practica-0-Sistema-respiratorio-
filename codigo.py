"""
Práctica 0: Mecánica pulmonar

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Nombres y Apellidos
Número de control: 12345678
Correo institucional: xxx.xxx@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0, t0, tend, dt, w, h = 0, 0, 10, 1E-3, 7, 3.5
N = round(tend/dt) + 1
t = np.linspace(t0, tend, N)
u1 = np.ones(N)  # Step
u2 = np.zeros(N); u2[round(1/dt):round(2/dt)] = 1  # Impulse
u3 = t/tend  # Ramp
u4 = np.sin(m.pi/2*t)  # Sine function

# Componentes del circuito RLC y función de transferencia
R, L, C = 10E3, 33E-6, 10E-6
num = [1]
den = [C*L, C*R, 1]
sys = ctrl.tf(num, den)
print(f"Funcion de transferencia del sistema: {sys}")

# Componentes del controlador
kP, kI, kD = 17.392, 850.664, 0.027
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re
Ce = kD/Rr
print(f"El valor de capacitancia Cr es de {Cr} faradios.\n")
print(f"El valor de resistencia Re es de {Re} faradios.\n")
print(f"El valor de resistencia Rr es de {Rr} faradios.\n")
print(f"El valor de capacitancia Ce es de {Ce} faradios.\n")

# Sistema de control en lazo cerrado




# Respuesta del sistema en lazo abierto y en lazo cerrado
