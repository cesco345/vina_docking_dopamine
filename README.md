# Dopamine D2 Receptor Docking with Risperidone

## Project Overview

This project focuses on understanding the interaction between the Dopamine D2 receptor (DRD2) and the atypical antipsychotic drug Risperidone. DRD2 is a crucial target for antipsychotic drugs and Parkinson’s disease therapies. However, drugs targeting DRD2 often suffer from serious side effects due to promiscuous activity against related receptors. This project aims to use molecular docking and simulation techniques to gain structural insights into how Risperidone binds to DRD2, which could inform the design of safer and more effective drugs.

### Goals
- Investigate the binding mode of Risperidone to the dopamine D2 receptor using molecular docking.
- Use homology modeling and molecular dynamics simulations to optimize receptor-ligand interactions.
- Employ computational tools to simulate the receptor-ligand binding in a biologically relevant environment.
  
## Methodology and Tools

### 1. **AutoDock Vina**
- **Objective:** Perform molecular docking of Risperidone to DRD2 to predict the binding affinity and explore binding modes.
- **Approach:** We will use a homology model of DRD2 and dock Risperidone into its orthosteric binding site using AutoDock Vina. Ligand poses will be ranked by binding affinity, and the most favorable poses will be selected for further analysis.

### 2. **ChimeraX**
- **Objective:** Visualize and refine the docking results.
- **Approach:** ChimeraX will be used to analyze the docked ligand-receptor complex, inspect the interaction sites, and prepare the system for further simulations. We'll also use ChimeraX to prepare and minimize the receptor-ligand complex for downstream molecular dynamics.

### 3. **Maestro (Schrödinger Suite)**
- **Objective:** Carry out advanced molecular modeling and refinement of ligand-receptor interactions.
- **Approach:** Using Maestro, we will refine the docked poses and optimize the structure to improve docking results. We'll also explore additional ligand conformations and energy minimizations using Schrödinger's tools.

### 4. **GROMACS**
- **Objective:** Perform molecular dynamics simulations to study the dynamics of the receptor-ligand complex.
- **Approach:** GROMACS will be used to run molecular dynamics simulations on the DRD2-Risperidone complex. This will allow us to investigate the stability of the docking results, optimize the receptor-ligand interactions in a solvated lipid bilayer environment, and analyze the dynamic behavior of the complex over time.

## Future Steps
1. **Docking:** Use AutoDock Vina to generate multiple ligand binding poses.
2. **Visualization and Refinement:** Use ChimeraX and Maestro to refine the best poses and inspect the binding interactions.
3. **Molecular Dynamics:** Use GROMACS to simulate the receptor-ligand complex in a lipid bilayer, optimizing for realistic biological conditions.
4. **Analysis:** Evaluate the results to gain insights into the structural determinants of Risperidone's binding to DRD2, with a focus on improving the specificity of potential drug candidates.

## Citation
Please cite the following paper if you use this repository:
- Wang et al., 2018. Structure of the D2 dopamine receptor bound to the atypical antipsychotic drug Risperidone. Nature. Available at: [Link to Paper]

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
