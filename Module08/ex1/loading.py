#!/usr/bin/env python3

import sys
import importlib

def check_dependencies():
    """Verifica si las librerías están instaladas y muestra sus versiones."""
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }
    
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    
    all_ok = True
    for pkg, desc in packages.items():
        try:
            # Intentamos importar la librería dinámicamente
            lib = importlib.import_module(pkg)
            version = getattr(lib, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {desc}")
        except ImportError:
            print(f"[MISSING] {pkg} - Not found!")
            all_ok = False
            
    if not all_ok:
        print("\nERROR: Missing dependencies detected.")
        print("To fix with pip:    pip install -r requirements.txt")
        print("To fix with Poetry: poetry install")
        sys.exit(1)

def run_matrix_analysis():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    
    # 1. GENERAR DATOS CON NUMPY (Obligatorio)
    # Creamos una matriz de 1000 puntos aleatorios (simulando señales de la Matrix)
    points = 1000
    data_points = np.random.randn(points) 
    
    print(f"Processing {points} data points...")

    # 2. PROCESAR CON PANDAS
    df = pd.DataFrame(data_points, columns=['Signal_Strength'])
    # Hacemos un análisis simple (ej. media móvil para suavizar la señal)
    df['Rolling_Mean'] = df['Signal_Strength'].rolling(window=50).mean()

    # 3. VISUALIZAR CON MATPLOTLIB
    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(df['Signal_Strength'], alpha=0.3, label='Raw Signal', color='green')
    plt.plot(df['Rolling_Mean'], label='Decoded Pattern', color='lime', linewidth=2)
    plt.title("Matrix Data Stream Analysis")
    plt.legend()
    
    # Guardar el resultado
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    check_dependencies()
    run_matrix_analysis()