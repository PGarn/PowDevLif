## Calcul_DuréeDeVie_IGBT

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
Ce projet nécessite des versions spécifiques de bibliothèques. Pour configurer votre environnement, vous devez installer les dépendances suivantes :

  Python : Le projet est écrit en Python. Assurez-vous d'avoir installé Python 3.6 ou une version ultérieure.

  Bibliothèques : Installez les bibliothèques Python suivantes avec les versions spécifiées :
  - scipy==1.10.1
  - pandas==2.0.1
  - matplotlib==3.7.1
  - numpy==1.24.1
  - rainflow==3.2.0
  - openpyxl==3.1.2

Vous pouvez installer ces packages en utilisant pip, qui est un gestionnaire de packages pour Python. Si vous utilisez une interface en ligne de commande, tapez les commandes suivantes :

  - pip install scipy==1.10.1
  - pip install pandas==2.0.1
  - pip install matplotlib==3.7.1
  - pip install numpy==1.24.1
  - pip install rainflow==3.2.0
  - pip install openpyxl==3.1.2

Pour installer le projet, téléchargez tous les fichiers et conservez la même organisation des fichiers.

## Utilisation
Pour utiliser vos propres données, remplacez simplement les fichiers dans le répertoire "exemples". Le fichier "variables.py" contient un dictionnaire où vous pouvez stocker toutes les données nécessaires. Pour le fichier Excel, les informations requises se trouvent à la fin du fichier "variables.py".

/!\ Assurez-vous de fournir le chemin correct vers le fichier Excel pour garantir une récupération correcte des données (ligne 52 dans "variables.py").

Pour exécuter le programme, exécutez le fichier "lifetime.py". Une fois que tout est lancé avec succès, appelez la fonction "rul_calculation()". Elle renverra les valeurs suivantes dans l'ordre : "lifetime_IGBT", "lifetime_diode", "number_of_km_IGBT", "e_kwh_byhours", et "efficiency".

Si vous voulez afficher les graphiques pour le couple, la vitesse, le courant et les pertes totales, vous pouvez décommenter la ligne 38 du fichier "lifetime.py". Cela permettra au code de tracer et d'afficher les graphiques.

Pour intégrer ce programme dans votre propre script, vous devez importer le fichier lifetime.py. Suite à cela, la fonction rul_calculation peut être invoquée. Voici un exemple qui démontre cela :

- import lifetime
- lifetime_IGBT, lifetime_diode = lifetime.rul_calculation()

Vous pouvez retourner plus de données comme : "number_of_km_IGBT", "e_kwh_byhours", et "efficiency" en modifiant la ligne 44 dans "lifetime.py".

## Exemple
Un exemple du code en fonctionnement est détaillé dans le fichier [DetailedExampleFR.md](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/DetailedExampleFR.md)

## Contribution
Nous accueillons toutes sortes de contributions ! Pour contribuer au projet, commencez par forker le dépôt, faites vos modifications proposées dans une nouvelle branche et créez une pull request. Assurez-vous que votre code est lisible et bien documenté. Incluez des tests unitaires si possible.

Vous pouvez également contribuer en soumettant des rapports de bugs, des demandes de fonctionnalités et en suivant les problèmes.

## Licence
Ce projet est licencié sous les termes de la licence MIT. En contribuant au projet, vous acceptez que vos contributions soient licenciées sous sa licence MIT.
