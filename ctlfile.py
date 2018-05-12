import shutil,os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time

class category():
    def __init__(self,folder_name):
        self.folder_name = folder_name
        self.pic = ['.jpg','.bmp','.gif','.png','.jpeg','.jpg_orig']
        self.media = ['.mp3','.mp4','.mkv','.3gp','.avi','.m2ts','.ts','.flv','.rmvb','.rm','.srt','.ssa','.mpg','.mp41','.webm','.ogg','.tp','.m2t','.wma','.mov','.m4a','.m3u8','.wmv','.ass','.f4v','.mka']
        self.doc = ['.pdf','.txt','.mobi','.doc','.docx','.xlsx']
        self.compression = ['.zip','.rar','.7z','.zip','.iso','.whl','.tar','.gz','bz2','.z01','.z02','.z03','.z04','.z05','.pkg','.deb','.bin','.bz2','.tgz']
        self.executable = ['.exe','.apk','.msi','.sh']
        self.bt = ['.torrent']
        '''目录分类'''
        self.pic_dir = u'D:\\download\\图片'
        self.media_dir = u'D:\\download\\视频音乐'
        self.doc_dir = u'D:\\download\\文档'
        self.com_dir = u'D:\\download\\压缩文件'
        self.exe_dir = u'D:\\download\\程序'
        self.bt_dir = u'D:\\download\\torrent'
    def cate_file(self):
        '''分类移动'''
        scan_dir = os.listdir(self.folder_name)
        '''遍历目录下所有的文件和文件夹生成列表'''
        return scan_dir

    def run(self,file):
        full = os.path.join(self.folder_name,file)
        '''os.path.isfile的判断需要使用绝对路径,os.path.join添加路径'''
        suffix = os.path.splitext(file)[1].lower()
        '''将文件名和后缀分离,所有的后缀强制小写'''
        if os.path.isfile(full):
            '''判断是否为文件，是则判断后缀，然后分类'''
            try:
                if suffix in self.pic:
                    shutil.move(full,self.pic_dir)
                    print(file,'>>>>moving to {}<<<<'.format(self.pic_dir))
                elif suffix in self.media:
                    shutil.move(full,self.media_dir)
                    print(file,'>>>>moving to {}<<<<'.format(self.media_dir))
                elif suffix in self.doc:
                    shutil.move(full,self.doc_dir)
                    print(file,'>>>>moving to {}<<<<'.format(self.doc_dir))
                elif suffix in self.compression:
                    shutil.move(full,self.com_dir)
                    print(file,'>>>>moving to {}<<<<'.format(self.com_dir))
                elif suffix in self.executable:
                    shutil.move(full,self.exe_dir)
                    print(file,'>>>>moving to {}<<<<'.format(self.exe_dir))
                elif suffix in self.bt:
                    shutil.move(full,self.bt_dir)
                    print(file,'>>>>moving to {}<<<<'.format(self.bt_dir))
            except:
                pass

    # def temp_save(self,path):
    #     scan_dir = os.listdir(path)
    #     list_suf = []
    #     for file in scan_dir:
    #         full = os.path.join(path,file)
    #         suffix = os.path.splitext(file)[1].lower()
    #         if os.path.isfile(full):
    #             list_suf.append(suffix)
    #     l = set(list_suf)
    #     with open('d:\\verysync\\suf.txt','w') as f:
    #         f.write(repr(l))
                #repr转化列表成string，写入文件
    #         f.close()

if __name__ == '__main__':
    path = 'd:\\download'
    cat = category(path)
    start = time.clock()
    pool = ThreadPool(10)
    pool.map(cat.run,cat.cate_file())
    pool.close()
    pool.join()
    end = time.clock()
    print(end-start)
