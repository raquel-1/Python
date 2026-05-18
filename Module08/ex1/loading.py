#!/usr/bin/env python3
# check the files in your virtual environment and ask the system,
# “Hey, what exact version of Pandas is installed here?”
import importlib.metadata
import sys


try:
    # pyplot draw grafics
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    # GLOBAL
    DEPENDENCIES_PRESENT = True
except ImportError:
    DEPENDENCIES_PRESENT = False


def check_dependencies() -> None:
    """
    check the versions installed in the production env
    """
    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    # checking the dictionary packages
    for pack, message in packages.items():
        try:
            # version = what version of this package is available?
            version: str = importlib.metadata.version(pack)
            print(f"[OK] {pack} ({version}) - {message}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {pack} - Not found")


def data_process_graph() -> None:
    """
    data is generated -> processed -> graph
    """
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    #  initializes NumPy random number generator with a seed(seed=42)
    # default_rng = Default Random Number Generator
    # seed= 42 = compu ∞ use the same mathematical formula to generate Num
    rng = np.random.default_rng(seed=42)
    # generate list of 1000 random n following campana de Gauss
    data_points = rng.normal(loc=0.0, scale=1.0, size=1000)

    # take numbers from NumPy -> Pandas to create DataFrame
    df = pd.DataFrame(data_points, columns=["Signal_Strength"])

    print("Generating visualization...")
    # preparing to draw 10x6
    plt.figure(figsize=(10, 6))
    # plot a line graph using 1000 data from columns=["Signal_Strength"]
    plt.plot(df["Signal_Strength"], color="green")
    # Top title for the graph
    plt.title("Matrix Data Stream Analysis")

    # store the final file name in a text variable
    output_file: str = "matrix_analysis.png"
    # take the drawing and save it to your hard drive as a normal image
    plt.savefig(output_file)
    # free space
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    if not DEPENDENCIES_PRESENT:
        print("LOADING STATUS: Loading programs...")
        print("Checking dependencies:")
        # Forzamos la visualización de los paquetes caídos
        for pkg in ["pandas", "numpy", "matplotlib"]:
            print(f"[MISSING] {pkg} - Not found")
        print("\nERROR: Missing dependencies detected.")
        print("To fix with pip:    pip install -r requirements.txt")
        print("To fix with Poetry: poetry install")
        sys.exit(1)

    check_dependencies()
    data_process_graph()


if __name__ == "__main__":
    main()
