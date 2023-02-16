# Basic autonomous robot implementation 

# The code is intended to test autonomous driving inside an open source robot platform called robobo
#all the info about the project, simulator and libraries can be found here https://theroboboproject.com/en/

# video of code implemented in simulator https://drive.google.com/file/d/10tR_E3HIZ8k3vy9p_2LYaLvwiiqj30rp/view
# Video of robot in reality https://drive.google.com/file/d/1VCsk1lI1y0OCoXvizUUUUiXxYUcsNSyo/view?usp=share_link

# the code is programmed in python using a basic structure of a cognitive architecture where behaviours are repeated in loop and acceced when needed depending on external factors, and already done actions. 
# The idea behind the architecture is to study the posibility of the robot movements to be directly conected to sensors and camera to face different initial conditions for a recycling task. 
# The robot is programed to search for an object, approach it, search for the correspondent tash can and push it to the can. 
# The proyect was build to proove the posibilities of hierarquical behaviours as (rudimentary but effective) initial approach to open ended problems.

# Backlog: 
 - Armar clase automata con los metodos de los comportamientos y las variables correspondientes 
 - Hacer un refactor
 - Armar setup con inicializaciones de la instalacia de la clase robobo y la clase automata
 - agregar mover cabeza para determinar de que lado se encuentra el obj y Qr antes de moverse(pan)
 - agregar sistema de deteccion de fallos del sensor para evitar erraticas ante fallos de lectura 
