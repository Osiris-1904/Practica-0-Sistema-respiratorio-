"""
Práctica 0: Mecánica pulmonar

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Osiris Jaylin Chavez Hernandez 
Número de control: 23210697
Correo institucional: l23210697@tectijuana.edu.mx

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

numPID =  [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
denPID = [Re*Cr,t0]
PID = ctrl.tf(numPID,denPID)
print(f"Funcion de transferencia del controlador PID: {PID} \n")


# Sistema de control en lazo cerrado
x = ctrl.series(PID,sys)
sysPID = ctrl.feedback(x,1,sign = -1)
print(f"Funcion de transferencia del sistema de control en lazo cerrado: {sysPID}")

# Respuesta del sistema en lazo abierto y en lazo cerrado
_,PAu1 =  ctrl.forced_response(sys,t,u1,x0)
_,PAu2 =  ctrl.forced_response(sys,t,u2,x0)
_,PAu3 =  ctrl.forced_response(sys,t,u3,x0)
_,PAu4 =  ctrl.forced_response(sys,t,u4,x0)

_,PIDu1 = ctrl.forced_response(sysPID,t,u1,x0)
_,PIDu2 = ctrl.forced_response(sysPID,t,u2,x0)
_,PIDu3 = ctrl.forced_response(sysPID,t,u3,x0)
_,PIDu4 = ctrl.forced_response(sysPID,t,u4,x0)

clr1 = np.array([252,245,238])/255
clr2 = np.array([255,196,196])/255
clr3 = np.array([238,105,131])/255
clr4 = np.array([133,14,53])/255
clr5 = np.array([15,14,14])/255

fg1 =  plt.figure() #Respuesta al escalon
plt.plot(t,u1,'-',color =  clr1,label='Pao(t') #Entrada 
plt.plot(t,PAu1,'--',color=clr4,label='PA(t)') #Respuesta en lazo abierto 
plt.plot(t,PIDu1,':',color=clr5,label='PID(t)') #Respuesta en lazo cerrado
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t)] [V]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg1.savefig('step_python.pdf',bbox_inches='tight')

fg2 =  plt.figure() #Respuesta al impulso
plt.plot(t,u2,'-',color =  clr1,label='Pao(t') #Entrada 
plt.plot(t,PAu2,'--',color=clr4,label='PA(t)') #Respuesta en lazo abierto 
plt.plot(t,PIDu2,':',color=clr5,label='PID(t)') #Respuesta en lazo cerrado
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t)] [V]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg2.savefig('step_python.pdf',bbox_inches='tight')

fg3 =  plt.figure() #Respuesta a la rampa
plt.plot(t,u3,'-',color =  clr1,label='Pao(t') #Entrada 
plt.plot(t,PAu3,'--',color=clr4,label='PA(t)') #Respuesta en lazo abierto 
plt.plot(t,PIDu3,':',color=clr5,label='PID(t)') #Respuesta en lazo cerrado
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-0.05,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t)] [V]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg3.savefig('step_python.pdf',bbox_inches='tight')

fg4 =  plt.figure() #Respuesta a la funcion sinusoidal
plt.plot(t,u4,'-',color =  clr1,label='Pao(t') #Entrada 
plt.plot(t,PAu4,'--',color=clr4,label='PA(t)') #Respuesta en lazo abierto 
plt.plot(t,PIDu4,':',color=clr5,label='PID(t)') #Respuesta en lazo cerrado
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-1,1); plt.yticks(np.arange(-1,1.1,0.2))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t)] [V]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg4.savefig('step_python.pdf',bbox_inches='tight')