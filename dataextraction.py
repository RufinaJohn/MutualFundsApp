import pdfplumber as pb
import pandas as pd
import schemetypedata as stdata
column_headers = [
    'Scheme Name',
    'Scheme Type',
    'Scheme Subtype',
    'No. of Schemes',
    'No. of Folios',
    'Funds Mobilized (INR in crore)',
    'Repurchase/Redemption (INR in crore)',
    'Net Assets Under Management (INR in crore)',
    'Average Net Assets Under Management (INR in crore)',
    'No. of segregated portfolios created',
    'Net Assets Under Management in segregated portfolio (INR in crores)',
    'Net Inflow or Outflow',
    'Net Asset under Management per Scheme',
    'Net Inflow or Outflow per Scheme',
    'month and year'
]
def get_tables(path):
    tables = dict()
    with pb.open(path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            tables[table[0][0][32:]] = page.extract_table()
    return tables


def add_data_to_dataframe(table, tbname):
    for row in range(2, len(table)):
        if table[row][1] is None or table[row][1].strip() == '-' or table[row][1].strip() == '':
            continue
        name = table[row][1].strip()

        if row in stdata.openindex:
            type = stdata.types[0]
        elif row in stdata.closedindex:
            type = stdata.types[1]
        elif row in stdata.intervalindex:
            type = stdata.types[2]
        else:
            type = ''
        if row==72:
            subtype = 'Growth/Equity Oriented Schemes'
            type = 'Close Ended Schemes'
        elif name in stdata.subtypesdict.keys():
            subtype = stdata.subtypesdict[name]
        else:
            subtype = ''
        nscheme = 0 if table[row][2] is None or table[row][2].strip() == '-' or table[row][2].strip() == '' else int(table[row][2].replace(',', '').replace(' ', '').replace('#', '').strip())
        nfolios = 0 if table[row][3] is None or table[row][3].strip() == '-' or table[row][3].strip() == '' else int(table[row][3].replace(',', '').replace(' ', '').strip())
        funmob = 0 if table[row][4] is None or table[row][4].strip() == '-' or table[row][4].strip() == '' else float(table[row][4].replace(',', '').replace(' ', '').strip())
        re = 0 if table[row][5] is None or table[row][5].strip() == '-' or table[row][5].strip() == '' else float(table[row][5].replace(',', '').replace(' ', '').strip())
        naum = 0 if table[row][6] is None or table[row][6].strip() == '-' or table[row][6].strip() == '' else float(table[row][6].replace(',', '').replace(' ', '').strip())
        anaum = 0 if table[row][7] is None or table[row][7].strip() == '-' or table[row][7].strip() == '' else float(table[row][7].replace(',', '').replace(' ', '').strip())
        nspc = 0 if table[row][8] is None or table[row][8].strip() == '-' or table[row][8].strip() == '' else int(table[row][8].replace(',', '').replace(' ', '').strip())
        naumsp = 0 if table[row][9] is None or table[row][9].strip() == '-' or table[row][9].strip() == '' else float(table[row][9].replace(',', '').replace(' ', '').strip())
        nio =  funmob - re
        naumps = 0 if table[row][2] is None or table[row][2].strip() == '-' or table[row][2].strip() == '' else naum/nscheme
        niops = 0 if table[row][2] is None or table[row][2].strip() == '-' or table[row][2].strip() == '' else nio/nscheme

        row_data = {
            'Scheme Name': name,
            'Scheme Type': type,
            'Scheme Subtype':  subtype,
            'No. of Schemes': nscheme,
            'No. of Folios': nfolios,
            'Funds Mobilized (INR in crore)': funmob,
            'Repurchase/Redemption (INR in crore)': re,
            'Net Assets Under Management (INR in crore)': naum,
            'Average Net Assets Under Management (INR in crore)': anaum,
            'No. of segregated portfolios created': nspc,
            'Net Assets Under Management in segregated portfolio (INR in crores)': naumsp,
            'Net Inflow or Outflow':  nio,
            'Net Asset under Management per Scheme':  naumps,
            'Net Inflow or Outflow per Scheme':  niops,
            'month and year': tbname
        }
        global df
        df = df._append(row_data, ignore_index=True)
    df.to_csv('mutualfunds.csv', index=False)

if __name__ == "__main__":
    global df
    df = pd.DataFrame(columns=column_headers)

    paths = ['dataset/MF Data - March 2022 - April 2021.pdf', 'dataset/MF Data - March 2023 - April 2022.pdf',
         'dataset/MF Data - March 2024 - April 2023.pdf']

    tables = get_tables(paths[0])
    for tbname in tables:
        #print(tables[tbname], end="\n\n")
        table = tables[tbname]
        add_data_to_dataframe(table, tbname)
'''
    for path in paths:
        for tables in get_tables(path):
            for tbname in tables:
                print(tables[tbname], end="\n\n")
                table = tables[tbname]
                add_data_to_dataframe(table, tbname)
    print(df)
'''
