# basic

这是基于FastAPI和Tortoise ORM实现的一个web后端框架，结构简单，功能强大，扩展性强。

```bash
app目录下有extensions和modules，extensions下的是功能模块，modules下的模块是业务模块。
modules下的base是一些封装好的基类，user模块是一个示例，包含models（ORM），resources（接口），schemas（基于pydantic实现实例的序列化和反序列化），validations（声明枚举）。
可根据user模块快速新增其他模块进行开发。
```

### 建表、更新表结构
```bash
# 默认已经创建好数据库 temp_00(create database temp_00 charset=utf8mb4)
# aerich会根据模块中声明的model在数据库映射出表结构（https://tortoise.github.io/migration.html?h=migrate）
# 建表
aerich init -t app.extensions.mysql.TORTOISE_ORM 
aerich init-db
# 更新表结构
aerich migrate --name update
aerich upgrade
```

### run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# 修改config文件的MYSQL_URL和REDIS_URL
# 启动
uvicorn wsgi:app --host 0.0.0.0 --port 8080 --workers 2
```

### API
```bash
http://127.0.0.1:8080/docs
```