import os 
print("==> Python script started")
with open('/tmp/github-env.txt', 'w') as f: 
    for k, v in os.environ.items(): 
        f.write(f"{k}={v}\n")
        print("==> Entered loop")
print("==> Wrote /tmp/github-env.txt")

