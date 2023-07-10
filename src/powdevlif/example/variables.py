variables = {
    # General parameters
    "time_cycle": 1800,                     # Cycle duration in seconds
    "Ta": 50,                               # Ambient temperature in degrees Celsius
    "Vdc": 450,                             # DC voltage in volts
    "f_sw": 10000,                          # Switching frequency in Hz

    "number_IGBT": 6,                       # Total number of IGBTs
    "number_IGBT_parallel": 1,              # Number of IGBTs in parallel (number_IGBT/6)

    # IGBT parameters (single die)
    "Vce0": 1.10,                           # Collector-emitter saturation voltage in volts
    "Rce": 0.75e-3,                         # Collector-emitter saturation resistance in ohms
    "Eon_sw": 13.5e-3,                      # Turn-on activation energy in joules
    "Eoff_sw": 23.5e-3,                     # Turn-off activation energy in joules
    "E_sw": 13.5e-3 + 23.5e-3,              # Total activation energy in joules
    "Vref_sw": 400,                         # Reference voltage of the IGBT control circuit in volts
    "Iref_sw": 450,                         # Reference current of the IGBT control circuit in amperes
    "kv_igbt": 1.35,                        # Variation coefficient of the IGBT activation voltage

    # Diode parameters (single die)
    "Vd": 1.45,                             # Diode forward voltage in volts
    "Rd": 0.75e-3,                          # Diode resistance in ohms
    "E_d": 7e-3,                            # Diode activation energy in joules
    "Vref_d": 400,                          # Reference voltage of the diode control circuit in volts
    "Iref_d": 450,                          # Reference current of the diode control circuit in amperes
    "ki_diode": 0.6,                        # Variation coefficient of the diode leakage current
    "kv_diode": 0.6,                        # Variation coefficient of the diode activation voltage
  
    # Global thermal parameters  (single die)
    "Rth_ch": 0.05 / 6,                     # Convective cooling thermal resistance of the assembly in degrees Celsius per watt
    "Cth_ch": 0,                            # Convective cooling thermal capacitance of the assembly in joules per degree Celsius
    "Rth_hf": 0.06 / 6,                     # Heat conduction cooling thermal resistance in degrees Celsius per watt
    "Cth_hf": 0,                            # Heat conduction cooling thermal capacitance in joules per degree Celsius
  
    # IGBT thermal parameters  (single die)
    "layers_Rth_jc_IGBT": [0.005, 0.055, 0.022, 0.013],     # Junction-to-case thermal resistance of the IGBT in degrees Celsius per watt for each layer
    "layers_Cth_jc_IGBT": [0.001 / 0.005, 0.03 / 0.055, 0.25 / 0.022, 1.5 / 0.013],  # Junction-to-case thermal capacitance of the IGBT in joules per degree Celsius for each layer

    # Diode thermal parameters (single die)
    "layers_Rth_jc_diode": [0.015, 0.1, 0.025, 0.01],        # Junction-to-case thermal resistance of the diode in degrees Celsius per watt for each layer
    "layers_Cth_jc_diode": [0.001 / 0.015, 0.03 / 0.1, 0.25 / 0.025, 1.5 / 0.01],     # Junction-to-case thermal capacitance of the diode in joules per degree Celsius for each layer

    # Damage accumulation calculation parameters
    "A": 3.5535e15,                         # Pre-exponential factor in the Arrhenius equation
    "alpha": -7.0390,                       # Exponent in the Arrhenius equation
    "Ea": 2.7172e-20,                       # Activation energy in the Arrhenius equation
    "k": 1.38e-23,                          # Boltzmann constant
  
    # Excel parameters
    "excel_file_path": 'src/powdevlif/example/WLTP.xlsx',     # Path to the Excel file containing the input data
    "excel_page": 'Feuil1',                 # Name of the Excel sheet containing the input data
    "excel_starting_row": 2,                # Number of the first row containing the input data
    "excel_ending_row": 1802,               # Number of the last row containing the input data
    "excel_column_time": 1,                 # Number of the column containing the time values
    "excel_column_power": 6,               # Number of the column containing the power values
    "excel_column_current": 4,             # Number of the column containing the current values
    "excel_column_cosphi": 5,              # Number of the column containing the cosinus phi values
    "excel_column_m": 7,                   # Number of the column containing the m values
}
