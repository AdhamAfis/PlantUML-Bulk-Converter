# Batch PUML to PNG Converter

This script allows you to convert all `.puml` (PlantUML) files in a specified folder (and its subfolders) to `.png` format. It uses the PlantUML library and Java to perform the conversion, and it also verifies the required dependencies are installed before proceeding.

---

## Features
1. Recursively finds all `.puml` files in a folder.
2. Converts each `.puml` file to a `.png` image using PlantUML.
3. Saves the converted `.png` files to a `png_output` directory within the specified folder.
4. Verifies that required dependencies (`Java` and `Graphviz`) are installed.
5. Provides helpful error messages for missing dependencies or issues during the conversion process.

---

## Requirements

1. **Java**  
   Java must be installed on your system and accessible in the system's PATH.
   - To verify, run: `java -version`
   - [Download Java](https://www.oracle.com/java/technologies/javase-downloads.html)

2. **Graphviz**  
   Graphviz (required by PlantUML for rendering diagrams) must be installed and accessible in the system's PATH.
   - macOS: `brew install graphviz`
   - Linux: `sudo apt-get install graphviz`
   - Windows: `choco install graphviz` (using [Chocolatey](https://chocolatey.org/))

3. **PlantUML jar file**  
   The `plantuml.jar` file must be present in the same directory as the script.
   - [Download PlantUML](https://plantuml.com/download)

---

## Installation

1. Clone or download this repository to your local machine.
2. Ensure that `plantuml.jar` is in the same directory as this script.
3. Ensure that `java` and `dot` (Graphviz) are installed and properly set up in your system's PATH.

---

## Usage

Run the script from the command line with the folder containing `.puml` files as the argument:

```bash
python convert_puml_to_png.py <folder_path>
```

### Arguments:
- `<folder_path>`: The folder where `.puml` files are located. The script will search this folder and all its subfolders for `.puml` files.

### Example:
```bash
python convert_puml_to_png.py /path/to/puml/files
```

### Output:
- The script creates a subdirectory named `png_output` in the provided folder path.
- All converted `.png` files are saved in this directory.

---

## How It Works

1. **Dependency Check**  
   - Verifies if `java` and `Graphviz` are installed.
   - Exits with an error message if a dependency is missing.

2. **Find PUML Files**  
   - Searches the specified folder and its subfolders for `.puml` files.

3. **Convert PUML to PNG**  
   - For each `.puml` file found:
     - Executes the PlantUML JAR with Java to generate a `.png` image.
     - Saves the output to the `png_output` directory.

4. **Error Handling**  
   - Reports any issues, such as:
     - Missing `.puml` files in the folder.
     - Problems with the PlantUML conversion process.

---

## Troubleshooting

### Common Errors and Fixes

1. **Java not installed**
   ```
   Error: Java is not installed. Please install Java first.
   ```
   - Ensure Java is installed and available in your system's PATH.

2. **Graphviz not installed**
   ```
   Error: Graphviz is not installed. Please install it first:
     macOS: brew install graphviz
     Linux: sudo apt-get install graphviz
     Windows: choco install graphviz
   ```

3. **PlantUML jar not found**
   ```
   Error: plantuml.jar not found in the current directory
   Please download it from https://plantuml.com/download
   ```
   - Ensure the `plantuml.jar` file is in the same directory as the script.

4. **No PUML files found**
   ```
   No .puml files found in <folder>
   ```
   - Check that the specified folder contains `.puml` files.

---

## Advanced Use

### Modify Output Directory
You can modify the script to save `.png` files to a custom directory instead of the default `png_output` folder.

### Add Logging
For detailed logs, replace `print` statements with logging using Python's `logging` module.

---

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it.

---

## Contributing
Pull requests and suggestions are welcome! If you encounter any issues, please open a GitHub issue.

---

## References
- [PlantUML Documentation](https://plantuml.com/)
- [Graphviz](https://graphviz.org/)
- [Java Downloads](https://www.oracle.com/java/technologies/javase-downloads.html)