from pathlib import Path

label_path = Path("Dataset-Chess/labels")

for label_file in label_path.glob("*.txt"):
    new_name = label_file.name[label_file.name.find("Screenshot_"):]
    label_file.rename(new_name)