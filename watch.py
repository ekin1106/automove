# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
# class MyHandler(FileSystemEventHandler):
#     def on_created(self, event):
#         if event.src_path == 'D:\\verysync\\':      #监控指定文件内容、权限等变化
#             print ('log file {} changed!'.format(event.src_path))
#
# if __name__ == '__main__':
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path='D:\\verysync\\', recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# from watchdog.events import FileSystemEvent
import watchdog.events


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
            print('{}    modified'.format(event.src_path))

    def on_moved(self,event):
        '''检测文件或文件夹移动事件，此处只针对文件移动进行处理'''
        if not event.is_directory:
            print('{0}    moved to {1}'.format(event.src_path,event.dest_path))




if __name__ == '__main__':
    event_handler = MyHandler()
    observer=Observer()
    observer.schedule(event_handler,path='D:\\verysync',recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
