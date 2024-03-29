#!/usr/bin/env python3

from subprocess import run
from argparse import ArgumentParser

try:
    from googlesearch import search
except:
    print("Installing Google library")
    run(["/usr/local/bin/pip3 install google"], shell=True)

class Bulldust:

    def __init__(self):
        pass


    def get_google_results(self, site: str):
        try:
            results = search("site:" + site, tld="com", lang="en", num=99999999, stop=None, pause=1)
            [print(r) for r in results]
        except Exception as e:
            print("Error! in get_google_results: " + str(e))
            exit(1)


    def get_site(self):
        try:
            arg = ArgumentParser()
            arg.add_argument("site", help="site to fetch results for: eg. google.com", type = str)
            parsed = arg.parse_args()
            if parsed:
                if parsed.site:
                    site = parsed.site
                    if not len(site) > 99:
                        if "." in str(site):
                            if not str(site).startswith("http"):
                                return str(site)
                            else:
                                print("Please do not include protocol in url")
                                exit(1)
            exit(1)
        except Exception as e:
            print("Error! in get_site: " + str(e))
            exit(1)


    def print_banner(self):
        try:
            print("         __n__n__")
            print("  .------`-\\00/-\'")
            print(" /  ##  ## (oo)")
            print("/ \## __  ./")
            print(" |//YY \|/")
            print(" |||   |||  Bulldust!\n")

        except Exception as e:
            print("Error! in print_banner: " + str(e))


    def controller(self):
        try:
            self.print_banner()
            self.get_google_results(self.get_site())
        except Exception as e:
            print("Error! in controller: " + str(e))
            exit(1)

def builder():
    try:
        new_bulldust = Bulldust()
        return new_bulldust
    except Exception as e:
        print("Error! building new Bulldust object: " + str(e))
        exit(1)

def main():
    builder().controller()

if __name__ == '__main__':
    main()




