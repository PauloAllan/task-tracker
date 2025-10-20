import json
from pathlib import Path
from typing import List
from .models import Task

DATA_FILE = Path('data/tasks.json')

def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text('[]', encoding='utf-8')

def read_tasks() -> List[dict]:
    ensure_data_file()
    text = DATA_FILE.read_text(encoding='utf-8')
    return json.loads(text)

def write_tasks(tasks: List[dict]):
    DATA_FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding='utf-8')

def next_id(tasks: List[dict]) -> int:
    if not tasks:
        return 1
    return max(t['id'] for t in tasks) + 1
