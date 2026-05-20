import yaml
import os

OUTPUT_DIR = "hello_world_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("hello_world.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

for entry in data["hello_world_programs"]:
    language = entry["language"]
    extension = entry.get("extension", ".txt")
    code = entry.get("code", "").strip()
    note = entry.get("note", "")

    # Build a safe filename from the language name
    safe_name = language.lower().replace(" ", "_").replace("/", "_").replace("#", "sharp").replace("+", "plus").replace("!", "")
    filename = f"hello_{safe_name}{extension}"
    filepath = os.path.join(OUTPUT_DIR, filename)

    content = code if code else f"# {language}\n# Note: {note}\n"

    with open(filepath, "w", encoding="utf-8") as out:
        out.write(content + "\n")

    print(f"Created: {filepath}")

print(f"\nDone! {len(data['hello_world_programs'])} files written to '{OUTPUT_DIR}/'")
