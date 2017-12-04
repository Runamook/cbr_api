# -*- coding:cp1251 -*-
#!/usr/bin/python


from zeep import Client
import datetime


def get_data(bank, required_time, url):

    #print "\n\n Bank %s \n\n" % bank
    client = Client(url)
    result = client.service.Data135FormFullXML(bank, required_time)

    for i in result.xpath('F135_3'):
        V = i.xpath('V3')
        C = i.xpath('C3')
        if len(V) == 0:
            pass
            #return "C = %s" % (C[0].text)
        else:
            #return "C = %s, V = %s" % (C[0].text, V[0].text)
            print "%s;%s;%s" % (required_time, V[0].text, C[0].text)
            #print (C[0].text, V[0].text)

# >>> print res.xpath('F135_3/C3')[0].text
# Н1
# >>> print res.xpath('F135_3/V3')[0].text
# 10.540

def main():
    
    url = 'http://www.cbr.ru/CreditInfoWebServ/CreditOrgInfo.asmx?WSDL'
    bank = '1481'
    
    print "Year;V;C"
    start_year = 2013
    end_year = 2017

    day = 1

    for i in range(end_year - start_year):
        year = start_year + i + 1

        for j in range(12):
            month = j + 1

            required_time = datetime.date(year, month, day)
    
            get_data(bank, required_time, url)
            #(norm, value) = get_data(bank, required_time, url)
            #print "%s,%s,%s" % (required_time, norm, value)


    # bank_list = ['1481'] 
    # 1481 - Sberbank
    
    # End of variables
    
if __name__ == "__main__":
    main()
