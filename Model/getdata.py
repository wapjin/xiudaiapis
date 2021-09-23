from .conmysql import c_mysql
from .get_data import get_data


# 获取指定所有表格数据


def get_table(table, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0"
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 获取未接单表格数据


def get_tableall(table, page, limit, uid):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where  uid='" + str(
        uid) + "'  and ISNULL(send_ctime)>0  and  ISNULL(dtime)>0 order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where  uid='" + str(
        uid) + "'  and ISNULL(send_ctime)>0  and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 获取接单表格数据


def get_tablemyall(table, uid, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where uid='" + str(
        uid) + "' and  ISNULL(send_ctime)<=0 and  ISNULL(dtime)>0 order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where uid='" + str(
        uid) + "' and  ISNULL(send_ctime)<=0 and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_tablemyall_no(table, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(uid)<=0   and  ISNULL(dtime)>0 order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(uid)<=0  and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 采购单列表
def get_tablemyallsd(table, uid, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select *,a.id zid,a.caigou_name from x_order a join x_orders b on a.orderid=b.id and a.uid=" + str(
        uid) + " and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 order by a.id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select *,a.id zid,a.caigou_name from x_order a join x_orders b on a.orderid=b.id and a.uid=" + str(
        uid) + " and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 "
    # sql = "select * from "+str(table)+" where uid='"+str(uid)+"' and  ISNULL(dtime)>0 order by id desc limit "+str((page-1)*limit)+","+str(limit)
    # sql1 = "select * from "+str(table)+" where uid='"+str(uid)+"' and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 管理采购单列表
