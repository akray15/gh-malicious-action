import os 
import pathlib 

workspace = os.environ.get("GITHUB_WORKSPACE", "/github/workspace")
output_path = pathlib.Path(workspace) / "github-env.txt"

with open(output_path, 'w') as f: 
    for k, v in os.environ.items(): 
        f.write(f"{k}={v}\n")
print(f"==> Wrote {output_path}")
