from urllib import request

goog_url = 'http://www.quietaffiliate.com/Files/CSV_Database_of_First_Names.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)
