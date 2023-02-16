from robobopy.Robobo import Robobo
rob = Robobo("192.168.0.42")
#rob = Robobo("localhost")
rob.connect()

__all__ = ['rob', 'tachos', 'datos_objDet','obj_reciclados','cotas_centrar','cotas_centrar_qr','qr_centrado','condition','til','pan','comand']
tachos = {"papeles":["cup","book","vase"],"material organico":["banana","apple", "orange"],"plasticos":["bottle","yoghurt"]}
datos_objDet = {"detectado":0,"ojeto":0,"target_tacho":"","x":0,"centrado":0,"lado":0,"agarrado":0,"obj_ya_reciclado": 0, "tacho_detectado":0,"target_tacho_detectado":0,"qr_centrado":0,"qr_x":0,"qr_lado":0,"reciclado":0,"qr_dist":0}
obj_reciclados = []
cotas_centrar = [242,252]
cotas_centrar_qr = [242,261]
qr_centrado = {}
condition = 1
til = 100
pan = 0
comand = ''


automata = {'buscar_obj':['buscar'],'agarrar_ob':['centrar','agarrar'],'buscar_tacho':['buscar_tacho'],'reciclar_obj':['centrar_qr','reciclar']}
#automata = {'comportamiento_anterior':'','comportamiento_actual':'',}

objetos_totales = 3
