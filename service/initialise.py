from octopus.modules.cache import cache

def initialise():
    # generate the csv cache
    print "Generating CSV export cache file"
    cache.generate_file("csv", respect_timeout=True)    # respect the timeout so we don't regenerate it every time we restart
