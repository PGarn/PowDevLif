# Title: "Development of a library Tool for Analysis of IGBT and Diode Components"
# Tags:
  - power electronics
  - IGBT
  - diode
  - library tool
  - lifetime
# Authors:
  - [Garnier Paul](https://gitlab.com/PGarn)
    affiliation: SATIE, UMR CNRS 8029, École Normale Supérieure de Rennes, 35170 Bruz, France
  - [Baudais Briac]()
    affiliation: SATIE, UMR CNRS 8029, École Normale Supérieure de Rennes, 35170 Bruz, France
# Date: 2023-05-25

# Summary

This article presents the development of a library tool for the analysis of IGBT (Insulated Gate Bipolar Transistor) and diode components in power electronic systems. The library tool aims to evaluate the lifespan and performance of these components under specific operating conditions. It provides functionality for loss calculation, temperature estimation, and durability prediction, enabling engineers and researchers to make informed decisions during system design.

# Introduction

Power electronic systems rely heavily on the performance and reliability of IGBT and diode components. The accurate analysis of these components is crucial for designing efficient and durable systems. This article presents a library tool developed to address the need for comprehensive analysis and lifespan evaluation of IGBT and diode components.

# Features

The library tool offers the following features:

1. **Data Import**: The tool allows easy import of experimental data from Excel files, including measurements such as time, power, speed, torque, current, and power factor. This ensures seamless integration of data into the analysis process.

2. **Loss Calculation**: The library tool automatically calculates the electrical losses of IGBT and diode components based on specific parameters for each component. It takes into account characteristics such as threshold voltage, thermal resistance, switching frequency, and reference currents.

3. **Thermal Modeling**: Advanced thermal models are integrated into the tool to estimate temperature variations of IGBT and diode components based on electrical losses. These models utilize material thermal properties and thermal impedances to provide accurate results.

4. **Lifespan Calculation**: The library tool employs damage accumulation algorithms to calculate the lifespan of components. It considers charge-discharge cycles resulting from temperature variations to estimate component durability under specific conditions.

5. **Result Visualization**: The tool generates detailed reports and graphical representations to visualize the analysis results. It provides information such as estimated component lifespan, corresponding distance traveled, energy consumed per hour, and energy efficiency.

# Implementation

The library tool is implemented using python with external libraries NumPy, Pandas, Openpyxl, SciPy, Matplotlib and Rainflow.

# library Requirements

To run the library tool, the following library requirements should be met:

- Python 3.6
  - scipy==1.10.1
  - pandas==2.0.1
  - matplotlib==3.7.1
  - numpy==1.24.1
  - rainflow==3.2.0
  - openpyxl==3.1.2

# Documentation

Comprehensive documentation for the library tool is available, including online documentation, user guides and tutorials on the [README file](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/README.md) in english and a [french version](https://gitlab.com/PGarn/LifeTime_IGBT_Calculation/-/blob/main/READMEFR.md).

# Examples of Use

The library tool can be used in various applications, including:

- Optimizing the design of power electronic systems by identifying critical areas and evaluating the impact of operating parameters on component durability.
- Assessing the reliability and lifespan of IGBT and diode components under different operating conditions.
- Comparing the performance and durability of different component configurations to aid in decision-making during system design.

# Conclusion

The development of this library tool for the analysis of IGBT and diode components provides engineers and researchers with a powerful tool for evaluating component lifespan and performance in power electronic systems. By enabling comprehensive analysis and prediction of component durability, the tool supports the development of efficient, reliable, and durable systems.

We expect that this library tool will find wide usage in industry and research, contributing to the continuous improvement of performance and sustainability in power electronic systems.

# Acknowledgements

We would like to acknowledge the support from École Normale Supérieure de Rennes.

# References

- [Briac Baudais, Hamid Ben Ahmed, Gurvan Jodin, Nicolas Degrenne and Stéphane Lefebvre : Life Cycle Assessment of a 150 kW Electronic Power Inverter](https://doi.org/10.3390/en16052192)
