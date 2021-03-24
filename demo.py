from datetime import datetime


# # def conversion_time(time):
# #     """转换时间"""
# #     GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800 (CST)'
# #     create_time = datetime.strptime(time, GMT_FORMAT)
# #     print(create_time)
# #     return str(create_time)
#
#
# time = "Mon, 22 Feb 2021 12:03:03 GMT"
#
# # conversion_time(time)
# # GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800 (CST)'
#
# GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
#
# # print(datetime.utcnow().strftime(GMT_FORMAT))
# print(type(datetime.strptime(time, GMT_FORMAT)))


print(datetime(2021, 2, 22, 15, 58, 50))