"""
    @author Görkem Aktaş
    @date 30.04.2021
    @brief This application shows that how to design a PI type controller in Python
    In this case, I have chosen a sample system that is Gs = 19*s/(23s**2+250*s+200).
    You can use familiar steps and realize PI type controller for your system
    I have mentioned steps as comments

    The given transfer function input signal represents an acceleration and the
    output signal represents a dc motor with acceleration.

    It is not appropriate to use a PI controller for this system, as it can be seen in the output.
    But I showed it as an example. You can use similar algebraic methods when designing a PI controller.

    For example, the most important part is that the values of kp and ki are found in terms of wn.
    This brought the need for tabulation to the designer. You can see the tabulation part in the example.
"""
from sympy import *
import numpy as np
from control import *
import matplotlib.pyplot as plt

Gs = tf([19,0],[23,250,200])
s = Symbol('s')
Gss = 19*s/(23*s**2+250*s+200)
kp,ki = symbols('kp ki')
Fss = (kp*s+ki)/s
Tss = (Fss*Gss)/(1+Fss*Gss)
print(Fss)
print(simplify(expand(Tss,s)))
Tss = cancel(Tss)
num,den = fraction(Tss)
print(den)
den = Poly(den,s)
den_coef=den.coeffs()
print(den_coef)
zeta = 1
wn = Symbol('wn')
pds = s**2+2*zeta*wn*s+wn**2
pds = Poly(pds,s)
pds_coef = pds.coeffs()
for i in range(len(pds_coef)):
    pds_coef[i] = 23*pds_coef[i]
print(pds_coef)
eq_list = []
for i in range(1,len(den_coef)):
    eq_list.append(Eq(den_coef[i],pds_coef[i]))
print(eq_list)
sol = nonlinsolve(eq_list,[kp,ki,wn]) #NonLinear Solution
print(sol)
"""Table Form"""

for i in sol:
    for j in np.linspace(0,10,1000):
        val = i.subs(wn,j)
        print(val,(4/(j)))
    print("-----------")

"""
    We look at the table and have to choose suitable settling time
    We want no overshoot, so we have chosen zeta value is 1
    If we look at the table, we choose settling time for 0.5 seconds approximately
    So, wn value equals to 7.86786786786787
"""
wnval = 7.86786786786787
solution_list = []
for i in sol:
    i=i.subs(wn,wnval)
    solution_list.append(i)
print(solution_list)
sol_coeffs = []
for i in solution_list[0]:
    sol_coeffs.append(i)
del sol_coeffs[2]
print(sol_coeffs)
Fs_coeffs = np.array(sol_coeffs,ndmin=1,dtype=np.dtype(float))
Fs = tf(Fs_coeffs,[1,0])
print(Fs)
Ts = feedback(Fs*Gs,1)
print(Ts)
t,y = step_response(Ts)
plt.plot(t,y)
plt.grid()
plt.show()

