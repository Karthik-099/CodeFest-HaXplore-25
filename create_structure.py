import os
from pathlib import Path


base_dir = Path("ai-code-editor")


structure = {
    "frontend": {
        "public": ["index.html", "favicon.ico", "manifest.json"],
        "src": {
            "components": ["Navbar.jsx", "Sidebar.jsx", "CodeEditor.jsx"],
            "pages": ["Login.jsx", "Editor.jsx", "Dashboard.jsx"],
            "services": ["api.js", "socket.js"],
            "utils": ["auth.js"],
            "App.jsx": "",
            "index.jsx": "",
            "styles.css": "",
        },
        "package.json": "",
        "package-lock.json": "",
        ".env": "",
        "README.md": "",
    },
    "backend": {
        "app": {
            "api": {
                "endpoints": ["auth.py", "files.py", "__init__.py"],
                "websockets": ["collaborate.py"],
                "__init__.py": "",
            },
            "core": ["config.py", "security.py", "utils.py"],
            "db": {
                "models.py": "",
                "migrations": [],
                "__init__.py": "",
            },
            "services": ["ai_services.py", "file_services.py", "__init__.py"],
            "static": [],
            "templates": [],
            "main.py": "",
            "schemas.py": "",
            "__init__.py": "",
        },
        "tests": ["test_auth.py", "test_files.py", "__init__.py"],
        "requirements.txt": "",
        "Dockerfile": "",
        ".env": "",
        "README.md": "",
    },
    "ai-services": {
        "linting": ["linting.py"],
        "autocomplete": ["autocomplete.py"],
        "documentation": ["documentation.py"],
        "utils": ["openai_utils.py"],
    },
    "devops": {
        "docker-compose.yml": "",
        "nginx": ["nginx.conf"],
        "kubernetes": ["deployment.yaml", "service.yaml"],
        "scripts": ["deploy.sh"],
    },
    ".gitignore": "",
    "README.md": "",
    "create_structure.py": "",
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            
            path.mkdir(parents=True, exist_ok=True)
            for file in content:
                (path / file).touch()
        else:
            
            path.touch()


create_structure(base_dir, structure)

print(f"Folder structure created successfully at {base_dir}")