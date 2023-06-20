# Documentation des fonctions

## Fonction principale : `rul_calculation`

Cette fonction exécute une séquence de calculs liés aux propriétés thermiques et électriques de certains matériaux, basée sur des données d'un fichier Excel.

- **Entrée :**
  - `chemin du dictionnaire` - Chemin d'accès au fichier de dictionnaire.
    - EXEMPLE : "example/variables.py"
- **Sortie :**
  - `lifetime_IGBT` - Durée de vie calculée pour l'IGBT.
  - `lifetime_diode` - Durée de vie calculée pour la diode.
  - `efficiency` - Efficacité calculée.
    - EXEMPLE : (17790.673569426686, 14182.53219897886, 0.9156558987278411)

## Sous-classes

### Classe `Losses`

Cette classe initialise une instance de la classe Losses.

- **Entrée :**
  - `dic` (dict) : Dictionnaire de constantes et de paramètres de fichier.
  - `file` (pandas DataFrame) : Représentation du fichier Excel sous forme de pandas DataFrame.
    - EXEMPLE : ![Current](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/Figures/Current.png)

- **Sortie :**
  - Objet `Losses`
    - EXEMPLE : ![Total Losses](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/Figures/Losses.png)

### Classe `ZthMaterials`

Cette classe représente l'impédance thermique des matériaux pour l'IGBT et la diode. Elle utilise le modèle de Foster.

- **Entrée :**
  - `dic` (dict) : Dictionnaire de constantes et de paramètres de fichier.
- **Sortie :**
  - Objet `ZthMaterials`

## Sous-fonctions

### `losses.calculate_losses`

Cette fonction calcule les pertes pour l'IGBT et la diode. Les pertes de l'IGBT sont divisées en pertes de conduction (P_T_cond) et en pertes de commutation (P_T_sw). Les pertes de la diode sont divisées en pertes de conduction (P_D_cond) et en pertes de commutation (P_D_sw). Les pertes totales et leur somme cumulative sont également calculées et stockées.

- **Entrée :** Aucune
- **Sortie :** Aucune

### `calculate_temperature`

Cette fonction calcule la température de l'IGBT et de la diode.

- **Entrée :**
  - `losses` (objet) : Objet contenant les données de perte.
  - `dic` (dict) : Dictionnaire de constantes et de paramètres de fichier.
  - `file` (DataFrame) : Représentation du fichier Excel sous forme de pandas DataFrame.
- **Sortie :**
  - `Temp_IGBT`, `Temp_diode` (tableau) : Températures calculées de l'IGBT et de la diode, respectivement.
    - EXEMPLE : ![Temp vs Time](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/Figures/Temperatures.png)

  #### Sous-fonctions

  ##### `zth_obj.calculate_zth_cf`

  Cette fonction calcule l'impédance thermique boîtier-fluide.

  - **Entrée :** Aucune
  - **Sortie :** Aucune

  ##### `zth_obj.calculate_zth_foster`

  Cette fonction calcule l'impédance thermique en utilisant le modèle de Foster.

  - **Entrée :** Aucune
  - **Sortie :** Aucune

### `count`

Cette fonction calcule les cycles et `counter_Nf` en fonction de la température donnée (Temp) et du dictionnaire (dic) de constantes.

- **Entrée :**
  - `Temp` (tableau numpy) : Tableau de valeurs de température.
  - `dic` (dict) : Dictionnaire de constantes requis pour les calculs.
- **Sortie :**
  - `counter` (tableau numpy) : Cycles calculés pour la température donnée (Temp).
  - `counter_Nf` (tableau numpy) : Valeurs de `counter_Nf` calculées pour la température donnée (Temp).

### `graph`

Cette fonction génère et affiche des graphiques en fonction des données fournies.

- **Entrée :**
  - `losses` (objet) : Objet contenant les données de perte.
  - `dic` (dict) : Dictionnaire de constantes et de paramètres de fichier.
  - `file` (DataFrame) : Représentation du fichier Excel sous forme de pandas DataFrame.
  - `Temp_IGBT`, `Temp_diode`, `Temp_case` (tableau) : Températures calculées de l'IGBT, de la diode et du boîtier, respectivement.
- **Sortie :** Aucune

### `calculate_damage_cumulation`

Cette fonction calcule une série de quantités liées aux dommages en fonction des entrées fournies.

- **Entrée :**
  - `losses` (objet) : Objet contenant les données de perte.
  - `dic` (dict) : Dictionnaire de constantes et de paramètres de fichier.
  - `file` (DataFrame) : Représentation du fichier Excel sous forme de pandas DataFrame.
  - `counter_IGBT` (tableau numpy) : Tableau de valeurs de `counter` pour l'IGBT.
  - `counter_Nf_IGBT` (tableau numpy) : Tableau de valeurs de `counter_Nf` pour l'IGBT.
  - `counter_diode` (tableau numpy) : Tableau de valeurs de `counter` pour la diode.
  - `counter_Nf_diode` (tableau numpy) : Tableau de valeurs de `counter_Nf` pour la diode.
- **Sortie :**
  - `Lifetime_IGBT` (float) : Durée de vie calculée pour l'IGBT.
  - `Lifetime_diode` (float) : Durée de vie calculée pour la diode.
  - `number_of_km_IGBT` (float) : Kilomètres calculés pour l'IGBT.
  - `E_kwh` (float) : Énergie calculée en kWh.
  - `E_kwh_byhours` (float) : Énergie calculée par heure en kWh.
  - `rendemment` (float) : Efficacité
