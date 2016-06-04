#coding:utf-8
from blog import blog
from blog import config
blog.config.from_object(config)
blog.run(debug = True, port=5000)