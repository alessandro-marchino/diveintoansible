#/bin/bash

python3 -c 'import yaml, pprint; pprint.pprint(yaml.load(open("example.yaml").read(), Loader=yaml.FullLoader))'
