status_msg={
    10000: '参数不完整',
    10001: '用户名或密码错误',
    10011: '用户名不合法',
    10012: '两次密码不一致',
    10013: '密码不合法',
    10014: '手机号不合法',
    10015: '邮箱不合法',
    10016: '请登录后使用',
    10017: 'token不可使用',
    10018: '修改用户错误',
    10019: '删除用户错误',
    10020: '修改角色错误',
    10021: '没有此权限',
    10022: '没有此数据',
    10023: '没有上传文件',
    10024: '上传文件格式不符合规范',
    2000: '异常错误',
    200: '成功',
}

def to_dict_msg(status=200, data=None, msg=None):
    return {
        'status': status,
        'data': data,
        'msg': msg if msg else status_msg.get(status)
    }

if __name__=='__main__':
    print(to_dict_msg(10000))