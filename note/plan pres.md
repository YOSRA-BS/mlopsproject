plan pres



## ML LIFECYCLE :



## MLOPS

 

## Integration pipeline :





*  modele training ( hne bsh tahki ala features , parameters hyper parameters (o referes toi bl exp eli amaltou ))

 	|

 	|

* modele registry ( ahki ala mlflow en général mlflow.sklearn.log\_model )

 	|

 	|

* suitable form for integration :

 	1.charger le modele depuis registry ( sklearn.load\_model (L’output est un objet MLflow sklearncModel → utilisable directement pour prédictions sans ré-entrainer )



 	2.Passer à une forme intégrable (***ML Service***) : exporter ton modèle en format standard (ONNX, TensorFlow, etc. Puis le dockeriser et le déployer sur Minikube/Kubernetes comme ***microservice***.



 



 

