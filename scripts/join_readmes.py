import os
import shutil

order = (
    "basic_readme",
    "introduction",
    "why_mongodb",
    "python_mongodb_tools",
    "project_setup",
    "mongodb_atlas",
    "documents_database",
    "connection_to_db",
    "data_structure",
    "data_generators",
    "crud_queries",
    "tests",
    "resources",
)

project_directory = os.getcwd()
new_line = "\n"
if os.path.exists(f"{project_directory}/README.md"):
    os.remove(f"{project_directory}/README.md")
for index, tutorial_chapter in enumerate(order):
    temp_text = ""
    with open(
        os.path.join(f"{project_directory}/tutorial/{tutorial_chapter}", "README.md")
    ) as f:
        temp_text = f.read()
    with open(f"{project_directory}/README.md", "a") as f:
        f.write(f"{ new_line * 2 if index > 0 else ''}{temp_text}")


project_directory = os.getcwd()
for root, _, files in os.walk(f"{project_directory}/assets"):
    for file in files:
        os.remove(os.path.join(root, file))
for root, directories, f in os.walk(f"{project_directory}/tutorial"):
    for file in f:
        print(root, directories, f, file)
        directory = root.split("/")[-1]
        if directory == "assets":
            shutil.copyfile(
                os.path.join(root, file),
                os.path.join(f"{project_directory}/assets/{file}"),
            )
