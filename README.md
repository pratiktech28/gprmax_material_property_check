[![Material Property NRMSE Validation](https://github.com/pratiktech28/gprmax_material_property_check/actions/workflows/property.yml/badge.svg)](https://github.com/pratiktech28/gprmax_material_property_check/actions/workflows/property.yml)

<img width="600" height="73" alt="download" src="https://github.com/user-attachments/assets/2fb4460a-95b9-47ec-96d2-f9a5d059bddd" />                          

<img width="225" height="225" alt="download" src="https://github.com/user-attachments/assets/322d4dc7-6270-4d26-9af3-1779476417da" />


![download](https://github.com/user-attachments/assets/549da7ec-7e15-453d-8cf7-914f03da6ce7)

**🛠️ gprMax Material Property Check**

Automated Physics Validation Gate using NRMSE for High-Fidelity EM Simulations.

**📌 Overview**
This repository serves as an Automated Quality Assurance (QA) Gate for gprMax simulations. It focuses on validating simulated material constants (permittivity, conductivity, etc.) against theoretical benchmarks. By automating this process, we ensure that every simulation remains physically accurate and free from manual configuration errors.

**🧪 Mathematical Foundation**

To quantify the reliability of the simulations, I have implemented a validation logic based on the Normalized Root Mean Square Error (NRMSE).

**$$NRMSE = \frac{\sqrt{\text{mean}((Simulated - Theoretical)^2)}}{\max(Theoretical) - \min(Theoretical)}$$**

**Normalized Quality Metric**: This provides a unitless reliability score, allowing for standardized testing across different material types.
**Precision Threshold**: A strict 0.01 (1%) threshold is defined. Any simulation exceeding this error margin triggers an automatic failure in the CI/CD pipeline.

<img width="249" height="132" alt="image" src="https://github.com/user-attachments/assets/b767c9d9-5235-45c7-8471-5e93b4cff61d" />
<strong>
  Keys: Automated Material Property check demonstrating a perfect NRMSE of 0.000000, 
  performing well within the pre-defined 0.01 (1%) accuracy threshold for 
  high-fidelity physics simulations.
</strong>


**🚀 Key Features**
**1. Local Validation Logic**
The core engine performs a deep-dive check on material properties post-simulation.
Proof of Accuracy: Achieved a perfect NRMSE of 0.000000 during benchmark testing, ensuring the implementation is mathematically sound.

**2. GitHub Actions: Live Physics Automation**
I have integrated this logic into a CI/CD Pipeline to provide real-time validation for every code change or simulation update.
Automated Workflow: GitHub Actions spins up the environment, executes gprMax, calculates the NRMSE, and generates a pass/fail report dynamically.
Reliability: Ensures that physics-based fidelity is maintained even in remote cloud environments.

**📦 Getting Started**
```
Installation
# Clone the repository
git clone https://github.com/pratiktech28/gprmax_material_property_check.git

# Install necessary dependencies
pip install numpy matplotlib
```
---
```
Running the Test
# Execute the automated validation script
python scripts/material_validation.py




