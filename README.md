# RedLab Django App

**Log-in to server:**

```shell
ssh <USER>@redlab-dev.napier.ac.uk
```

**Update apt-get:**

```shell
sudo apt-get update
```

**App Location:**

`/var/local/django_cms_app` , as well as in `40223535/django_cms_app`.

**To run the app manually from the project folder (without NginX nor uWSGI):**

```shell
. env/bin/activate
sudo $(which python) manage.py runserver 0:80
```

**Hard restart nginx:**

```shell
sudo systemctl stop nginx.service
sudo systemctl start nginx.service
```

**Check error log (if needed):**

```shell
tail -f /var/log/nginx/error.log
```

**nginx.conf (~/django_cms_app/nginx.conf):**

```shell
upstream django {
        server unix:///home/40223535/django_cms_app/django_cms_app.sock; # for a file socket
        # server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

server {
        listen 80;
        server_name redlab-dev.napier.ac.uk;
        charset utf-8;

        location /static {
                alias /home/40223535/django_cms_app/static;
        }

        location / {
                uwsgi_pass django;
                include /home/40223535/django_cms_app/uwsgi_params;
        }
}
```

**Run app using uwsgi and nginx:**

```shell
sudo $(which uwsgi) --socket django_cms_app.sock --module django_cms_app/django_cms_app.wsgi --chmod-socket=664
```
