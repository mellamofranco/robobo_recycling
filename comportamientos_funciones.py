__all__ = ['buscar', 'centrar', 'agarrar','buscar_tacho','centrar_qr','reciclar','qr_dist','reset']

import var_global as g
from robobopy.utils.LED import LED
from robobopy.utils.Color import Color
from robobopy.utils.IR import IR


def clasificar(objt):
    for i in g.tachos:
        for j in g.tachos[i]:
            if j == objt:
                g.datos_objDet["target_tacho"] = i
                print("target_tacho: "+g.datos_objDet["target_tacho"])
                break

def buscar():
    print("buscar")
    g.datos_objDet["detectado"] = 0
    g.rob.startObjectRecognition()
    g.rob.moveTiltTo(95,100)
  
    while (g.datos_objDet["detectado"] != 1):       
        g.datos_objDet["obj_ya_reciclado"] = 0
        
        d = g.rob.readDetectedObject().label
        
        print("objeto detectado: "+str(g.datos_objDet["detectado"]))
        for i in g.obj_reciclados:
            if i == d:
                print("Objeto ya reciclado :"+str(d))
                g.datos_objDet["obj_ya_reciclado"] = 1
                break
                
        if (d != '' and g.datos_objDet["obj_ya_reciclado"] !=1 ):
            g.datos_objDet["detectado"] = 1
            objt_detectado = str(g.rob.readDetectedObject().label)
            g.datos_objDet["objeto"] = objt_detectado
            print("objeto detectado :"+g.datos_objDet["objeto"])
            print("obj_X:"+ str(g.rob.readDetectedObject().x))
            clasificar(objt_detectado)
            break
        g.rob.moveWheelsByTime(2,-3,1)
        g.rob.wait(0)
        g.rob.stopMotors()
        print("obj_X:"+ str(g.rob.readDetectedObject().x))

def centrar():
    print("centrar")
    
    while(g.datos_objDet["centrado"] == 0):
    
        g.datos_objDet["lado"] = ""    
        if(g.rob.readDetectedObject().label == g.datos_objDet["objeto"]):
            g.datos_objDet["x"] = g.rob.readDetectedObject().x
            print("X:"+ str(g.datos_objDet["x"])) 
        
        if(g.rob.readDetectedObject().label == g.datos_objDet["objeto"]):    
            if (g.datos_objDet["x"]>g.cotas_centrar[1]):
                g.datos_objDet["centrado"] = 0
                g.datos_objDet["lado"] = "d"
        if(g.rob.readDetectedObject().label == g.datos_objDet["objeto"]):
            if (g.datos_objDet["x"]<g.cotas_centrar[0]):
                g.datos_objDet["centrado"] = 0
                g.datos_objDet["lado"] = "r"
            
        #if(g.rob.readDetectedObject().label == g.datos_objDet["objeto"]):
        #   g.datos_objDet["x"] = g.rob.readDetectedObject().x
        
        if (g.datos_objDet["lado"] == "r"):    
            g.rob.moveWheelsByTime(0,2,1)
            print("rotar der") 
            print(g.rob.readDetectedObject().label == g.datos_objDet["ojeto"])
            print("lado: "+str(g.datos_objDet["lado"])+"  X:"+ str(g.datos_objDet["x"])) 
        if (g.datos_objDet["lado"] == "d"):
            print("rotar iz") 
            print(g.rob.readDetectedObject().label == g.datos_objDet["ojeto"])
            print("lado: "+str(g.datos_objDet["lado"])+"  X:"+ str(g.datos_objDet["x"])) 
            g.rob.moveWheelsByTime(2,0,1)
        #----------------
        #g.rob.moveWheelsByTime(2,2,1)
        g.rob.stopMotors()
        g.rob.wait(0.1)
        
        if(g.rob.readDetectedObject().label == g.datos_objDet["ojeto"]):
            g.datos_objDet["x"] = g.rob.readDetectedObject().x
            print(str(g.datos_objDet["x"])+"X:"+ str(g.datos_objDet["x"])) 
        if (g.datos_objDet["x"]<g.cotas_centrar[1]):
            if (g.rob.readIRSensor(IR.FrontC)>100):
                g.datos_objDet["agarrado"] = 1
                break
            if (g.datos_objDet["x"]>g.cotas_centrar[0]):
                g.datos_objDet["centrado"] = 1
                g.datos_objDet["lado"] = "0"
                print("centrado en x: "+str(g.datos_objDet["x"]))
                break
            
