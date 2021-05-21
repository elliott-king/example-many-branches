import uuid
import subprocess

x = 1
for i in range(x):
    id = str(uuid.uuid4())[:8]
    commands = [
        'git checkout main',
        f'git checkout -b new-branch-{id}',
        'git add .',
        f'git commit -m {id}',
        f'git push origin new-branch-{id}',
        'git checkout main'
    ]

    for command in commands:
        subprocess.run(command.split(), check=True, text=True)

