import os 
with open('/tmp/github-env.txt', 'w') as f: 
for k, v in os.environ.items(): 
    f.write(f"{k}={v}\n")
