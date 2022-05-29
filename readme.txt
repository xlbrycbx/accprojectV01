nginx.conf = nginx.conf + default.conf
user 改为 root
location / {
        root  项目路径；
        index  项目首页；
    }

如果80端口被占用，使用fuser -k 80/tcp命令杀掉进程

#启动nginx
nginx -c /srv/staticPage/nginx.conf

#显示nginx状态
ps -aux | grep nginx

#退出nginx
nginx -s quit
nginx -s stop