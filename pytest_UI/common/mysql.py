'''数据库操作'''
from pytest_UI.config import root_path
class Mysql_Operation(object):
    def __init__(self):
        from pytest_UI.config import Database_config
        import pymysql
        self.cnn = pymysql.connect(**Database_config) # 链接数据库
        self.cur = self.cnn.cursor(pymysql.cursors.DictCursor) # 查询返回类型为字典
    def Database_query(self,query_SQL):
        '''数据库查询'''
        self.cur.execute(query=query_SQL) # 传入查询的SQL语句
        return self.cur.fetchall()
    def Database_SQL(self,SQL):
        '''SQL语句操作'''
        try:
            self.cur.execute(SQL)
        except Exception as e:
            '''把错误写入到mysql日志里面'''
            import logging
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename=root_path+"\logs\mysql_log.txt") # 执行SQL语句如果遇到错误,把错误写到日志里面
            logger = logging.getLogger(__name__)
            logger.error(e)



if __name__ == '__main__':
    Mysql_Operation().Database_SQL('select * from user')
