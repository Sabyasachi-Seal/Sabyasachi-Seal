import requests
import random
import yaml
import os

# readmeraw = "https://raw.githubusercontent.com/Sabyasachi-Seal/Sabyasachi-Seal/main/README.md"

# cronjobraw = "https://raw.githubusercontent.com/Sabyasachi-Seal/Sabyasachi-Seal/main/.github/workflows/Profile3D.yml"

# readme = requests.get(readmeraw)

# cron = requests.get(cronjobraw)

# readmecontent = readme.text

# croncontent = cron.text

# cron = croncontent[croncontent.index("- cron"): croncontent.index("- cron") + 21]

yamlfile =  open('.github\workflows\Profile3D.yml', 'r')
fullfile = yaml.load(yamlfile, Loader=yaml.FullLoader)
yamlfile.close()

cron = fullfile[True]["schedule"][-1]["cron"]

# print(cron)

cron = "0 */" + str(random.randint(1, 8)) + " * * *"

fullfile[True]["schedule"][-1]["cron"] = cron

# print(fullfile)

yamlfile =  open('.github\workflows\Profile3D.yml', 'w')
yaml.dump(fullfile, yamlfile)
yamlfile.close()

print("Updated Cron Job")

os.system('git add .')
os.system('git commit -m "Cron Job Update"')
os.system('git push')