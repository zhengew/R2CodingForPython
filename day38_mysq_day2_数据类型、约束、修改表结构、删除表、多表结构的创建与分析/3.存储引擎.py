# 存储引擎 -- 存储数据的方式
# 一张表
    # 数据
    # 表的结构
    # 索引(查询的时候使用的一个目录结构)

# Innodb存储引擎    mysql5.6之后的默认的存储引擎
# 数据和索引存储在一起 2个文件
    # 数据索引\表结构
# 数据持久化
# 支持事务   : 为了保证数据的完整性,将多个操作变成原子性操作   : 保持数据安全
# 支持行级锁 : 修改的行少的时候使用                          : 修改数据频繁的操作
# 支持表级锁 : 批量修改多行的时候使用                        : 对于大量数据的同时修改
# 支持外键   : 约束两张表中的关联字段不能随意的添加\删除      : 能够降低数据增删改的出错率


# Myisam存储引擎    mysql5.5之前的默认的存储引擎
# 数据和索引不存储在一起  3个文件
    # 数据\索引\表结构
# 数据持久化
# 只支持表锁

# Memory存储引擎
# 数据存储在内存中, 1个文件
    # 表结构
# 数据断电消失


# 面试题
# 你了解mysql的存储引擎么?
# 你的项目用了什么存储引擎,为什么?
    # innodb
    # 多个用户操作的过程中对同一张表的数据同时做修改
    # innodb支持行级锁,所以我们使用了这个存储引擎
    # 为了适应程序未来的扩展性,扩展新功能的时候可能会用到...,涉及到要维护数据的完整性
    # 项目中有一两张xx xx表,之间的外键关系是什么,一张表的修改或者删除比较频繁,怕出错所以做了外键约束



















