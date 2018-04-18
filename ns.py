import sys, getopt, requests
from bs4 import BeautifulSoup


def main(argv):
    vertrek = ''
    aankomst = ''
    tijd = ''
    datum = ''
    try:
        opts, args = getopt.getopt(argv, "hv:a:t:d:")  # Geeft de parameters aan.
    except getopt.GetoptError:
        print('ns.py -v <vertrek station> -a <aankomst station> -t <tijd> -d <datum in jjjjmmdd>')
        sys.exit()
    for opt, arg in opts:  # Runt door parameters en voegt ze toe aan variablen
        if opt == '-h':
            print('ns.py -v <vertrek station> -a <aankomst station> -t <tijd> -d <datum in jjjjmmdd>')
            sys.exit()
        elif opt == '-v':
            vertrek = arg
        elif opt == '-a':
            aankomst = arg
        elif opt == '-t':
            tijd = arg
        elif opt == '-d':
            datum = arg
    url = 'https://www.ns.nl/reisplanner/#/?aankomst=' + aankomst + '&aankomsttype=treinstation&tijd=' + datum + 'T' + \
          tijd + '&type=vertrek&vertrek=' + vertrek + '&vertrektype=treinstation'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    elem = soup.find_all("div", class_="Stop__departureTime")

    print(elem)


if __name__ == "__main__":
    main(sys.argv[1:])
