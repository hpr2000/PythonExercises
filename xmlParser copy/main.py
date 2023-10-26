import xml.etree.ElementTree as XET


def xml_parse():
    tree = XET.parse('example.xml')
    root = tree.getroot()

    for person in root.findall('person'):
        name = person.find('name').text
        age = person.find('age').text
        city = person.find('city').text
        state = person.find('state').text
        country = person.find('country').text

        print(f'Name:{name} Age:{age} City:{city} State:{state} Country:{country}')


if __name__ == '__main__':
    xml_parse()
