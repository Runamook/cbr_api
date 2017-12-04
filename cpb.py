# -*- coding:cp1251 -*-
#!/usr/bin/python


from zeep import Client
import datetime
import codecs
import os


def get_data(bank, required_time, url):

    client = Client(url)
    result = client.service.Data135FormFullXML(bank, required_time)
    header = "Year;V;C"
    filename = bank + '.xlsx'

    # Check if file already exists. If yes - append to it, otherwise - create a new one

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'

    with codecs.open(filename, append_write,'utf-8') as ofile:

        for i in result.xpath('F135_3'):
            V = i.xpath('V3')
            C = i.xpath('C3')

            if len(V) == 0:
                pass
            else:
            
                line = "%s;%s;%s" % (required_time, V[0].text, C[0].text)
                ofile.write(line + '\n')
                print line

def main():
    
    url = 'http://www.cbr.ru/CreditInfoWebServ/CreditOrgInfo.asmx?WSDL'
    bank = '1481'
    
    start_year = 2011
    end_year = 2017

    day = 1

    for i in range(end_year - start_year):
        year = start_year + i + 1

        for j in range(12):
            month = j + 1

            required_time = datetime.date(year, month, day)
    
            get_data(bank, required_time, url)

    # bank_list = ['1481'] 
    # 1481 - Sberbank
    
if __name__ == "__main__":
    main()
