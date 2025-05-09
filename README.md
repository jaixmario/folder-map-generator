# Folder Map Generator (Python)

This simple Python script generates a folder and file structure map of a given directory. The output is saved as a readable text file.

---

## Features

- Recursively maps all subfolders and files
- Indents files and subfolders for clear visualization
- Supports:
  - **Windows** (e.g., `C:\Users\YourName\Documents\map`)
  - **Linux** (e.g., `/home/username/Documents/map`)
  - **Android** (e.g., `/storage/emulated/0/map`)
- Saves output to a `.txt` file

---

## Requirements

- Python 3.x
- Works on Windows, Linux, and Android (via Pydroid or Termux)

---

## How to Use

1. **Edit the paths in the script**:
   ```python
   base_path = r'C:\Users\YourName\Documents\map'  # For Windows
   # OR
   base_path = '/home/username/Documents/map'       # For Linux
   output_file = r'C:\Users\YourName\Documents\folder_map.txt'
   ```

2. **Run the script**:
   - On **Windows**: use Python IDLE, VS Code, or command line
   - On **Linux**: run in terminal with `python3 map.py`
   - On **Android**: run with **Pydroid 3** or **Termux**

3. **Check the output**:
   - A text file named `folder_map.txt` will be created containing the folder tree.

---

## Example Output

```
[Folder] Documents
  - resume.pdf
  [Folder] Projects
    - app.py
    - data.json
[Folder] Music
  - song.mp3
```

---

**Made with ♥️ by Mario**
