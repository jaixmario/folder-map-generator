import os

base_path = r'C:\Users\YourName\Documents\map'  # Change this to your desired path
output_file = r'C:\Users\YourName\Documents\folder_map.txt'

def map_folder(path, indent=0):
    items = []
    for entry in sorted(os.listdir(path)):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            items.append('  ' * indent + f'[Folder] {entry}')
            items += map_folder(full_path, indent + 1)
        else:
            items.append('  ' * indent + f'- {entry}')
    return items

if os.path.exists(base_path):
    folder_map = map_folder(base_path)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(folder_map))
    print(f"Folder map saved to: {output_file}")
else:
    print(f"Path does not exist: {base_path}")
