import pymysql

# 重写 django自带的 install_as_MySQLdb() 方法
pymysql.install_as_MySQLdb()