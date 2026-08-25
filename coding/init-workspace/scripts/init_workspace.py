#!/usr/bin/env python3
"""
init_workspace.py - Automated workspace initialization CLI script for AI agent development.
Scaffolds standard .ai/ workspace documentation (AGENTS.md, LESSONS_LEARNED.md,
FEATURE_HISTORY.md, TASKS.md, ARCHITECTURE.md) tailored to target repository.
"""

import argparse
import datetime
import json
import os
import subprocess
import sys

IGNORE_DIRS = {
    ".git", ".svn", ".hg", ".ai", "node_modules", "venv", ".venv", "env",
    "__pycache__", ".pytest_cache", ".ruff_cache", "dist", "build", "target",
    ".idea", ".vscode", ".next", ".nuxt", "bin", "obj"
}

def detect_project_type(root_path):
    info = {
        "project_name": os.path.basename(os.path.abspath(root_path)) or "My Project",
        "tech_stack": "Generic / Unspecified",
        "primary_languages": "Markdown / Text",
        "install_cmd": "echo 'No install step specified'",
        "build_cmd": "echo 'No build step specified'",
        "test_cmd": "echo 'No test suite specified'",
        "main_entry_point": "Unknown"
    }

    pkg_json = os.path.join(root_path, "package.json")
    pyproject = os.path.join(root_path, "pyproject.toml")
    req_txt = os.path.join(root_path, "requirements.txt")
    cargo_toml = os.path.join(root_path, "Cargo.toml")
    go_mod = os.path.join(root_path, "go.mod")

    if os.path.exists(pkg_json):
        info["tech_stack"] = "Node.js / JavaScript / TypeScript"
        info["primary_languages"] = "JavaScript / TypeScript"
        info["install_cmd"] = "npm install"
        info["build_cmd"] = "npm run build"
        info["test_cmd"] = "npm test"
        try:
            with open(pkg_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "name" in data:
                    info["project_name"] = data["name"]
                if "main" in data:
                    info["main_entry_point"] = data["main"]
                elif os.path.exists(os.path.join(root_path, "src", "index.ts")):
                    info["main_entry_point"] = "src/index.ts"
                elif os.path.exists(os.path.join(root_path, "src", "index.js")):
                    info["main_entry_point"] = "src/index.js"
        except Exception:
            pass

    elif os.path.exists(pyproject) or os.path.exists(req_txt):
        info["tech_stack"] = "Python"
        info["primary_languages"] = "Python"
        info["install_cmd"] = "pip install -r requirements.txt" if os.path.exists(req_txt) else "pip install -e ."
        info["build_cmd"] = "python -m build"
        info["test_cmd"] = "pytest"
        if os.path.exists(os.path.join(root_path, "main.py")):
            info["main_entry_point"] = "main.py"
        elif os.path.exists(os.path.join(root_path, "app.py")):
            info["main_entry_point"] = "app.py"

    elif os.path.exists(cargo_toml):
        info["tech_stack"] = "Rust"
        info["primary_languages"] = "Rust"
        info["install_cmd"] = "cargo check"
        info["build_cmd"] = "cargo build"
        info["test_cmd"] = "cargo test"
        info["main_entry_point"] = "src/main.rs"

    elif os.path.exists(go_mod):
        info["tech_stack"] = "Go"
        info["primary_languages"] = "Go"
        info["install_cmd"] = "go mod download"
        info["build_cmd"] = "go build ./..."
        info["test_cmd"] = "go test ./..."
        info["main_entry_point"] = "main.go"

    return info

def get_git_info(root_path):
    git_commits = []
    init_hash = "N/A"
    try:
        res = subprocess.run(
            ["git", "log", "-n", "10", "--oneline"],
            cwd=root_path,
            capture_output=True,
            text=True,
            check=True
        )
        lines = res.stdout.strip().split("\n")
        for l in lines:
            if l.strip():
                git_commits.append(l.strip())
        if git_commits:
            init_hash = git_commits[0].split()[0]
    except Exception:
        pass
    return git_commits, init_hash

def generate_dir_tree(root_path, max_depth=2):
    lines = [f"{os.path.basename(os.path.abspath(root_path))}/"]
    
    def _walk(current_dir, depth):
        if depth > max_depth:
            return
        try:
            entries = sorted(os.listdir(current_dir))
        except Exception:
            return

        dirs = [e for e in entries if os.path.isdir(os.path.join(current_dir, e)) and e not in IGNORE_DIRS]
        files = [e for e in entries if os.path.isfile(os.path.join(current_dir, e))]

        indent = "│   " * depth
        for d in dirs[:10]:
            lines.append(f"{indent}├── {d}/")
            _walk(os.path.join(current_dir, d), depth + 1)

        for f in files[:10]:
            lines.append(f"{indent}├── {f}")

    _walk(root_path, 1)
    return "\n".join(lines)

def scaffold(root_path, output_subfolder=".ai", overwrite=False):
    target_dir = os.path.join(root_path, output_subfolder)
    os.makedirs(target_dir, exist_ok=True)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.abspath(os.path.join(script_dir, "..", "assets"))

    proj_info = detect_project_type(root_path)
    git_commits, init_hash = get_git_info(root_path)
    dir_tree = generate_dir_tree(root_path)
    today_str = datetime.date.today().strftime("%Y-%m-%d")

    commit_list_str = "\n".join([f"  - `{c}`" for c in git_commits]) if git_commits else "  - Initial commit"

    replacements = {
        "${PROJECT_NAME}": proj_info["project_name"],
        "${TECH_STACK}": proj_info["tech_stack"],
        "${PRIMARY_LANGUAGES}": proj_info["primary_languages"],
        "${INSTALL_CMD}": proj_info["install_cmd"],
        "${BUILD_CMD}": proj_info["build_cmd"],
        "${TEST_CMD}": proj_info["test_cmd"],
        "${MAIN_ENTRY_POINT}": proj_info["main_entry_point"],
        "${INIT_DATE}": today_str,
        "${INIT_COMMIT_HASH}": init_hash,
        "${FEATURE_INDEX_ITEMS}": "- [Feature: Ongoing Refactor](#feature-ongoing-refactor)",
        "${FEATURE_SECTIONS}": f"## Feature: Ongoing Refactor\n- **Status**: In Progress\n- **Description**: Recent session changes and ongoing development.\n\n### Session Log: Recent Commit History\n- **Date**: {today_str}\n- **Summary**: Session developments extracted from git repository.\n- **Git Commits**:\n{commit_list_str}\n",
        "${DIRECTORY_TREE}": dir_tree
    }

    templates = [
        ("AGENTS.md.template", "AGENTS.md"),
        ("LESSONS_LEARNED.md.template", "LESSONS_LEARNED.md"),
        ("FEATURE_HISTORY.md.template", "FEATURE_HISTORY.md"),
        ("TASKS.md.template", "TASKS.md"),
        ("ARCHITECTURE.md.template", "ARCHITECTURE.md"),
    ]

    created_files = []
    skipped_files = []

    for t_file, out_file in templates:
        t_path = os.path.join(assets_dir, t_file)
        out_path = os.path.join(target_dir, out_file)

        if os.path.exists(out_path) and not overwrite:
            skipped_files.append(out_file)
            continue

        if os.path.exists(t_path):
            with open(t_path, "r", encoding="utf-8") as f:
                content = f.read()
            for key, val in replacements.items():
                content = content.replace(key, str(val))
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            created_files.append(out_file)
        else:
            print(f"Warning: Template file missing: {t_path}", file=sys.stderr)

    return target_dir, created_files, skipped_files

def main():
    parser = argparse.ArgumentParser(description="Initialize .ai/ workspace documentation for AI agent development.")
    parser.add_argument("--path", default=".", help="Root path of target repository (default: current directory)")
    parser.add_argument("--output-dir", default=".ai", help="Subfolder for workspace files (default: .ai)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing workspace files if present")
    
    args = parser.parse_args()
    abs_path = os.path.abspath(args.path)

    if not os.path.isdir(abs_path):
        print(f"Error: Target path '{abs_path}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    target_dir, created, skipped = scaffold(abs_path, args.output_dir, args.overwrite)

    print(f"Successfully initialized workspace in '{target_dir}'!")
    if created:
        print("Created files:")
        for f in created:
            print(f"  - {f}")
    if skipped:
        print("Skipped existing files (use --overwrite to replace):")
        for f in skipped:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
