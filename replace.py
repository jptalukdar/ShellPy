import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') or file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = content.replace('shellpy.Engine', 'shellpy.Engine')\
                                 .replace('shellpy.Shells', 'shellpy.Shells')\
                                 .replace("getLogger('shellpy", "getLogger('shellpy")
            if content != new_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print('Updated', path)
