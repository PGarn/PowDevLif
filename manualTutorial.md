## Tutorial: Installation and Usage of PowDevLif

This tutorial provides step-by-step instructions on how to install and use the PowDevLif project. This open-source project allows for thermal analysis and modeling of power electronic components, including power loss calculations, temperature estimation, and lifetime prediction. It utilizes Python and various libraries for data manipulation, computation, and visualization.

### Installation

To install the PowDevLif project, follow these steps:

1. Install Python: Ensure that you have Python 3.6 or later installed on your system. If you don't have Python installed, you can download and install it from the official Python website: [python.org](https://www.python.org).

2. Install Required Libraries: Open a command line interface, such as Terminal or Command Prompt, and run the following commands to install the required Python libraries:
   - scipy==1.10.1
   - pandas==2.0.1
   - matplotlib==3.7.1
   - numpy==1.24.1
   - rainflow==3.2.0
   - openpyxl==3.1.2

   Use the `pip install` command followed by the library name and version to install each library.

3. Download Project Files: Download all the files from the LifeTime_IGBT_Calculation repository and maintain the same file organization.

### Usage

To use the PowDevLif project, follow these steps:

1. Prepare Data: Replace the example files in the "examples" directory with your own data. The "variables.py" file contains a dictionary where you can store all the necessary data. For the Excel file, ensure that the correct path to the file is provided in the "variables.py" file (line 52).

2. Run the Program: Execute the "lifetime.py" file. If everything is launched successfully, call the "pdl_calculation()" function. It will return the following values in order: "lifetime_IGBT", "lifetime_diode", "number_of_km_IGBT", "e_kwh_byhours", and "efficiency".

3. Integrate with Your Script: To integrate the PowDevLif project into your own script, import the "lifetime" module and invoke the "pdl_calculation()" function. Here's an example:

   import lifetime
   lifetime_IGBT, lifetime_diode = lifetime.pdl_calculation()
   
   You can modify line 44 in "lifetime.py" to return additional data such as "number_of_km_IGBT", "e_kwh_byhours", and "efficiency".
   If you want to display graphs use pdl_graphs()
