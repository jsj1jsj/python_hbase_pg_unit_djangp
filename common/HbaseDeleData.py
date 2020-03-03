import happybase
def deleteHbase():
    connection = happybase.Connection(host='10.136.1.37', port=9090)
    table_name_list = connection.tables()
    print( table_name_list )
    connection.disable_table(b'new_ALL_TRADE_HISTORY')
    connection.delete_table(b'new_ALL_TRADE_HISTORY')
    print( "11" )
    table_name_list = connection.tables()
    print( table_name_list )
    connection.create_table('new_ALL_TRADE_HISTORY', {'mtrad':dict(), 'TTL':dict(), 'SNAPPY':dict()})
    print("11")
    table_name_list = connection.tables()
    print( table_name_list )

if __name__ == "__main__":
    b = deleteHbase()
