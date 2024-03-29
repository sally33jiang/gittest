"""
Django settings for django_demo project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#使用Python的 pathlib 模块，这会将 __file__ 变量的值转换为 Path 对象
BASE_DIR = Path(__file__).resolve().parent.parent    #项目根目录parent 是父级目录 subdir 子文件夹
#  'NAME': BASE_DIR / 'db.sqlite3',


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q5)!b_gume!$3^zv_8yd(4#z*34x74kvll_ndn(t&#(qo=!+u_'
#这是密钥，内部做加密解密处理

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#调试模式打开 用于开发过程  ，false 是上线部署

ALLOWED_HOSTS = ['*']
#被允许的ip主机地址 * 是所有的，通配符  或者指定私有ip也可以 ，指定多个可以写列表

# Application definition


#被安装的app，这里创建了demo_app 需要加进来定义一下 ，防止功能受到限制

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demo_app',
]


#中间件，csrf 做安全拦截，自定义需要注册

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


#根路由的路劲，自己生成的
ROOT_URLCONF = 'django_demo.urls'


#模板 可以配置多个模板，指定模板文件夹 tempplate 可以自动被识别
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#目录
WSGI_APPLICATION = 'django_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


#数据库配置sqlite方便使用，单线程，大型关系的mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',#django.db.backends.mysql指定ip 端口，sqlite3不需要用户名密码
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us' #zh-hans 中文

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


#静态文件 为html服务的
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


# 默认主键字段的类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