def get_tablemyallsd2(table, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select *,a.id zid,a.caigou_name caigou_name from x_order a join x_orders b on a.orderid=b.id and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 order by a.id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select *,a.id zid,a.caigou_name caigou_name from x_order a join x_orders b on a.orderid=b.id and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 "
    # sql = "select * from "+str(table)+" where uid='"+str(uid)+"' and  ISNULL(dtime)>0 order by id desc limit "+str((page-1)*limit)+","+str(limit)
    # sql1 = "select * from "+str(table)+" where uid='"+str(uid)+"' and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 获取列表
def get_tablemyalls(table, uid, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where orderid='" + str(
        uid) + "'  and  ISNULL(dtime)>0 order by id desc limit " + str((page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where orderid='" + str(uid) + "'  and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索单号是否重复
def get_orderid(table, uid, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where order_id='" + str(uid) + "' order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where order_id='" + str(uid) + "'"
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索单号是否重复
def get_xiadan(table, uid, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where xiadan_time='" + str(uid) + "' order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where xiadan_time='" + str(uid) + "'"
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索我的采购单
def get_s_myorder(table, uid, order_id, dingding_name, dingding_bumen, dingding_xm, dingding_endtime, dingding_type,
                  xiadan_time, gaizhang_type, fapiao_type, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    where = ""
    if order_id:
        where += " and a.order_id like '%" + order_id + "%'"
    if dingding_name:
        where += " and b.dingding_name like '%" + dingding_name + "%'"
    if dingding_xm:
        where += " and b.dingding_xm like '%" + dingding_xm + "%'"
    if dingding_bumen:
        where += " and b.dingding_bumen like '%" + dingding_bumen + "%'"
    if dingding_type:
        where += " and b.dingding_type='" + dingding_type + "'"
    if dingding_endtime:
        where += " and b.dingding_endtime like '%" + dingding_endtime + "%'"
    if xiadan_time:
        where += " and b.xiadan_time like '%" + xiadan_time + "%'"

    if fapiao_type:
        if fapiao_type == "未签字":
            where += " and (ISNULL(a.fapiao_type)>0 or a.fapiao_type='' or fapiao_type='未签字') "
        else:
            where += " and a.fapiao_type = '" + fapiao_type + "'"

    if gaizhang_type:
        if gaizhang_type == "未审批":
            where += " and (ISNULL(a.gaizhang_type)>0 or a.gaizhang_type='' or  gaizhang_type='未审批')"
        else:
            where += " and a.gaizhang_type = '" + gaizhang_type + "'"

    sql = "select *,a.id zid,a.caigou_name caigou_name from x_order a join x_orders b on a.orderid=b.id and a.uid=" + str(
        uid) + " and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 " + str(where) + " order by a.id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select *,a.id zid,a.caigou_name caigou_name from x_order a join x_orders b on a.orderid=b.id and a.uid=" + str(
        uid) + " and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0  " + str(where)
    print(sql)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索我的采购单
def get_s_myorder_admin(table, order_id, dingding_name, dingding_bumen, dingding_xm, dingding_endtime, dingding_type,
                        xiadan_time, gaizhang_type, fapiao_type, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    where = ""
    if order_id:
        where += " and a.order_id like '%" + order_id + "%'"
    if dingding_name:
        where += " and b.dingding_name like '%" + dingding_name + "%'"
    if dingding_xm:
        where += " and b.dingding_xm like '%" + dingding_xm + "%'"
    if dingding_bumen:
        where += " and b.dingding_bumen like '%" + dingding_bumen + "%'"
    if dingding_type:
        where += " and b.dingding_type='" + dingding_type + "'"
    if dingding_endtime:
        where += " and b.dingding_endtime like '%" + dingding_endtime + "%'"
    if xiadan_time:
        where += " and b.xiadan_time like '%" + xiadan_time + "%'"

    if fapiao_type:
        if fapiao_type == "未签字":
            where += " and (ISNULL(a.fapiao_type)>0 or a.fapiao_type='' or fapiao_type='未签字') "
        else:
            where += " and a.fapiao_type = '" + fapiao_type + "'"

    if gaizhang_type:
        if gaizhang_type == "未审批":
            where += " and (ISNULL(a.gaizhang_type)>0 or a.gaizhang_type='' or  gaizhang_type='未审批')"
        else:
            where += " and a.gaizhang_type = '" + gaizhang_type + "'"

    sql = "select *,a.id zid,a.caigou_name caigou_name from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 " + str(
        where) + " order by a.id desc limit " + str((page - 1) * limit) + "," + str(limit)
    sql1 = "select *,a.id zid,a.caigou_name caigou_name from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0  " + str(
        where)
    print(sql)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_all_order1(name, page, limit, s, uid):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # where =" and  concat( IFNULL(b.dingding_name,''), IFNULL(b.dingding_xm,''), IFNULL(b.dingding_bumen,''), IFNULL(b.typess,''), IFNULL(b.typess_body,''), IFNULL(b.typess_name,''), IFNULL(b.sfr,''), IFNULL(b.sfdz,''), IFNULL(b.bz,''), IFNULL(b.canpin_name,''), IFNULL(b.canpin_guige,''), IFNULL(b.caigou_name,'') ) LIKE '%"+name+"%'"

    # sql = "select *,a.id zid from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 "+str(where)+" order by a.id desc limit "+str((page-1)*limit)+","+str(limit)
    # sql1 = "select *,a.id zid from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0  "+str(where)
    w = " "
    if s == "all":
        # 搜索所有采购申请单
        pass
    if s == "end":
        # 搜索所有已接单的采购申请单
        w += " and uid= '" + str(uid) + "'"

    if s == "start":
        # 搜索所有未接单的采购申请单
        w += " and ISNULL(b.uid)>0 "
    print(s)
    sql = """
    SELECT
  *
FROM
  x_orders b
where   
  concat(
    IFNULL( b.dingding_name, '' ),
    IFNULL( b.dingding_xm, '' ),
    IFNULL( b.dingding_bumen, '' ),
    IFNULL( b.typess, '' ),
    IFNULL( b.typess_body, '' ),
    IFNULL( b.typess_name, '' ),
    IFNULL( b.sfr, '' ),
    IFNULL( b.sfdz, '' ),
    IFNULL( b.bz, '' ),
    IFNULL( b.canpin_name_f, '' ),
    IFNULL( b.canpin_guige_f, '' ),
    IFNULL( b.caigou_name, '' ) 
  ) LIKE '%""" + name + """%' """ + str(w) + """
ORDER BY
  b.id DESC
    limit 
    """ + str((page - 1) * limit) + "," + str(limit)
    sql1 = """
    SELECT
  *
FROM
  x_orders b
where   
  concat(
    IFNULL( b.dingding_name, '' ),
    IFNULL( b.dingding_xm, '' ),
    IFNULL( b.dingding_bumen, '' ),
    IFNULL( b.typess, '' ),
    IFNULL( b.typess_body, '' ),
    IFNULL( b.typess_name, '' ),
    IFNULL( b.sfr, '' ),
    IFNULL( b.sfdz, '' ),
    IFNULL( b.bz, '' ),
    IFNULL( b.canpin_name_f, '' ),
    IFNULL( b.canpin_guige_f, '' ),
    IFNULL( b.caigou_name, '' ) 
  ) LIKE '%""" + name + """%'""" + str(w)
    print(sql)

    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_all_order1s(name, page, limit, uid):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # where =" and  concat( IFNULL(b.dingding_name,''), IFNULL(b.dingding_xm,''), IFNULL(b.dingding_bumen,''), IFNULL(b.typess,''), IFNULL(b.typess_body,''), IFNULL(b.typess_name,''), IFNULL(b.sfr,''), IFNULL(b.sfdz,''), IFNULL(b.bz,''), IFNULL(b.canpin_name,''), IFNULL(b.canpin_guige,''), IFNULL(b.caigou_name,'') ) LIKE '%"+name+"%'"

    # sql = "select *,a.id zid from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 "+str(where)+" order by a.id desc limit "+str((page-1)*limit)+","+str(limit)
    # sql1 = "select *,a.id zid from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0  "+str(where)

    sql = """
    SELECT
  *
FROM
  x_orders b
where   
  concat(
    IFNULL( b.dingding_name, '' ),
    IFNULL( b.dingding_xm, '' ),
    IFNULL( b.dingding_bumen, '' ),
    IFNULL( b.typess, '' ),
    IFNULL( b.typess_body, '' ),
    IFNULL( b.typess_name, '' ),
    IFNULL( b.sfr, '' ),
    IFNULL( b.sfdz, '' ),
    IFNULL( b.bz, '' ),
    IFNULL( b.canpin_name_f, '' ),
    IFNULL( b.canpin_guige_f, '' ),
    IFNULL( b.caigou_name, '' ) 
  ) LIKE '%""" + name + """%' and uid='""" + str(uid) + """'
 ORDER BY
  b.id DESC
    limit 
    """ + str((page - 1) * limit) + "," + str(limit)
    sql1 = """
    SELECT
  *
FROM
  x_orders b
where   
  concat(
    IFNULL( b.dingding_name, '' ),
    IFNULL( b.dingding_xm, '' ),
    IFNULL( b.dingding_bumen, '' ),
    IFNULL( b.typess, '' ),
    IFNULL( b.typess_body, '' ),
    IFNULL( b.typess_name, '' ),
    IFNULL( b.sfr, '' ),
    IFNULL( b.sfdz, '' ),
    IFNULL( b.bz, '' ),
    IFNULL( b.canpin_name_f, '' ),
    IFNULL( b.canpin_guige_f, '' ),
    IFNULL( b.caigou_name, '' ) 
  ) LIKE '%""" + name + """%' and  uid='""" + str(uid) + """'"""
    print(sql)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_all_order2(name, page, limit, gaizhang_type, fapiao_type):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    where = " "
    if gaizhang_type:
        if gaizhang_type == "已审批":
            where += " and a.gaizhang_type='" + gaizhang_type + "'"
        elif gaizhang_type == "未审批":
            where += " and a.gaizhang_type=''"
    if fapiao_type:
        if fapiao_type == "已签字":
            where += " and fapiao_type='" + fapiao_type + "'"
        elif fapiao_type == "未签字":
            where += " and a.fapiao_type=''"
    if name:
        where += """ and  concat(
            IFNULL(a.order_id, ''),
            IFNULL(b.dingding_bumen, '' ),
            IFNULL(b.dingding_name, '' ),
		    IFNULL(a.wuliao_lei, ''),
		    IFNULL(a.canpin_name, ''),
		    IFNULL(a.canpin_guige, ''),
		    IFNULL(a.canpin_pinpai, ''),
		    IFNULL(a.canpin_danwei, ''),
		    IFNULL(a.canpin_shu, ''),
		    IFNULL(a.canpin_danjia, ''),
		    IFNULL(a.canpin_shuilv, ''),
		    IFNULL(a.canpin_zongjia, ''),
		    IFNULL(a.canpin_endtime, ''),
		    IFNULL(a.caigou_name, ''),
		    IFNULL(a.gonghuo_name, ''),
		    IFNULL(a.gonghuo_danwe, ''),
		    IFNULL(a.gonghuo_itel, ''),
		    IFNULL(a.gonghuo_gtel, ''),
		    IFNULL(a.gonghuo_dizhi, ''),
		    IFNULL(a.gonghuo_cz, ''),
		    IFNULL(a.hetong_endtime, ''),
		    IFNULL(a.fukan_fangshi, ''),
		    IFNULL(a.kaipiao_time, ''),
		    IFNULL(a.fapiao_hao, ''),
		    IFNULL(a.yufu_kuan, ''),
		    IFNULL(a.yufu_time, ''),
		    IFNULL(a.zhongqi_kuan, ''),
		    IFNULL(a.zhongqi_time, ''),
		    IFNULL(a.yukuan, ''),
		    IFNULL(a.yukuan_time, ''),
		    IFNULL(a.gaizhang_type, ''),
		    IFNULL(a.fapiao_type, ''),
		    IFNULL(a.fujian_url, '')
	    ) LIKE '%""" + name + """%'"""

    sql = "select *,a.id zid,a.caigou_name  from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 " + str(
        where) + " order by a.id desc limit " + str((page - 1) * limit) + "," + str(limit)
    sql1 = "select *,a.id zid,a.caigou_name from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0  " + str(
        where)
    print(sql)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_all_order2s(name, page, limit, uid, gaizhang_type, fapiao_type):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    where = " "
    if gaizhang_type:
        if gaizhang_type == "已审批":
            where += " and a.gaizhang_type='" + gaizhang_type + "'"
        elif gaizhang_type == "未审批":
            where += " and a.gaizhang_type=''"
    if fapiao_type:
        if fapiao_type == "已签字":
            where += " and a.fapiao_type='" + fapiao_type + "'"
        elif fapiao_type == "未签字":
            where += " and a.fapiao_type=''"
    if name:
        where += """ and  concat(
            IFNULL(a.order_id, ''),
            IFNULL(b.dingding_xm, '' ),
            IFNULL(b.dingding_name, '' ),
            IFNULL(b.dingding_bumen, '' ),
    		IFNULL(a.wuliao_lei, ''),
    		IFNULL(a.canpin_name, ''),
    		IFNULL(a.canpin_guige, ''),
    		IFNULL(a.canpin_pinpai, ''),
    		IFNULL(a.canpin_danwei, ''),
    		IFNULL(a.canpin_shu, ''),
    		IFNULL(a.canpin_danjia, ''),
    		IFNULL(a.canpin_shuilv, ''),
    		IFNULL(a.canpin_zongjia, ''),
    		IFNULL(a.canpin_endtime, ''),
    		IFNULL(a.caigou_name, ''),
    		IFNULL(a.gonghuo_name, ''),
    		IFNULL(a.gonghuo_danwe, ''),
    		IFNULL(a.gonghuo_itel, ''),
    		IFNULL(a.gonghuo_gtel, ''),
    		IFNULL(a.gonghuo_dizhi, ''),
    		IFNULL(a.gonghuo_cz, ''),
    		IFNULL(a.hetong_endtime, ''),
    		IFNULL(a.fukan_fangshi, ''),
    		IFNULL(a.kaipiao_time, ''),
    		IFNULL(a.fapiao_hao, ''),
    		IFNULL(a.yufu_kuan, ''),
    		IFNULL(a.yufu_time, ''),
    		IFNULL(a.zhongqi_kuan, ''),
    		IFNULL(a.zhongqi_time, ''),
    		IFNULL(a.yukuan, ''),
    		IFNULL(a.yukuan_time, ''),
    		IFNULL(a.gaizhang_type, ''),
    		IFNULL(a.fapiao_type, ''),
    		IFNULL(a.fujian_url, '')
    	) LIKE '%""" + name + """%'"""

    where += " and a.uid='" + str(uid) + "' "
    sql = "select *,a.id zid,a.caigou_name  from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 " + str(
        where) + " order by a.id desc limit " + str((page - 1) * limit) + "," + str(limit)
    sql1 = "select *,a.id zid,a.caigou_name  from x_order a join x_orders b on a.orderid=b.id  and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0  " + str(
        where)
    print(sql)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索未接单的采购单
def get_s_order(table, order_id, dingding_name, dingding_bumen, dingding_xm, dingding_endtime, dingding_type,
                xiadan_time, page, limit):
    where = ""
    if order_id:
        where += " and order_id like '%" + order_id + "%'"
    if dingding_name:
        where += " and dingding_name like '%" + dingding_name + "%'"
    if dingding_xm:
        where += " and dingding_xm like '%" + dingding_xm + "%'"
    if dingding_bumen:
        where += " and dingding_bumen like '%" + dingding_bumen + "%'"
    if dingding_type:
        where += " and dingding_type='" + dingding_type + "'"
    if dingding_endtime:
        where += " and dingding_endtime like '%" + dingding_endtime + "%'"
    if xiadan_time:
        where += " and xiadan_time like '%" + xiadan_time + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(uid)>0  and  ISNULL(dtime)>0 " + str(
        where) + "  order by id desc limit " + str((page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(uid)>0 and  ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索所有的采购单
def get_s_allorder(table, order_id, dingding_name, dingding_bumen, dingding_xm, dingding_endtime, dingding_type,
                   xiadan_time, page, limit):
    where = ""
    if order_id:
        where += " and order_id like '%" + order_id + "%'"
    if dingding_name:
        where += " and dingding_name like '%" + dingding_name + "%'"
    if dingding_xm:
        where += " and dingding_xm like '%" + dingding_xm + "%'"
    if dingding_bumen:
        where += " and dingding_bumen like '%" + dingding_bumen + "%'"
    if dingding_type:
        where += " and dingding_type='" + dingding_type + "'"
    if dingding_endtime:
        where += " and dingding_endtime like '%" + dingding_endtime + "%'"
    if xiadan_time:
        where += " and xiadan_time like '%" + xiadan_time + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where  ISNULL(dtime)>0 " + str(where) + "  order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where   ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索用户

def get_suser(table, gonghao, name, ziwei, page, limit, names):
    where = ""
    if gonghao:
        where += " and gonghao = '" + gonghao + "'"
    if name:
        where += " and name like '%" + name + "%'"
    if names:
        where += " and name = '" + names + "'"
    if ziwei:
        where += " and ziwei = '" + ziwei + "'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 根据id获取用户
def get_suser2(table, uid):
    where = ""
    if uid:
        where += " and id = '" + uid + "'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id "
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 根据id获取
def get_suser22(table, uid):
    where = ""
    if uid:
        where += " and orderid = '" + uid + "'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id "
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索统一的基础

def all_s_list(table, name, page, limit):
    where = ""
    if name:
        where += " and name like '%" + name + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索统一的基础

def all_s_list1(table, name, page, limit):
    where = ""
    if name:
        where += " and name = '" + name + "'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索供货单位信息

def danwei_s_list(table, gonghuo_danwe, gonghuo_name, gonghuo_itel, gonghuo_dizhi, page, limit):
    where = ""
    if gonghuo_danwe:
        where += " and gonghuo_danwe like '%" + gonghuo_danwe + "%'"
    if gonghuo_name:
        where += " and gonghuo_name like '%" + gonghuo_name + "%'"
    if gonghuo_itel:
        where += " and gonghuo_itel like '%" + gonghuo_itel + "%'"
    if gonghuo_dizhi:
        where += " and gonghuo_dizhi like '%" + gonghuo_dizhi + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 搜索供货单位信息

def danwei_s_list1(table, gonghuo_danwe, gonghuo_name, gonghuo_itel, gonghuo_dizhi, page, limit):
    where = ""
    if gonghuo_danwe:
        where += " and gonghuo_danwe = '" + gonghuo_danwe + "'"
    if gonghuo_name:
        where += " and gonghuo_name like '%" + gonghuo_name + "%'"
    if gonghuo_itel:
        where += " and gonghuo_itel like '%" + gonghuo_itel + "%'"
    if gonghuo_dizhi:
        where += " and gonghuo_dizhi like '%" + gonghuo_dizhi + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where) + "  order by id desc limit " + str(
        (page - 1) * limit) + "," + str(limit)
    sql1 = "select * from " + str(table) + " where ISNULL(dtime)>0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 获取统计数据 yufu_time zhongqi_time yukuan_time
def get_tongji(table, yers, finds):
    where = ""

    # where += " and "+str(finds)+" like '%"+yers+"%' "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(uid)=0 " + str(where)
    sql1 = "select * from " + str(table) + " where ISNULL(uid)=0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_dels(table, where):
    # where += " and "+str(finds)+" like '%"+yers+"%' "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where " + str(where)
    sql1 = "select * from " + str(table) + " where " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 反获取项目名
def getid(table, id):
    where = ""

    where += "  id = '" + str(id) + "' "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where " + str(where)
    sql1 = "select * from " + str(table) + " where  " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 获取统计数据
def get_tongjigg(table):
    where = ""

    where += " and ISNULL(dtime)>0 "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(uid)=0 " + str(where)
    sql1 = "select * from " + str(table) + " where ISNULL(uid)=0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_tongjis(table, yers, finds, xm_name, g):
    where = ""
    print(xm_name)
    print(g)
    where += " and " + str(finds) + " like '%" + yers + "%' "
    where += " and " + g + " = '" + str(xm_name) + "' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where ISNULL(uid)=0 " + str(where)
    sql1 = "select * from " + str(table) + " where ISNULL(uid)=0 " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


def get_orders(table,ids):
    where = ""


    where += " id = '" + str(ids) + "' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where " + str(where)
    sql1 = "select * from " + str(table) + " where " + str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)