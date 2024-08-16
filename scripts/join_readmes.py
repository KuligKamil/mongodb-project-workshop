import os

project_directory = os.getcwd()
for root, _, f in os.walk(f"{project_directory}/tutorial"):
    for file in f:
        if file.endswith(".md"):
            temp_text = ""
            with open(os.path.join(root, file)) as f:
                temp_text = f.read()
            with open(f"{project_directory}/README.md", "a") as f:
                f.write(f"\n\n{temp_text}")
# TODO: add order of flies
