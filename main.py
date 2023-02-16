#from detectar_qr import detectar_qr

from robobopy.Robobo import Robobo
from robobopy.utils.LED import LED
from robobopy.utils.Color import Color
from robobopy.utils.IR import IR
#from comportamientos_funciones import __all__
#buscar,centrar, agarrar,buscar_tacho,centrar_qr,reciclar,qr_dist,reset
import var_global as g
import comportamientos_funciones as cc

from comportamientos_funciones import *

#aquitecture, defined in var_globla file
def iniciar_arquitectura(i):      
    if (g.objetos_totales > i):
        print("Automata:")
        for comportamiento in g.automata:
            print("comportamiento: "+comportamiento)
            for accion in g.automata[comportamiento]:
                print("accion: "+accion)
                globals()[accion]()
        i =i+1
        g.rob.wait(3)
        iniciar_arquitectura(i)  




#manual comands funtion
def input_comandos():
    #input de control para debug
    #para inciar ejecutar comando "iniciar" desde consola
    while(g.condition):
        comand = input("accion?")
        if (comand=="end"):
            print(input)
            g.condition = 0
        elif(comand=="ad"):
            g.rob.moveWheelsByTime(15,15,1)
            g.rob.stopMotors()
        elif(comand=="atr"):
            g.rob.moveWheelsByTime(-15,-15,1)
            g.rob.stopMotors()
        elif(comand=="r_d"):
            g.rob.moveWheelsByTime(-2,2,1)
            g.rob.stopMotors()   
        elif(comand=="r_dd"):
            g.rob.moveWheelsByTime(-6,6,3)
            g.rob.stopMotors()
        elif(comand=="r_i"):
            g.rob.moveWheelsByTime(2,-2,1)
            g.rob.stopMotors()
        elif(comand=="til+"):
            g.til = g.til+20
            if g.til>104:
                g.til=105
            g.rob.moveTiltTo(g.til,100)
            print("til: "+str(g.til))
        elif(comand=="til-"):
            if g.til<5:
                g.til=5
            g.til = g.til-20
            print("til: "+str(g.til))
            g.rob.moveTiltTo(g.til,100)
        elif(comand=="pan+"):
            pan = g.pan+20
            if pan>160:
                pan=160
            print("pan: "+str(pan))
            g.rob.movePanTo(pan,100)
        elif(comand=="pan-"):
            pan = g.pan-20
            if pan<-160:
                pan=-160
            print("pan: "+str(pan))
            g.rob.movePanTo(pan,100)
        elif(comand=="rqr"):
            cc.buscar_tacho()
        elif(comand=="obj"):
            g.rob.startObjectRecognition()
            print("obj :"+str(g.rob.readDetectedObject().label))
            print("obj_X:"+ str(g.rob.readDetectedObject().x))
        elif(comand=="cla"):
            g.rob.startObjectRecognition()
            objt_detectado = str(g.rob.readDetectedObject().label)
            cc.clasificar(objt_detectado)
            print("obj :"+objt_detectado)
            print("obj_X:"+ str(g.rob.readDetectedObject().x))
        elif(comand=="src"):
            cc.buscar()
        elif(comand=="cent"):
            g.rob.startObjectRecognition()
            cc.centrar()
        elif(comand=="x"):
            g.rob.startObjectRecognition()
            print("obj_X:"+ str(g.rob.readDetectedObject().x))
        elif(comand=="ag"):
            cc.agarrar()
        elif(comand=="qr_cent"):
            cc.centrar_qr()
        elif(comand=="qr_dist"):
            cc.qr_dist()
        elif(comand=="qr_recic"):
            cc.reciclar()
        elif(comand=="reset"):
            cc.reset()
        elif(comand=="test"):
            cc.buscar()
            cc.centrar()
            cc.agarrar()
            cc.buscar_tacho()
            cc.centrar_qr()
            cc.reciclar()
            cc.reset()

            cc.buscar()
            cc.centrar()
            cc.agarrar()
            cc.buscar_tacho()
            cc.centrar_qr()
            cc.reciclar()
            cc.reset()
            
            cc.buscar()
            cc.centrar()
            cc.agarrar()
            cc.buscar_tacho()
            cc.centrar_qr()
            cc.reciclar()
            cc.reset()
        elif(comand=="iniciar"):
            iniciar_arquitectura(0)
    
#unncomment next line to start manual positioning, basic comands are defined in function above.    
#if enable manual will never stop unlees end comand in typed in console. 
#input_comandos()

iniciar_arquitectura(0)
