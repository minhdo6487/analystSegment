import graphlab.aggregate
from getData2FRAME import callLoadData
#from getData2FRAME import getData



sf = callLoadData.initialize()
sf.groupby()
print(sf.column_names())