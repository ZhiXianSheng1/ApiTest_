from config.Conf import YamlReader
import requests

sess = requests.sessions

ca = YamlReader("./test.yaml").read_data()
r = ca["assert"]["eq"].split(":")
print(r)
