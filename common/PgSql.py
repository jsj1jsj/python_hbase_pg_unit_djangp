## 导入psycopg2包
import psycopg2
def deleteOperate():
    ## 连接到一个给定的数据库
    conn = psycopg2.connect( database="fxjk", user="fxjk", password="83566B9F53810E90", host="10.136.1.69",
                             port="5432" )
    ## 建立游标，用来执行数据库操作
    cursor = conn.cursor()

    ## 执行SQL SELECT命令
    cursor.execute( "delete from customer" )
    cursor.execute( "delete from message" )
    cursor.execute( "delete from transhandle" )
    cursor.execute( "delete from transrulematch" )
    conn.commit()
    ## 获取SELECT返回的元组
    # rows = cursor.fetchall()
    # for row in rows:
    #     print('id = ',row[0], 'name = ', row[1], '\n')

    ## 关闭游标
    cursor.close()

    ## 关闭数据库连接
    conn.close()