import wikirepo
from wikirepo.data import lctn_utils, wd_utils
from datetime import date

credentials = wd_utils.login()

ents_dict = wd_utils.EntitiesDict()
country = "Country Name"
depth = 2
sub_lctns = True
timespan = (date(2000,1,1), date(2018,1,1))
interval = 'yearly'

lctns_dict = lctn_utils.gen_lctns_dict()

df = wikirepo.data.query()
df_copy = df.copy()

# The user checks for NaNs and adds data

df_edits = pd.concat([df, df_copy]).drop_duplicates(keep=False)

wikirepo.data.upload(df_edits, credentials)