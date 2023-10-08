import json
from pathlib import Path


def format_json(dir_path: Path):
    for file_path in dir_path.glob("**/*.json"):
        print(f"Detect {file_path.name}")  # noqa: T201

        with Path.open(file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        with Path.open(file_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        print(f"Format {file_path.name}")  # noqa: T201

    for file_path in dir_path.glob("**/persistent_res.json"):
        file_path.unlink()
        print(f"Delete {file_path.name}")  # noqa: T201


dir_path = Path().absolute() / "excel"
format_json(dir_path)
