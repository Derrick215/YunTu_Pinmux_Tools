import os
import sys
import webview

def get_html_path():
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'index.html')

def main():
    html_path = get_html_path()
    html_url = f'file:///{html_path.replace(os.sep, "/")}'

    webview.create_window(
        title='云途 YTM32 引脚配置工具',
        url=html_url,
        width=1400,
        height=900,
        resizable=True,
        min_size=(800, 500),
    )
    webview.start()

if __name__ == '__main__':
    main()
