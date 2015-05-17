#### 文件目录结构

- opera-museum  <--- **django_project**
	- museum	<--- **app**
	- opera_museum	<--- **project 配置文件等**
	- manage.py

- venv
	- 环境配置  

- 数据库
	- 测试环境 db.sqlite3
	-  生产环境 mysql




upstream django {

    server unix:/var/www/opera_museum/mysite.sock;
    #server 127.0.0.1:8001;

}

server {

    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name 121.41.95.216; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {

        alias /var/www/opera_museum/media;  # your Django project's media files - amend as required

    }

    location /static {

        alias /var/www/opera_museum/static; # your Django project's static files - amend as required

    }    
    
    location / {

        uwsgi_pass  django;
        include     /var/www/opera_museum/uwsgi_params; # the uwsgi_params file you installed

    }

}
