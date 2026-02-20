PRATIQUEMENT (MLOPS STARTER )

1-awel etape : bien sur en travaillant dans une equipe plusieurs personnes vont collaborer , bsh ycommitiw l code ymirgiw ydevloppiw new models  etc thats why awel etape bsh tkoun hiya e setup mta l GitHub eli bsh ykoun repo mte3na for commiting our code o bsh ykhali e development ykoun syncro entre les memebres mta e team



2- setup.py : responsable de tranformer le projet en package installabale par un simple pip



when find\_packages is runnig dans ligne package= find\_packages() it will go an d see how many floder have \_\_init.py\_\_ o yconsiderihom houma as packages itselves and try to build them after th build we can import them as packages



en runnant pip install .

Python va :



Lire ton setup.py.



Installer toutes les dépendances listées dans requirements.txt.



Enregistrer ton projet (mlproject) comme package Python dans ton environnement.



cela rend facile a intégrer  un pipeline MLflow, ou un job Kubernetes, il suffit d’installer ton package

*  Sans package

Tu peux lancer ton pipeline MLflow en pointant directement vers tes scripts (train.py, pipeline.py, etc.).



Tu peux construire une image Docker avec COPY . /app et exécuter ton code.



Tu peux déployer sur Kubernetes en montant ton code source dans le conteneur.



👉 Ça marche, mais c’est un peu “bricolage” : tu dois gérer les chemins, copier les fichiers, et maintenir la cohérence manuellement.



* Avec package

Tu fais pip install . ou pip install -e . dans ton conteneur ou ton environnement.



Ton projet devient une librairie Python (import mlproject) utilisable partout.



MLflow peut exécuter ton code en important directement ton package.



Dans Docker/Kubernetes, tu n’as qu’à installer ton package (comme numpy ou scikit-learn) et tout est prêt.





👉 Ça rend ton projet portable, réutilisable et maintenable. Tu n’as plus besoin de copier-coller des scripts ou de gérer des chemins compliqués.





find\_packages() dans setup.py

Elle parcourt ton répertoire de projet (par défaut le dossier courant).



Elle repère tous les sous-dossiers qui contiennent un fichier \_\_init\_\_.py.

👉 La présence de \_\_init\_\_.py indique que le dossier est un package Python. ( building the package )



Elle construit une liste de ces packages et sous-packages pour les inclure dans ton installation.

