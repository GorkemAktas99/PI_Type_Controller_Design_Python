# PI_Type_Controller_Design_Python
This application shows that how to design a PI type controller in Python     
In this case, I have chosen a sample system that is Gs = 19*s/(23s**2+250*s+200).You can use familiar steps and realize PI type controller for your system.I have mentioned steps as comments.

The given transfer function input signal represents an acceleration and the output signal represents a dc motor with acceleration. 

It is not appropriate to use a PI controller for this system, as it can be seen in the output. But I showed it as an example. You can use similar algebraic methods when designing a PI controller.
For example, the most important part is that the values of kp and ki are found in terms of wn. This brought the need for tabulation to the designer. You can see the tabulation part in the example.
