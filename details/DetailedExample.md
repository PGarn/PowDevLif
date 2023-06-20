# Function Documentation

## Main function: `rul_calculation`

This function executes a sequence of calculations related to thermal and electrical properties of some materials, based on data from an Excel file.

- **Input:**
  - `dictionary path` - The path to the dictionary file.
    - EXAMPLE: "example/variables.py"
- **Output:**
  - `lifetime_IGBT` - The calculated lifetime for the IGBT.
  - `lifetime_diode` - The calculated lifetime for the diode.
  - `efficiency` - The calculated efficiency.
    - EXAMPLE: (17790.673569426686, 14182.53219897886, 0.9156558987278411)

## Subclasses

### `Losses` class

This class initializes an instance of the Losses class.

- **Input:**
  - `dic` (dict): Dictionary of constants and file parameters.
  - `file` (pandas DataFrame): A pandas DataFrame representation of the Excel file.
    - EXAMPLE: ![Current](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/Figures/Current.png)

- **Output:**
  - `Losses` object
    - EXAMPLE: ![Total Losses](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/Figures/Losses.png)

### `ZthMaterials` class

This class represents the thermal impedance of materials for IGBT and diode. It uses Foster's model.

- **Input:**
  - `dic` (dict): Dictionary of constants and file parameters.
- **Output:**
  - `ZthMaterials` object

## Subfunctions

### `losses.calculate_losses`

This function calculates losses for both IGBT and Diode. IGBT losses are divided into conduction losses (P_T_cond) and switching losses (P_T_sw). Diode losses are divided into conduction losses (P_D_cond) and switching losses (P_D_sw). The total losses and their cumulative sum are also calculated and stored.

- **Input:** None
- **Output:** None

### `calculate_temperature`

This function calculates the temperature of IGBT and Diode.

- **Input:**
  - `losses` (object): Object containing the loss data.
  - `dic` (dict): Dictionary of constants and file parameters.
  - `file` (DataFrame): A pandas DataFrame representation of the Excel file.
- **Output:**
  - `Temp_IGBT`, `Temp_diode` (array): Calculated temperatures of IGBT and Diode, respectively.
    - EXAMPLE: ![Temp vs Time](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/details/Figures/Temperatures.png)

  #### Subfunctions

  ##### `zth_obj.calculate_zth_cf`

  This function calculates the case-to-fluid thermal impedance.

  - **Input:** None
  - **Output:** None

  ##### `zth_obj.calculate_zth_foster`

  This function calculates the thermal impedance using the Foster model.

  - **Input:** None
  - **Output:** None

### `count`

This function calculates the cycles and `counter_Nf` based on the given temperature (Temp) and dictionary (dic) of constants.

- **Input:**
  - `Temp` (numpy array): Array of temperature values.
  - `dic` (dict): Dictionary of constants required for calculations.
- **Output:**
  - `counter` (numpy array): Calculated cycles for the given Temp.
  - `counter_Nf` (numpy array): Calculated counter_Nf values for the given Temp.

### `graph`

This function generates and displays graphs based on the given data.

- **Input:**
  - `losses` (object): Object containing the loss data.
  - `dic` (dict): Dictionary of constants and file parameters.
  - `file` (DataFrame): A pandas DataFrame representation of the Excel file.
  - `Temp_IGBT`, `Temp_diode`, `Temp_case` (array): Calculated temperatures of IGBT, Diode, and Case, respectively.
- **Output:** None

### `calculate_damage_cumulation`

This function calculates a series of damage-related quantities based on the given inputs.

- **Input:**
  - `losses` (object): Object containing the loss data.
  - `dic` (dict): Dictionary of constants and file parameters.
  - `file` (DataFrame): A pandas DataFrame representation of the Excel file.
  - `counter_IGBT` (numpy array): Array of counter values for the IGBT.
  - `counter_Nf_IGBT` (numpy array): Array of counter_Nf values for the IGBT.
  - `counter_diode` (numpy array): Array of counter values for the diode.
  - `counter_Nf_diode` (numpy array): Array of counter_Nf values for the diode.
- **Output:**
  - `Lifetime_IGBT` (float): Calculated lifetime for the IGBT.
  - `Lifetime_diode` (float): Calculated lifetime for the diode.
  - `number_of_km_IGBT` (float): Calculated kilometers for IGBT.
  - `E_kwh` (float): Calculated energy in kWh.
  - `E_kwh_byhours` (float): Calculated energy per hour in kWh.
  - `rendemment` (float): Calculated efficiency.
