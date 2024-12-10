import os
import subprocess
import argparse
from pathlib import Path
import shutil

def check_dependencies():
    # Check for Java
    try:
        subprocess.run(['java', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Java is not installed. Please install Java first.")
        return False

    # Check for Graphviz
    if not shutil.which('dot'):
        print("Error: Graphviz is not installed. Please install it first:")
        print("  macOS: brew install graphviz")
        print("  Linux: sudo apt-get install graphviz")
        print("  Windows: choco install graphviz")
        return False
    
    return True

def convert_puml_to_png(folder_path):
    if not check_dependencies():
        return
    
    # Convert folder path to Path object
    folder = Path(folder_path)
    
    # Create output directory
    output_dir = folder / 'png_output'
    output_dir.mkdir(exist_ok=True)
    
    # Find all .puml files recursively
    puml_files = list(folder.rglob('*.puml'))
    
    if not puml_files:
        print(f"No .puml files found in {folder}")
        return
    
    # Check if plantuml.jar exists in the current directory
    plantuml_jar = Path.cwd() / "plantuml.jar"
    if not plantuml_jar.exists():
        print("Error: plantuml.jar not found in the current directory")
        print("Please download it from https://plantuml.com/download")
        return
    
    print(f"Found {len(puml_files)} PUML files. Converting...")
    
    # Convert each file
    for puml_file in puml_files:
        try:
            # Run PlantUML to convert the file with output directory specified
            subprocess.run(['java', '-jar', str(plantuml_jar), '-o', str(output_dir), str(puml_file)], check=True)
            print(f"Successfully converted {puml_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {puml_file.name}: {e}")
        except Exception as e:
            print(f"Unexpected error with {puml_file.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PUML files to PNG in a folder')
    parser.add_argument('folder', help='Folder containing PUML files')
    args = parser.parse_args()
    
    convert_puml_to_png(args.folder)