#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# 启动 python manage.py runserver ip:80000  多人开发 局域网可以协作使用，或者购买服务器部署上线
#makemiragrations 生成执行文件和 启动执行迁移文件去迁移  migrations  迁移就是将模型映射到数据库
#每个应用里默认有mirgrations ，所以不需要初始化文件夹
#新建db 找到本地文件 链接数据库，查看main文件，可以看到数据库的结构


#

