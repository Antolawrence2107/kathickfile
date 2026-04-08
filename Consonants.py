import datetime 
def get_datetime():
    dt1 = datetime.datetime.now()
    return dt1.strftime("%d %B, %Y")
monthstr = get_datetime()
urlapi= '/data/url'
ERRORNOTIFICATIONARN = '/data/errorarn' 
SUCCESSNOTIFICATIONARN='/data/successarn'
COMPONENT_NAME = 'STOCK_DATA_EXTRACT'
ERROR_MSG = f'NEED ATTENTION ****API ERROR /KEY EXPIRED ** ON {monthstr} ******'
SUCCESS_MSG = f'SUCCESSFULLY EXTRACTED  FILES FOR {monthstr}***'
SUCCESS_DESCRIPTION='SUCCESS'
ENVIRONMENT = '/data/dev'