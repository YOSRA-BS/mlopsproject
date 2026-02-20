les files a ajouter dans le projet actuel MLOPS STARTER : 



exception.py 

avoir des logs qui track les erreurs clairement  et précisemment est très utile en MLOps / production pour comprendre rapidement où ça plante.



* error\_detail.exc\_info() → récupère les infos de l’exception en cours (type, valeur, traceback).



* exc\_tb → c’est l’objet traceback qui contient où l’erreur s’est produite.



* exc\_tb.tb\_frame.f\_code.co\_filename → donne le nom du fichier où l’erreur est apparue.



* exc\_tb.tb\_lineno → donne le numéro de ligne de l’erreur.



et puis on formate le message detaillé de l'erreur 

La classe CustomException

Hérite de la classe Exception → donc c’est une exception personnalisée.



Dans le constructeur (\_\_init\_\_), elle appelle error\_message\_detail pour générer un message enrichi (fichier + ligne + texte).



\_\_str\_\_ → quand on affiche l’exception (print(e)), ça renvoie directement le message formaté.



logger.py 

utilisé pour enregistrer des événements (infos, erreurs, avertissements) dans un fichier, afin de suivre ce qui se passe dans ton application.



logger.py configure le système de logging :



Il crée un fichier de logs (avec un nom basé sur la date/heure).



Il définit le format des messages (date, ligne, niveau, message).



Il enregistre tout ce qui est loggé (logging.info, logging.error, etc.) dans ce fichier.

Quand tu combines les deux logger.py et exception.py:



Si une erreur survient, tu lèves une CustomException.



Cette exception génère un message détaillé.



Tu peux ensuite utiliser logging.error(str(e)) pour enregistrer ce message dans ton fichier de logs.



logging : module standard Python pour gérer les logs.



os : pour manipuler les chemins de fichiers et dossiers.



datetime : pour générer un nom de fichier basé sur la date et l’heure.



LOG\_FILE=f"{datetime.now().strftime('%m\_%d\_%Y\_%H\_%M\_%S')}.log"

Crée un nom de fichier de log basé sur la date/heure actuelle.

strftime est une méthode de datetime qui formate une date/heure en texte selon un modèle.

Exemple : 02\_20\_2026\_10\_58\_30.log.

👉 Chaque exécution aura son propre fichier de logs.



logs\_path=os.path.join(os.getcwd(),"logs",LOG\_FILE)

os.makedirs(logs\_path,exist\_ok=True)

os.getcwd() → récupère le répertoire courant.

os.path.join(..., "logs", LOG\_FILE) → construit un chemin du type :

/mon\_projet/logs/02\_20\_2026\_10\_58\_30.log

os.makedirs(..., exist\_ok=True) → crée le dossier logs si nécessaire.

((((((((((((((((((((((( il ya une incohérence ds le code la version correcte doit normalement etre :logs\_path=os.path.join(os.getcwd(),"logs")

os.makedirs(logs\_path,exist\_ok=True)

LOG\_FILE\_PATH=os.path.join(logs\_path,LOG\_FILE)

))))))))))))))))))))))) 



logging.basicConfig(

&nbsp;   filename=LOG\_FILE\_PATH,

&nbsp;   format="\[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

&nbsp;   level=logging.INFO,

)

logging.basicConfig( ) 

Ici, tu dis au module logging : écris tous les logs dans ce fichier.



Important : à ce moment-là, le fichier n’existe pas encore physiquement.



C’est logging qui va créer le fichier automatiquement dès qu’un premier message est écrit (logging.info, logging.error, etc.).



👉 Donc tu n’as pas “créé” le fichier toi-même, tu as juste préparé son chemin et dit à logging où écrire.

Configure le logger :



filename=LOG\_FILE\_PATH → les logs seront écrits dans ce fichier.



format=... → définit le format des messages :



%(asctime)s → date/heure du log.



%(lineno)d → numéro de ligne où le log est généré.



%(name)s → nom du logger.



%(levelname)s → niveau du log (INFO, ERROR, WARNING…).



%(message)s → le message du log.



level=logging.INFO → on enregistre tous les logs de niveau INFO et plus (INFO, WARNING, ERROR, CRITICAL).

