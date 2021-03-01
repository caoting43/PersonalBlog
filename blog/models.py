from blog import db
from datetime import datetime


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""

    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""

    __tablename__ = "blog_user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    name = db.Column(db.String(32), unique=True, nullable=False)  # 用户暱称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号


class Articles(BaseModel, db.Model):
    """博文表"""

    __tablename__ = "blog_articles"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    aid = db.Column(db.Integer, nullable=False)  # 用户编号
    title = db.Column(db.String(52), nullable=False)  # 标题
    author = db.Column(db.String(10), nullable=False)  # 作者
    content = db.Column(db.TEXT, nullable=False)  # 文章
    img_url = db.Column(db.String(128), nullable=False)  # 图片地址
    label = db.Column(db.String(10), nullable=False)  # 文章标签

    def to_dict(self):
        d = {
            "title": self.title,
            "author": self.author,
            "content": self.content,
            "img_url": self.img_url,
            "label": self.label,
        }
        return d

    def to_list_dict(self):
        d = {
            "aid": self.aid,
            "title": self.title,
            "author": self.author,
            "img_url": self.img_url,
            "label": self.label,
            "create_time": self.create_time,
        }
        return d
