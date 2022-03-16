import cv2 
  
webcam = cv2.VideoCapture(0) 
  # Introducir por parametro el numero de cámara que estas tratando.
  # Asi podemos llamar a las diferentes camaras
  
while(True): 
    grabar, ventana = webcam.read() 

    to_imagen_gris = cv2.cvtColor(ventana, cv2.COLOR_RGB2GRAY)
    to_imagen_sepia = cv2.cvtColor(ventana, cv2.COLOR_BGR2RGB)
    to_imagen_arcoiris = cv2.cvtColor(ventana, cv2.COLOR_BGR2XYZ)

    mostrar_imagen= cv2.imshow('GRIS -> Controles: q=quit', to_imagen_gris)
    mostrar_imagen2= cv2.imshow('FILTRO 1 -> Controles: q=quit', to_imagen_sepia) 
    mostrar_imagen3= cv2.imshow('FILTRO 2 -> Controles: q=quit', to_imagen_arcoiris)

     # (Nombre de ventana, ventana_que_salta)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
webcam.release() 
cv2.destroyAllWindows()