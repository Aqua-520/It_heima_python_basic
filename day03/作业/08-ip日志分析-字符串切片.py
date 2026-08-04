# 【题目】
# 已知某服务的访问日志字符串：(字符串结构: "IP|页面访问路径|访问耗时(ms)")
# log = "192.168.1.100|/home|12; 10.0.0.55|/login|5; 192.168.1.100|/products|45; 172.16.3.20|/home|8; 10.0.0.55|/cart|33; 192.168.1.100|/login|7; 172.16.3.20|/products|29; 10.0.0.55|/home|6"
# blacklist = {"10.0.0.55", "192.168.1.100"}
#
# 请依次完成（不使用函数）：
# 1. 使用 split("; ") 将日志切割成列表 records
# 2. 遍历 records，收集所有 IP 地址到列表 ip_list
# 3. 使用集合获取所有去重后的访问页面路径
# 4. 使用集合推导式从 ip_list 中筛选出属于黑名单的 IP，生成 visited_black_ips(实际日志中包含的黑名单中的IP)
# 5. 计算黑名单 IP 的总访问次数
# 6. 找出响应时间大于 30ms 的记录所在的页面路径


# 访问日志字符串
log = "192.168.1.100|/home|12; 10.0.0.55|/login|5; 192.168.1.100|/products|45; 172.16.3.20|/home|8; 10.0.0.55|/cart|33; 192.168.1.100|/login|7; 172.16.3.20|/products|29; 10.0.0.55|/home|6"

# IP黑名单判定规则列表
blacklist = {"10.0.0.55", "192.168.1.100", "10.7.0.9"}

# 1. 使用 split("; ") 将日志切割成列表 records
records = log.split('; ')
print(f"records日志成功切割：{records}")

# 2. 遍历 records，收集所有 IP 地址到列表 ip_list
# 3. 使用集合获取所有去重后的访问页面路径

# 切好的iplist
ip_list = []
# 做对路径去重的集合
path_set = set()

for log_item in records:
    # 先对每个字符串做去除前后空格的操作,链式调用
    current_list = log_item.strip().split('|')
    # print(current_list)
    # 再将每一个一号位添入ip_list
    ip_list.append(current_list[0])
    path_set.add(current_list[1])

# 成功将ip地址切割出来
print(f"访问过的ip切割记录结果：{ip_list}")
print(f"对访问路径的去重结果：{path_set}")

# 4. 使用集合推导式从 ip_list 中筛选出属于黑名单的 IP，生成 visited_black_ips(实际日志中包含的黑名单中的IP)
# 查找两个的交集，中间那一块大家都有的
visited_black_ips = {ip for ip in ip_list if ip  in blacklist} # 集合推导式子
print(f"访问了哪些黑名单ip：{visited_black_ips}")

# 5. 计算黑名单 IP 的总访问次数
total = 0
for ip in ip_list:
    if ip in blacklist:
        total += 1
print(f"黑名单访问次数{total}")

print("-" * 50)
path_30ms_list = set()
# 6. 找出响应时间大于 30ms 的记录所在的页面路径
for log_item in records:
    current_list = log_item.strip().split('|')
    # print(current_list)
    if int(current_list[-1]) > 30:
        # 如果延迟大于30，记录页面路径
        path_30ms_list.add(current_list[-2])

print(f"访问超时大于30ms的路径去重后的结果：{path_30ms_list}")
