#!/usr/bin/env python3

from requests import session
from subprocess import run
from argparse import ArgumentParser
try:
    import bs4
except:
    print("Beautiful Soup is required. \nAttempting to install.")
    run(["/usr/bin/apt -y install python3-bs4"], shell=True)


class Bulldust:

    def __init__(self):
        pass


    def get_google_results(self, site: str):
        try:
            s = session()
            r = s.get("https://www.google.com/search?q=site%3A" + site)
            soup = bs4.BeautifulSoup(r.text, "html.parser")

            links = [h for h in soup.find_all("a")]
            [print(str(l) + "\n") for l in links]

            links = [l.get("href") for l in links]
            #[print(l) for l in links]
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




