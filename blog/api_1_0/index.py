from . import api
from flask import current_app, request, jsonify
from blog.utils.response_code import RET
from blog import db, models
from blog.models import Articles


@api.route("/get_list_data", mothods=["GET"])
def get_list_data():
    """
    博文列表
    入参：
    :return: aid,title,author,img_url,label,create_time
    """
    art_li = Articles.query.all()
    # print(art_li)
    art_dict_li = []
    for art in art_li:
        print(art.to_dict())
        art_dict_li.append(art.to_list_dict())
    return jsonify(errno=RET.OK, errmsg="ok", data=art_dict_li)


@api.route("/recise_data", mothods=["POST"])
def recise_data():
    """
    博文列表修改
    入参：aid
    :return: title,content,img_url,label
    """
    result = request.form
    try:
        aid = result["aid"]
    except Exception as e:
        return jsonify(errno=RET.PARAMERR, errmsg="缺少参数")

    art_data = Articles(aid=aid)
    try:
        db.session.add(art_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据错误")

    return jsonify(errno=RET.OK, errmsg="OK")


@api.route("/update_data", mothods=["POST"])
def update_data():
    """
    更新数据
    入参：title,content,img_url,label
    :return: ok
    """
    pass


@api.route("/delete_data", mothods=["POST"])
def delete_data():
    """
    删除博文
    入参：label
    :return: ok
    """
    pass


@api.route("/add_data", mothods=["POST"])
def add_data():
    """
    新增博文数据
    入参：title,content,img_url,label
    :return: ok
    """
    pass


@api.route("/get_data", mothods=["GET"])
def get_data():
    """
    主页数据
    入参：
    :return: title，img_url,label
    """
    pass


@api.route("/get_label_data", mothods=["POST"])
def get_label_data():
    """
    标签页博文数据
    入参：label
    :return: title，img_url,label
    """
    pass


@api.route("/get_detailed_data", mothods=["POST"])
def get_detailed_data():
    """
    博文详情数据
    入参：label
    :return: title,author,content,label,create_time
    """
    pass


@api.route("/post_data", methods=["POST"])
def submit_data():
    """
    获取前端提交的数据
    有title、img_url、content、author
    生成aid
    """
    result = request.form
    try:
        title = result["title"]
        author = result["author"]
        content = result["content"]
        img_url = result["img_url"]
    except Exception as e:
        return jsonify(errno=RET.PARAMERR, errmsg="缺少参数")
    # 校验参数
    if not all([title, author, content, img_url]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    art = Articles(aid=2, title=title, author=author, content=content, img_url=img_url)
    try:
        db.session.add(art)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据错误")

    return jsonify(errno=RET.OK, errmsg="OK")


@api.route("/index")
def index():
    """获取所有文章数据"""
    art_li = Articles.query.all()
    # print(art_li)
    art_dict_li = []
    for art in art_li:
        print(art.to_dict())
        art_dict_li.append(art.to_dict())
    return jsonify(errno=RET.OK, errmsg="ok", data=art_dict_li)
