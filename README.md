# DetecteurObjetsOrbitaux
Code du projet de TP de 3ème année consistant à détecter des objets en orbite basse à l'aide de caméras optiques

## Code à éxécuter sur le raspberry pi pour prendre des images automatiquement :

Pour procéder à la prise de photos automatiquement, il faut réaliser les étapes suivantes (cela est sous réserve d'avoir inclu la ligne ```python3 /home/pi/take.py``` dans le fichier ```/etc/rc.local```

-Allumer la caméra au préalable
-Allumer le raspberry pi en connectant la battrie à son port de charge
-Presser pendant 3 secondes sur l'interrupteur du module GPS pour l'activer
-Attendre environ 30 secondes et les images commenceront à être prises automatiquement, et stockées dans l'adresse mentionnée dans le code, cela peut être soit ```/home/pi/PHOTO_FULLPROCESS``` ou ```/etc/media/DISQUE/PHOTO_FULLPROCESS```. Un nouveau set sera crée à chaque fois que le raspberry pi est brancé, avec chaque set contenant un fichier param.txt contenant l'orientation et paramètres intrinsèques à la caméra, et un fichier stations.in contenant la position GPS du prototype.

Pour procéder à la prise de photos manuelle, il faut :

-Se connecter au préalable avec un réseau wifi mobile (partage de connexion), pour que le raspberry pi se souvienne de se réseau.
-Une fois sur place, allumer le partage de connexion, et se connecter avec un PC à se même réseau
-Allumer la caméra
-Allumer le raspberry pi en connectant la battrie à son port de charge
-Presser pendant 3 secondes sur l'interrupteur du module GPS pour l'activer
-En utilisant VNC viewer, se connecter à l'adresse IP du raspberry pi préalablement enregistrée
-Lancer le code ```/home/pi/take.py```
-Attendre environ 30 secondes et les images commenceront à être prises automatiquement, et stockées dans l'adresse mentionnée dans le code, cela peut être soit ```/home/pi/PHOTO_FULLPROCESS``` ou ```/etc/media/DISQUE/PHOTO_FULLPROCESS```. Un nouveau set sera crée à chaque fois que le raspberry pi est brancé, avec chaque set contenant un fichier param.txt contenant l'orientation et paramètres intrinsèques à la caméra, et un fichier stations.in contenant la position GPS du prototype.
-Le programme peut être arrêté à tout moment en faisant ```CTRL+C```, et le programme peut être relancé avec la même commande
