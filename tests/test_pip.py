from climber import Climber
import json

c = Climber({"images" : True})

results = c.climb("wolf")
results = json.loads(results)

print "Results for search of wolf."
for bolt in results['data']:
    print "-----------------------\n"
    print "Contexts: ",
    print bolt['contexts']
    print "Text: ",
    print bolt['text']
    print "-----------------------\n"
