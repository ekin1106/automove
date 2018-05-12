import shutil,os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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
                    try:
                        shutil.move(full,self.media_dir)
                    except shutil.Error:
                        pass
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

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self,event):
        '''检测文件或文件夹建立事件，此处只针对文件建立进行处理
           在新建文件以后，增加文件分类功能，需try except'''
        if not event.is_directory:# == 'd:\\verysync'
            print('{}   created'.format(event.src_path))

    def on_deleted(self,event):
        '''检测文件或文件夹删除事件，此处只针对文件建立进行处理'''
        if not event.is_directory:
            print('{}   deleted'.format(event.src_path))

    def on_modified(self,event):
        '''检测文件或文件夹修改事件，此处只针对文件修改进行处理'''
        if not event.is_directory:
            file = event.src_path
            category('d:\\download').run(file)
            print('{}    modified'.format(event.src_path))

    def on_moved(self,event):
        '''检测文件或文件夹移动事件，此处只针对文件移动进行处理'''
        if not event.is_directory:
            print('{0}    moved to {1}'.format(event.src_path,event.dest_path))




if __name__ == '__main__':
    path = 'd:\\download'
    event_handler = MyHandler()
    observer=Observer()
    observer.schedule(event_handler,path='d:\\download',recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
