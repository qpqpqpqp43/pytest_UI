import yaml
'''读yaml格式的用例'''
from pytest_UI.config import root_path
class Yaml_read_or_writer(object):
    def __init__(self,file_path):
        '''传入读取文件地址为实例属性'''
        from yaml import load, dump
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper
        self.file_path = file_path
        self.Loader = Loader
        self.Dumper = Dumper
        self.load = load
        self.dump = dump
    def read_yaml(self):
        '''读yaml文件'''
        try:
            with open(self.file_path,'r',encoding='utf8') as f:
                data = self.load(f,Loader=self.Loader)
                return data
        except Exception as e:
            '''写入错误日志'''
            import logging
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                filename=root_path + r"\logs\read_or_writer_yaml_log.txt")  # 执行SQL语句如果遇到错误,把错误写到日志里面
            logger = logging.getLogger(__name__)
            logger.error(e)
    def writer_yaml(self,data):
        '''data写入yaml文件'''
        try:
            with open(self.file_path,'w',encoding='utf8') as f:
                out_put = self.dump(data=data,Dumper=self.Dumper,allow_unicode=True)
                f.write(out_put)
        except Exception as e:
            '''写入错误日志'''
            import logging
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                filename=root_path + r"\logs\read_or_writer_yaml_log.txt")  # 执行SQL语句如果遇到错误,把错误写到日志里面
            logger = logging.getLogger(__name__)
            logger.error(e)


if __name__ == '__main__':
    Yaml_read_or_writer('F:\pythonProject5\pytest_UI\data\writer_test.yaml').writer_yaml([{'name':'攀哥'}]) # 测试写入
    print(Yaml_read_or_writer('F:\pythonProject5\pytest_UI\data\writer_test.yaml').read_yaml()) # 测试读出