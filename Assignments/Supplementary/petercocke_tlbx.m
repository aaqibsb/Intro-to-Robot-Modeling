clear all
clf

d1=0.333; d3=0.3160; d5=0.3840; d7=0.1070; a3=0.088;

L(1)=Link([0, d1,  0,  pi/2, 0]);
L(2)=Link([0,  0,  0, -pi/2, 0]);
L(3)=Link([0, d3, a3, -pi/2, 0]);
L(4)=Link([0,  0,-a3,  pi/2, 0]);
L(5)=Link([0, d5   0,  pi/2, 0]);
L(6)=Link([0,  0, a3, -pi/2, 0]);
L(7)=Link([0,-d7,  0,     0, 0]);

robot = SerialLink (L);
robot.name = 'Panda';
robot.teach