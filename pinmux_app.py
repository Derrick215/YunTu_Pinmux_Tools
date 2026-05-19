import os
import sys
import tkinter as tk
from tkinter import filedialog
import webview

class Api:
    def save_file(self, default_name, content, file_types):
        """Open native save dialog and write file. Returns 'ok' or 'cancel'."""
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)

        types = []
        for ft in file_types:
            types.append((ft['name'], ft['ext']))

        file_path = filedialog.asksaveasfilename(
            parent=root,
            title='导出文件',
            initialfile=default_name,
            defaultextension=types[0][1] if types else '.xls',
            filetypes=types,
        )
        root.destroy()

        if not file_path:
            return 'cancel'

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 'ok'


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
        title='YTM32 引脚配置工具',
        url=html_url,
        width=1400,
        height=900,
        resizable=True,
        min_size=(800, 500),
        js_api=Api(),
    )
    webview.start()


if __name__ == '__main__':
    main()
