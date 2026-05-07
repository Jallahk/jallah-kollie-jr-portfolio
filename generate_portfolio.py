from __future__ import annotations

import ast
import json
import re
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path


SITE_DIR = Path(__file__).resolve().parent
DATA_DIR = SITE_DIR / "data"
FILES_DIR = SITE_DIR / "files"
DEMO_UPLOADS_DIR = SITE_DIR / "demo_uploads"
DEMO_ENTRIES_PATH = SITE_DIR / "demo_entries.json"
WORKSPACE_ROOT = SITE_DIR.parent
PYCHARM_ROOT = WORKSPACE_ROOT.parent.parent

SOURCE_FOLDERS = [
    ("Machine Learning", WORKSPACE_ROOT),
    ("A&D", PYCHARM_ROOT / "A&D"),
    ("BirdBrain", PYCHARM_ROOT / "BirdBrain"),
    ("BirdBrain", PYCHARM_ROOT / "BIrdBrain"),
]

EXCLUDED_DIR_NAMES = {
    ".git",
    ".idea",
    ".venv",
    "__pycache__",
    SITE_DIR.name,
}

VIDEO_EXTENSIONS = {".mp4", ".mov", ".webm", ".m4v"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

KEYWORD_TAGS = {
    "knn": ["classification", "nearest neighbors"],
    "bayes": ["classification", "probability"],
    "regression": ["regression", "modeling"],
    "graph": ["graph", "network"],
    "tree": ["tree", "recursion"],
    "sort": ["sorting", "algorithms"],
    "swarm": ["optimization", "heuristics"],
    "perceptron": ["neural network", "classification"],
    "cluster": ["clustering", "unsupervised learning"],
    "search": ["search", "algorithms"],
    "queue": ["data structure", "simulation"],
    "stack": ["data structure"],
    "linked": ["data structure"],
    "hash": ["hashing", "lookup"],
    "image": ["image processing"],
    "food": ["graph analysis"],
    "parking": ["data analysis"],
    "curve": ["curve fitting"],
    "house": ["prediction"],
}

MODULE_HINTS = {
    "sklearn": "use scikit-learn models and evaluation tools",
    "numpy": "use NumPy for numeric computation",
    "pandas": "use pandas for tabular data handling",
    "matplotlib": "create charts or visualizations",
    "seaborn": "use seaborn for statistical plotting",
    "random": "include randomized behavior",
    "turtle": "draw graphics with turtle",
}

TOPIC_PATTERNS = [
    ("train_test_split", "split data into training and test sets"),
    ("LinearRegression", "fit a linear regression model"),
    ("polyfit", "fit a polynomial curve to data"),
    ("plt.", "render a chart or plotted output"),
    ("open(", "read from local data files"),
    ("def ", "build reusable functions"),
    ("Digraph", "model graph relationships"),
    ("Perceptron", "build a perceptron-based learner"),
    ("Queue", "work with queue operations"),
    ("Stack", "work with stack operations"),
]


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return cleaned or "file"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_header_comment(text: str) -> str:
    lines = text.splitlines()
    comment_lines: list[str] = []
    for line in lines[:8]:
        stripped = line.strip()
        if not stripped:
            if comment_lines:
                break
            continue
        if stripped.startswith("#"):
            comment = stripped.lstrip("# ").strip()
            if "coding" in comment.lower():
                continue
            comment_lines.append(comment)
            continue
        break
    return " ".join(comment_lines).strip()


def build_ast_metadata(text: str) -> dict:
    meta = {
        "docstring": "",
        "imports": [],
        "functions": [],
        "classes": [],
    }
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return meta

    meta["docstring"] = (ast.get_docstring(tree) or "").strip()
    imports: list[str] = []
    functions: list[str] = []
    classes: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.append(node.module.split(".")[0])
        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    meta["imports"] = sorted(dict.fromkeys(imports))
    meta["functions"] = sorted(dict.fromkeys(functions))
    meta["classes"] = sorted(dict.fromkeys(classes))
    return meta


def detect_tags(name: str, section: str, text: str) -> list[str]:
    tags = [section, "Python"]
    ast_meta = build_ast_metadata(text)
    header = extract_header_comment(text)
    lowered = f"{name} {header} {ast_meta['docstring']} {' '.join(ast_meta['imports'])}".lower()
    for keyword, extra_tags in KEYWORD_TAGS.items():
        if keyword in lowered:
            tags.extend(extra_tags)
    return list(dict.fromkeys(tags))


def line_count(text: str) -> int:
    return len(text.splitlines())


def preview_text(text: str, max_lines: int = 20, max_chars: int = 1200) -> str:
    lines = text.strip().splitlines()[:max_lines]
    preview = "\n".join(lines)
    if len(preview) > max_chars:
        preview = preview[: max_chars - 3].rstrip() + "..."
    return preview or "# Empty file"


def sentence_case_name(name: str) -> str:
    return name.replace("_", " ")


def human_join(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def soft_lowercase(text: str) -> str:
    first_word = text.split()[0] if text.split() else text
    if first_word.isupper():
        return text
    return text[:1].lower() + text[1:]


def sanitize_text(text: str) -> str:
    cleaned = text
    cleaned = re.sub(r"(?i)\bname:\s*jallah\s+kollie\b", "", cleaned)
    cleaned = re.sub(r"(?i)\bjallah\s+kollie\b", "", cleaned)
    cleaned = re.sub(r"(?i)\bkollie\b", "", cleaned)
    cleaned = re.sub(
        r"(?i)\b(j\.?\s*rauff|james\s+rauff|dr\.?\s*rauff|rauff)\b",
        "Dr. Rauff",
        cleaned,
    )
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"\s+([,.:;])", r"\1", cleaned)
    return cleaned.strip(" -,\n\t")


def summarize_file(source_path: Path, section: str, text: str, ast_meta: dict) -> str:
    name = sentence_case_name(source_path.stem)

    desc_parts: list[str] = []
    header = sanitize_text(extract_header_comment(text))
    docstring = sanitize_text(ast_meta["docstring"])
    purpose = docstring or header
    if re.fullmatch(r"-\*-\s*coding:.*-\*-", purpose.strip(), flags=re.IGNORECASE):
        purpose = ""
    if purpose:
        purpose = purpose.replace("\n", " ").strip().rstrip(".")
        if "Dr. Rauff" in purpose:
            purpose = "a class provided by my professor Dr. Rauff"
        desc_parts.append(f"In this project, I focus on {soft_lowercase(purpose)}.")

    import_notes = [MODULE_HINTS[module] for module in ast_meta["imports"] if module in MODULE_HINTS]
    pattern_notes = [note for token, note in TOPIC_PATTERNS if token in text]

    if not desc_parts:
        keyword_tags = [tag for tag in detect_tags(name, section, text) if tag not in {section, "Python"}]
        if keyword_tags:
            desc_parts.append(
                f"In this {section} project, I work with {human_join(keyword_tags[:3])}."
            )
        else:
            desc_parts.append(f"In this file, I share part of my {section} work.")

    behavior_bits: list[str] = []
    if ast_meta["classes"]:
        behavior_bits.append(f"I define classes like {human_join(ast_meta['classes'][:3])}")
    if ast_meta["functions"]:
        behavior_bits.append(f"I implement functions such as {human_join(ast_meta['functions'][:4])}")
    if import_notes:
        behavior_bits.append(f"I {human_join(import_notes[:2])}")
    if pattern_notes:
        filtered_pattern_notes = [
            note for note in pattern_notes
            if not (note == "implements reusable functions" and ast_meta["functions"])
        ]
        filtered_pattern_notes = [
            note for note in filtered_pattern_notes
            if not (note == "defines reusable classes" and ast_meta["classes"])
        ]
    else:
        filtered_pattern_notes = []

    if filtered_pattern_notes:
        behavior_bits.append(f"I {human_join(filtered_pattern_notes[:2])}")

    if behavior_bits:
        desc_parts.append(" ".join(bit.rstrip(".") + "." for bit in behavior_bits))

    if "open(" in text:
        file_refs = sorted(set(re.findall(r"open\(['\"]([^'\"]+)['\"]", text)))
        if file_refs:
            desc_parts.append(f"I read input from files like {human_join(file_refs[:3])}.")

    if not ast_meta["functions"] and not ast_meta["classes"] and ("print(" in text or "plt.show(" in text):
        desc_parts.append("I can run this script directly to produce output or visual results.")

    summary = " ".join(part.strip() for part in desc_parts if part.strip())
    summary = sanitize_text(summary)
    summary = re.sub(r"(Dr\. Rauff(?:\s*--\s*March\s*2025)?)", "Dr. Rauff", summary)
    summary = re.sub(r"\bIn this project, I focus on\.$", "In this project, I share my work and approach.", summary)
    return re.sub(r"\s+", " ", summary).strip()


def section_records() -> list[dict]:
    sections: list[dict] = []
    seen_sections: set[str] = set()

    for section_name, folder in SOURCE_FOLDERS:
        if section_name in seen_sections:
            existing_index = next(i for i, item in enumerate(sections) if item["name"] == section_name)
            if sections[existing_index]["available"]:
                continue

        available = folder.exists()
        record = {
            "name": section_name,
            "path": str(folder),
            "available": available,
        }
        if section_name in seen_sections:
            existing_index = next(i for i, item in enumerate(sections) if item["name"] == section_name)
            sections[existing_index] = record
        else:
            sections.append(record)
            seen_sections.add(section_name)

    return sections


def collect_files() -> tuple[list[dict], list[dict]]:
    files: list[dict] = []
    sections = section_records()

    for section in sections:
        if not section["available"]:
            continue

        section_name = section["name"]
        folder = Path(section["path"])

        for source_path in sorted(folder.rglob("*.py")):
            if any(part in EXCLUDED_DIR_NAMES for part in source_path.parts):
                continue

            relative_path = source_path.relative_to(folder)
            destination = FILES_DIR / slugify(section_name) / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, destination)

            stat = source_path.stat()
            modified = datetime.fromtimestamp(stat.st_mtime)
            text = read_text(source_path)
            ast_meta = build_ast_metadata(text)
            stem_name = sentence_case_name(source_path.stem)

            files.append({
                "id": f"{slugify(section_name)}-{slugify(str(relative_path))}",
                "title": stem_name,
                "section": section_name,
                "relative_path": str(relative_path),
                "summary": summarize_file(source_path, section_name, text, ast_meta),
                "line_count": line_count(text),
                "size_label": f"{round(stat.st_size / 1024, 1)} KB",
                "modified": modified.isoformat(),
                "modified_label": modified.strftime("%b %d, %Y"),
                "file_url": str(destination.relative_to(SITE_DIR)).replace("\\", "/"),
                "preview": preview_text(text),
                "tags": detect_tags(stem_name, section_name, text),
            })

    files.sort(key=lambda item: (item["section"], item["title"].lower()))
    return files, sections