def agarrar():
    print("agarrar")
    g.datos_objDet["agarrado"] = 0
    while(g.datos_objDet["agarrado"] == 0):
        print("Ir front: "+ str(g.rob.readIRSensor(IR.FrontC)))
        if (g.rob.readIRSensor(IR.FrontC)>350):
                    g.datos_objDet["agarrado"] = 1
                    print("agarrado")
                    break
        g.rob.moveWheelsByTime(10,10,1)
        g.rob.stopMotors() 
        
def buscar_tacho():
    g.rob.moveTiltTo(90,100)
    print("buscando tacho")
    while (g.datos_objDet["target_tacho_detectado"] == 0):
        g.datos_objDet["tacho_detectado"] = g.rob.readQR().id
        print("buscando tacho, tacho detectado: "+ str( g.datos_objDet["tacho_detectado"]))
        if (g.datos_objDet["tacho_detectado"] == g.datos_objDet["target_tacho"]):
            print("target tacho detectado :" +str( g.datos_objDet["tacho_detectado"] ))
            print("tacho qr.x :" +str(g.rob.readQR().x))
            g.datos_objDet["target_tacho_detectado"] = 1
            break
        g.rob.moveWheelsByTime(2,-2,1)
        g.rob.stopMotors()
       
def centrar_qr():
    print("centrar_qr")
    g.datos_objDet["qr_centrado"] = 0
    while(g.datos_objDet["qr_centrado"] == 0):
        if(g.rob.readQR().id == g.datos_objDet["target_tacho"]):
            g.datos_objDet["qr_x"] = g.rob.readQR().x
            print("qr_X: "+ str(g.datos_objDet["qr_x"])) 
        #rob.wait(1)
        if (g.datos_objDet["qr_x"]>g.cotas_centrar_qr[1]):
            g.datos_objDet["qr_centrado"] = 0
            g.datos_objDet["qr_lado"] = "d"
        if (g.datos_objDet["qr_x"]<g.cotas_centrar_qr[0]):
            g.datos_objDet["qr_centrado"] = 0
            g.datos_objDet["qr_lado"] = "r"
        g.datos_objDet["qr_x"] = g.rob.readQR().x
        if (g.datos_objDet["qr_lado"] == "r"):    
            g.rob.moveWheelsByTime(0,2,1)
            print("rotar der") 
            print("qr_lado: "+str(g.datos_objDet["qr_lado"])+"  qr_X:"+ str(g.datos_objDet["qr_x"])) 
        if (g.datos_objDet["qr_lado"] == "d"):
            print("rotar iz") 
            print("lado: "+str(g.datos_objDet["qr_lado"])+" qr_X:"+ str(g.datos_objDet["qr_x"])) 
            g.rob.moveWheelsByTime(2,0,1)
        g.rob.stopMotors()
        #rob.wait(0.1)        
        if(g.rob.readQR().id == g.datos_objDet["target_tacho"]):
            g.datos_objDet["qr_x"] = g.rob.readQR().x
            print("X:"+ str(g.datos_objDet["qr_x"])) 
        if (g.datos_objDet["qr_x"]<g.cotas_centrar_qr[1]):
            if (g.datos_objDet["qr_x"]>g.cotas_centrar_qr[0]):
                g.datos_objDet["qr_centrado"] = 1
                g.datos_objDet["qr_lado"] = "0"
                print("qr centrado en x: "+str(g.datos_objDet["qr_x"]))
                break
        g.datos_objDet["qr_dist"]  = g.rob.readQR().distance
        print("dist: " + str(g.datos_objDet["qr_dist"]))
        if (g.datos_objDet["qr_dist"]>650):
            g.datos_objDet["qr_centrado"] = 1
            g.datos_objDet["reciclado"] = 1
            print("reciclado")    
            break
    
def reciclar():
    print("reciclar")
    g.datos_objDet["reciclado"] = 0
    while(g.datos_objDet["reciclado"] == 0):
        g.datos_objDet["qr_dist"]  = g.rob.readQR().distance
        print("QR_dis: "+ str(g.datos_objDet["qr_dist"]))
        if (g.datos_objDet["qr_dist"]>700):
                    g.datos_objDet["reciclado"] = 1
                    print("reciclado")
                    g.obj_reciclados.append(str(g.datos_objDet["objeto"]))
                    print("obj_reciclados :")
                    print(g.obj_reciclados)
                    break
        g.rob.moveWheelsByTime(10,10,1)
        g.rob.stopMotors() 
        
def qr_dist():
    dist = g.rob.readQR().distance
    print("dist: " + str(dist))
    return dist

def reset():
    g.rob.moveWheelsByTime(-25,-25,2)
    g.rob.moveWheelsByTime(5, -12,3)
    g.rob.stopMotors()
    for x in g.datos_objDet:
        g.datos_objDet[x] = 0
    print("reset")  

def iniciar():
    print("Iniciar")