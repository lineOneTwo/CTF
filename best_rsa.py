from sameNAttack import same_n_attack
from Crypto.Util.number import *

n = 13060424286033164731705267935214411273739909173486948413518022752305313862238166593214772698793487761875251030423516993519714215306808677724104692474199215119387725741906071553437840256786220484582884693286140537492541093086953005486704542435188521724013251087887351409946184501295224744819621937322469140771245380081663560150133162692174498642474588168444167533621259824640599530052827878558481036155222733986179487577693360697390152370901746112653758338456083440878726007229307830037808681050302990411238666727608253452573696904083133866093791985565118032742893247076947480766837941319251901579605233916076425572961
e1 = 117
e2 = 65537
c1 = open(r"D:\Program Files\JetBrains\PyCharm Community Edition 2020.2\CTF\file\cipher1.txt", "rb").read()
c2 = open(r"D:\Program Files\JetBrains\PyCharm Community Edition 2020.2\CTF\file\cipher2.txt", "rb").read()
m = same_n_attack(n, e1, e2, bytes_to_long(c1), bytes_to_long(c2))
print(long_to_bytes(m))