def copy_demo_asset(asset_name: str) -> str:
    source = DEMO_UPLOADS_DIR / asset_name
    if not source.exists():
        return ""
    destination = FILES_DIR / "demos" / asset_name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return str(destination.relative_to(SITE_DIR)).replace("\\", "/")


def collect_demos() -> list[dict]:
    if not DEMO_ENTRIES_PATH.exists():
        return []

    entries = json.loads(DEMO_ENTRIES_PATH.read_text(encoding="utf-8"))
    demos: list[dict] = []

    for index, entry in enumerate(entries, start=1):
        filename = (entry.get("filename") or "").strip()
        thumbnail = (entry.get("thumbnail") or "").strip()

        video_url = copy_demo_asset(filename) if filename else ""
        thumbnail_url = copy_demo_asset(thumbnail) if thumbnail else ""

        ext = Path(filename).suffix.lower() if filename else ""
        demos.append({
            "id": f"demo-{index}",
            "title": entry.get("title", f"Demo {index}"),
            "description": entry.get("description", ""),
            "status": entry.get("status", "Private demo"),
            "project_url": entry.get("project_url", ""),
            "video_url": video_url,
            "thumbnail_url": thumbnail_url,
            "is_video": ext in VIDEO_EXTENSIONS if filename else False,
            "has_thumbnail": bool(thumbnail_url),
        })

    return demos


