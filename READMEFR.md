## PowDevLif(Power Device Remaining Useful Life)

Projet Open Source pour l'analyse thermique et la modélisation de composants électroniques de puissance.
Ce projet vise à fournir une plateforme logicielle pour effectuer des calculs de pertes de puissance, estimer les températures des composants électroniques et prévoir leur durée de vie opérationnelle.
Il comprend des fonctionnalités pour la récupération de données à partir de fichiers Excel, le traitement de signaux, le calcul de pertes de puissance, la modélisation thermique et l'analyse de dommages cumulatifs.
Le projet utilise des bibliothèques populaires telles que NumPy, Pandas, SciPy, Matplotlib et Rainflow pour la manipulation des données, le calcul scientifique et la visualisation des résultats.

Ce projet est ouvert à la contribution de la communauté Open Source. N'hésitez pas à explorer le code source, soumettre des problèmes, proposer des améliorations et contribuer au développement du projet.

## Table des Matières
- [Installation](#Installation)
- [Utilisation](#Utilisation)
- [Contribution](#Contribution)
- [Licence](#Licence)

## Installation
Ce projet se présente sous la forme d'une bibliothèque à installer dans votre environnement Python.
Pour installer la bibliothèque, il vous suffit d'utiliser la commande `pip install PowDevLif`.
Assurez-vous d'avoir la dernière version de pip afin que les dernières dépendances de la bibliothèque puissent être installées.
Les dépendances du projet sont les suivantes :

    - scipy==1.10.1
    - pandas==2.0.1
    - matplotlib==3.7.1
    - numpy==1.24.1
    - rainflow==3.2.0
    - openpyxl==3.1.2

Il est également possible d'utiliser le projet sans avoir à installer la bibliothèque. Je vous invite à consulter [OLDREADMEFR.md](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/OLDREADMEFR.md) si cela vous intéresse.

## Utilisation
Pour utiliser la bibliothèque, vous avez besoin de deux fichiers :
    - Un dictionnaire contenant toutes les variables de la simulation
    - Le fichier Excel avec les données d'entrée de la simulation
Vous devez respecter le format, le nom des variables et la structure interne des fichiers pour que votre projet fonctionne sans problème.

Un exemple de chaque fichier est disponible ici : [Example Fichier](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/tree/main/example)

Pour utiliser la bibliothèque une fois installée, il vous suffit de l'importer dans votre projet avec la ligne suivante :

`import PowDevLif.lifetime`

Une fois ce module chargé, vous pouvez utiliser la fonction rul_calculation en lui fournissant le chemin vers votre dictionnaire de variables, par exemple ("C:/Votre/chemin/vers/variables.py"). Dans votre code, l'appel de fonction doit ressembler à ceci :

`résultats = rul_calculation("C:/Votre/chemin/vers/variables.py")`

Vous pouvez aussi afficher différents graphiques avec l'appel de fonction suivant:

`rul_graphs("C:/Votre/chemin/vers/variables.py")`

## Exemple
Un exemple du code en fonctionnement est détaillé dans le fichier [DetailedExampleFR.md](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/DetailedExampleFR.md)

## Contribution
Nous accueillons toutes sortes de contributions ! Pour contribuer au projet, commencez par forker le dépôt, faites vos modifications proposées dans une nouvelle branche et créez une pull request. Assurez-vous que votre code est lisible et bien documenté. Incluez des tests unitaires si possible.

Vous pouvez également contribuer en soumettant des rapports de bugs, des demandes de fonctionnalités et en suivant les problèmes.

## Licence
Ce projet est licencié sous les termes de la licence MIT. En contribuant au projet, vous acceptez que vos contributions soient licenciées sous sa licence MIT.

## Auteurs

- Baudais Briac : briac.baudais@ens-rennes.fr (Créateur de la méthode de calcul)
- Garnier Paul : paul.garnier@ens-rennes.fr (Développeur de la bibliothèque Python)
