import pandas as pd


df = pd.read_excel("CRDF-RP-2000-2020.xlsx", sheet_name="All")
df.head()
net = df[(df["Year"]==2010)| (df["Year"]==2020)].copy(deep=True)

net['Provider'].replace({
     "Norwegian Postcode Lottery": "Norway",
    "Charity Projects Ltd (Comic Relief)": "UK",
    "CABEI": "Ireland",
    "BBVA Microfinance Foundation": "Latina America",
    "Gatsby Charitable Foundation": "UK",
    "People's Postcode Lottery": "UK",
    "IFC": "United States",
    "Bezos Earth Fund": "United States",
    "Mastercard Foundation": "Canada",
    "Howard G. Buffett Foundation": "United States",
    "Swedish Postcode Lottery": "Sweden",
    "MAVA Foundation": "Switzerland",
    "McKnight Foundation": "United States",
    "AIIB": "China",
    "Open Society Foundations": "UK",
    "Margaret A. Cargill Foundation": "United States",
    "BelgiumF": "Belgium",
    "Rockefeller Foundation": "China",
    "Grameen Crédit Agricole Foundation": "Luxembourg",
    "AIIB": "China",
    "IsDB": "Saudi Arabia",
    "EBRD": "UK",
    "AsDB": "Philippines",
    "AfDB": "Ivory Coast",
    "GGGI": "South Korea",
    "Dutch Postcode Lottery": "Netherlands",
    "Wallis and Futuna": "New Zealand",
    "Middle Africa, regional": "Africa",
    "Melanesia, regional": "Melanesia",
    "Southern Africa, regional": "South Africa",
    "Eastern Africa, regional": "Africa",
    "Western Africa, regional": "Africa",
    "Democratic People's Republic of Korea": "North Korea",
    "States Ex-Yugoslavia unspecified": "Yugoslavia",
    "Caribbean, regional": "Caribbean",
    "South & Central Asia, regional": "Asia",
    "Central African Republic": "Africa",
    "North of Sahara, regional": "Sahara",
    " Central Asia, regional": "Asia",
    " South Asia, regional": "Asia",
    " China (People's Republic of)": "China",
    "Bernard van Leer Foundation": "Netherlands",
    "Carnegie Corporation of New York": "United States",
    "Conrad N. Hilton Foundation": "United States",
    "H&M Foundation": "Sweden",
    "IDB": "United States",
    "Bill & Melinda Gates Foundation": "United States",
    "Bloomberg Family Foundation": "United States",
    "EU Institutions (excl. EIB)": "United States",
    "CIF": "Belgium",
    "EIB": "Luxembourg",
    "GEF": "United States",
    "WB": "United States",
    "IFAD": "Italy",
    "CAF": "Venezuela",
    "GCF": "Korea",
    "John D. & Catherine T. MacArthur Foundation": "United States",
    "Oak Foundation": "Switzerland",
    "William & Flora Hewlett Foundation": "United States",
    "Charity Projects Ltd (Comic Relief)": "United Kingdom",
    "CIFF": "United Kingdom",
    "David & Lucile Packard Foundation": "United States",
    "FAO": "Italy",
    "Ford Foundation": "United States",
    "IKEA Foundation": "Netherlands",
    "Citi Foundation": "United States",
    "Gordon and Betty Moore Foundation": "United States",
    "Laudes Foundation": "Multilateral",
    "UBS Optimus Foundation": "Switzerland",
    "Adaptation Fund": "Multilateral",
    "Charity Projects Ltd (Comic Relief)": "United Kingdom",
    "Wellcome Trust": "United Kingdom",
    "Korea": "South Korea",
    "United Kingdom": "UK",
    "United States": "USA",
    "EU Institutions (excl. Luxembourg)": "EU"

}, inplace=True)

net['Recipient'].replace({
    "Africa, regional": "Africa",
    "America, regional": "America",
    "Asia, regional": "Asia",
    "Burkina Faso": "Africa",
    "Chad": "Africa",
    "China (People's Republic of)": "China",
    "Democratic Republic of the Congo": "Congo",
    "Europe, regional": "EU",
    "North of Sahara, regional": "Sahara"
}, inplace=True)

net = net[ ( net[ "Provider Type" ] == "DAC member" ) | 
           ( net[ "Provider Type" ] == "Non-DAC member" ) ]
net.shape
net = net[ ( ~ net[ "Recipient" ].str.contains( "unspecified" ) ) & 
           ( ~ net[ "Recipient" ].str.contains( "regional" ) ) ]
net.shape
cols_to_keep = [ 0, 2, 9, 24 ]
cols_to_remove = [ ]
col_names = list( net.columns.values )
for col, name in enumerate( net.columns.values ) :
    if not col in cols_to_keep:
        cols_to_remove.append( col_names[ col ] )
net.drop( columns = cols_to_remove, inplace = True )
net.shape

net.dropna( inplace = True )
net.shape
