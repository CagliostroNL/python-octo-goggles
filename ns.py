import sys, getopt, requests
import xml.etree.ElementTree as ET



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
    url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation=' + vertrek + '&toStation=' + aankomst
    res = requests.get(url, auth=('mail', 'password'))
    xml = res.content
    #xmlc = ET.parse(xml)
    getstring = ET.fromstring(xml)
    #print(xml)
    #print(res)
    print(getstring[0][6].text)
    for iit in range(0, (len(getstring))):

        vertrekTijdString = getstring[0][1].find('GeplandeVertrekTijd').text
        vertrekTijd = vertrekTijdString
        print(iit)
        print(type(vertrekTijd))

if __name__ == "__main__":
    main(sys.argv[1:])
