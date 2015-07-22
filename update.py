"""Simplified set-up code for updating the regexes for parser"""

print('Copying regexes.yaml to package directory...')
import os
import shutil
cwd = os.path.abspath(os.path.dirname(__file__))
yaml_src = os.path.join(cwd, 'uap-core', 'regexes.yaml')
if not os.path.exists(yaml_src):
    raise RuntimeError(
              'Unable to find regexes.yaml, should be at %r' % yaml_src)
yaml_dest = os.path.join(cwd, 'ua_parser', 'regexes.yaml')
shutil.copy2(yaml_src, yaml_dest)

print('Converting regexes.yaml to regexes.json...')
import json
import yaml
json_dest = yaml_dest.replace('.yaml', '.json')
regexes = yaml.load(open(yaml_dest))
with open(json_dest, "w") as f:
    json.dump(regexes, f)