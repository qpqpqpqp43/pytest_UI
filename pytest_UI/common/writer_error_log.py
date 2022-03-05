'''写错误日志'''
class Writer_log():
    def __init__(self,e,file_path):
        '''
        :param e: 程序报错的内容
        :param file_path: 保存日志的文件路径
        '''
        import logging
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename=rf"{file_path}") # 执行SQL语句如果遇到错误,把错误写到日志里面
        logger = logging.getLogger(__name__)
        logger.error(e)
        

if __name__ == '__main__':
    Writer_log(e='313131',file_path='F:\pythonProject5\pytest_UI\logs\dwd.txt')