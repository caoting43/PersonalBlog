from . import api
from flask import current_app, request, jsonify, make_response
from blog.utils.response_code import RET
from blog import db, models
from blog.models import Articles


@api.route("/get_list_data", methods=["GET"])
def get_list_data():
    """
    博文列表
    入参：
    :return: id,title,author,img_url,label,create_time
    """
    art_li = Articles.query.all()
    # print(art_li)
    art_dict_li = []
    for art in art_li:
        print(art.to_list_dict())
        art_dict_li.append(art.to_list_dict())
    response = make_response(jsonify(code=RET.OK, errmsg="ok", data=art_dict_li))
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response


@api.route("/recise_data", methods=["GET"])
def recise_data():
    """
    博文列表修改按钮
    入参：id
    :return: title,content,img_url,label
    """

    try:
        id = request.args.get("id")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.PARAMERR, errmsg="缺少参数")

    try:
        art_data = Articles.query.get(id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.DATAERR, errmsg="数据错误")

    return jsonify(code=RET.OK, errmsg="OK", data=art_data.to_revise_dict())


@api.route("/update_data", methods=["POST"])
def update_data():
    """
    更新数据
    入参：title,content,img_url,label
    :return: ok
    """
    result = request.form
    try:
        id = result["id"]
        title = result["title"]
        content = result["content"]
        img_url = result["img_url"]
        label = result["label"]
    except Exception as e:
        return jsonify(code=RET.PARAMERR, errmsg="缺少参数")
    # 校验参数
    if not all([id, title, content, img_url, label]):
        return jsonify(code=RET.PARAMERR, errmsg="参数不完整")

    art = Articles.query.get(id)
    art.aid = id
    art.title = title
    art.content = content
    art.img_url = img_url
    art.label = label

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(code=RET.DATAERR, errmsg="数据错误")

    return jsonify(code=RET.OK, errmsg="成功修改")


@api.route("/delete_data", methods=["POST"])
def delete_data():
    """
    删除博文
    入参：label
    :return: ok
    """
    result = request.form
    try:
        id = result["id"]
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.PARAMERR, errmsg="缺少参数")
    art = Articles.query.get(id)
    try:
        db.session.delete(art)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.DATAERR, errmsg="数据错误")

    return jsonify(code=RET.OK, errmsg="删除成功")


@api.route("/add_data", methods=["POST"])
def add_data():
    """
    新增博文数据
    入参：title,content,img_url,label
    :return: ok
    """
    result = request.form
    try:
        title = result["title"]
        author = result["author"]
        content = result["content"]
        img_url = result["img_url"]
        label = result["label"]
    except Exception as e:
        response = make_response(jsonify(code=RET.PARAMERR, errmsg="缺少参数"))
        response.headers["Access-Control-Allow-Origin"] = '*'
        return response
    # 校验参数
    if not all([title, author, content, img_url]):
        response = make_response(jsonify(code=RET.PARAMERR, errmsg="参数不完整"))
        response.headers["Access-Control-Allow-Origin"] = '*'
        return response

    art = Articles(title=title, author=author, content=content, img_url=img_url, label=label)
    try:
        db.session.add(art)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        response = make_response(jsonify(code=RET.DATAERR, errmsg="数据错误"))
        response.headers["Access-Control-Allow-Origin"] = '*'
        return response

    response = make_response(jsonify(code=RET.OK, errmsg="新增一条数据"))
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response


@api.route("/get_data", methods=["GET"])
def get_data():
    """
    主页数据
    入参：
    :return: title，img_url,label
    """
    art_li = Articles.query.all()
    # print(art_li)
    art_dict_li = []
    for art in art_li:
        print(art.to_dict())
        art_dict_li.append(art.to_dict())
    return jsonify(code=RET.OK, errmsg="ok", data=art_dict_li)


@api.route("/get_label_data", methods=["GET"])
def get_label_data():
    """
    标签页博文数据
    入参：label
    :return: title，img_url,label
    """
    try:
        label = request.args.get("label")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.PARAMERR, errmsg="缺少参数")

    try:
        art_list = Articles.query.filter_by(label=label)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.DATAERR, errmsg="数据错误")
    art_data_list = []
    for i in art_list:
        print(i.to_label_dict())
        art_data_list.append(i.to_label_dict())

    return jsonify(code=RET.OK, errmsg="OK", data=art_data_list)


@api.route("/get_detailed_data", methods=["GET"])
def get_detailed_data():
    """
    博文详情数据
    入参：label
    :return: title,author,content,label,create_time
    """
    try:
        id = int(request.args.get("id"))
        label = request.args.get("label")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.PARAMERR, errmsg="缺少参数")

    try:
        art_list = Articles.query.filter(Articles.id == id, Articles.label == label)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(code=RET.DATAERR, errmsg="数据错误")

    return jsonify(code=RET.OK, errmsg="OK", data=art_list[0].to_detailed_dict())
