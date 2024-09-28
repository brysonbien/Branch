import pymysql.cursors


connection = pymysql.connect(host='128.61.118.107',
                             port=3306,
                             user='root',
                             password='database123',
                             db='local instance 3306',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)