def build_catalog() -> dict:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    FILES_DIR.mkdir(parents=True, exist_ok=True)

    if FILES_DIR.exists():
        for child in FILES_DIR.iterdir():
            if child.is_dir():
                shutil.rmtree(child)

    files, sections = collect_files()
    demos = collect_demos()

    latest_modified = max((item["modified"] for item in files), default=None)
    latest_label = (
        datetime.fromisoformat(latest_modified).strftime("%b %d, %Y")
        if latest_modified
        else "N/A"
    )

    catalog = {
        "generated_at": datetime.now().isoformat(),
        "latest_modified_label": latest_label,
        "sections": sections,
        "section_counts": Counter(item["section"] for item in files),
        "files": files,
        "demos": demos,
    }
    return catalog


def main() -> None:
    catalog = build_catalog()
    json_path = DATA_DIR / "projects.json"
    js_path = DATA_DIR / "projects.js"
    json_payload = json.dumps(catalog, indent=2)
    json_path.write_text(json_payload, encoding="utf-8")
    js_path.write_text(f"window.PORTFOLIO_DATA = {json_payload};\n", encoding="utf-8")
    print(
        f"Generated portfolio catalog with {len(catalog['files'])} Python files and "
        f"{len(catalog['demos'])} demo entries."
    )


if __name__ == "__main__":
    main()
