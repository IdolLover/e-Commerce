<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <div>
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input placeholder="请输入用户名" v-model="queryInfo.name">
              <el-button
                slot="append"
                icon="el-icon-search"
                @click="searchUser"
              ></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button
              type="primary"
              icon="el-icon-circle-plus-outline"
              @click="addDialogVisible = true"
              >新增用户</el-button
            >
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-table :data="userList" border style="width: 100%">
              <el-table-column type="index"></el-table-column>
              <el-table-column
                width="50"
                prop="id"
                label="ID"
              ></el-table-column>
              <el-table-column prop="name" label="用户名"></el-table-column>
              <el-table-column prop="nick_name" label="昵称"> </el-table-column>
              <el-table-column prop="email" label="邮箱"> </el-table-column>
              <el-table-column prop="phone" label="电话"> </el-table-column>
              <el-table-column prop="role_name" label="角色名称">
              </el-table-column>
              <el-table-column label="操作">
                <template slot-scope="scope">
                  <el-button
                    type="primary"
                    icon="el-icon-edit"
                    role_name
                    circle
                    @click="showEdit(scope.row)"
                  ></el-button>
                  <el-button
                    type="warning"
                    icon="el-icon-refresh"
                    circle
                    @click="showReset(scope.row)"
                  ></el-button>
                  <el-button
                    type="danger"
                    icon="el-icon-delete"
                    circle
                    @click="showDel(scope.row)"
                  ></el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryInfo.pnum"
          :page-sizes="[1, 2, 5, 10]"
          :page-size="queryInfo.psize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
        >
        </el-pagination>
      </div>
    </el-card>
    <!-- 增加用户功能 -->
    <el-dialog
      title="新增用户"
      :visible.sync="addDialogVisible"
      width="30%"
      :before-close="addFormClose"
    >
      <el-form
        ref="addFormRef"
        :rules="addFormRules"
        :model="addForm"
        label-width="80px"
      >
        <el-form-item label="账号" prop="name">
          <el-col :span="18">
            <el-input v-model="addForm.name"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="昵称" prop="nick_name">
          <el-col :span="18">
            <el-input v-model="addForm.nick_name"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="密码" prop="pwd">
          <el-col :span="18">
            <el-input show-password v-model="addForm.pwd"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="确认密码" prop="real_pwd">
          <el-col :span="18">
            <el-input show-password v-model="addForm.real_pwd"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="电话" prop="phone">
          <el-col :span="18">
            <el-input v-model="addForm.phone"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-col :span="18">
            <el-input v-model="addForm.email"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="addForm.role_name" placeholder="请选择角色">
            <el-option
              :label="r.name"
              :value="r.id"
              v-for="r in roles"
              :key="r.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 编辑用户功能 -->
    <el-dialog
      title="编辑用户"
      :visible.sync="editDialogVisible"
      width="30%"
      :before-close="editFormClose"
    >
      <el-form
        ref="editFormRef"
        :rules="editFormRules"
        :model="editForm"
        label-width="80px"
      >
        <el-form-item label="账号" prop="name">
          <el-col :span="18">
            <el-input v-model="editForm.name" :disabled="true"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="昵称" prop="nick_name">
          <el-col :span="18">
            <el-input v-model="editForm.nick_name" :disabled="true"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="电话" prop="phone">
          <el-col :span="18">
            <el-input v-model="editForm.phone"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-col :span="18">
            <el-input v-model="editForm.email"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="editForm.role_name" placeholder="请选择角色">
            <el-option
              :label="r.name"
              :value="r.id"
              v-for="r in roles"
              :key="r.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editUser">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 删除用户功能 -->
    <el-dialog title="删除用户" :visible.sync="delDialogVisible" width="30%">
      <span>确认删除账号 {{ delName }} 昵称 {{ delNickName }} 的用户吗？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="delDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="delUser">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 重置密码功能 -->
    <el-dialog
      title="重置用户密码"
      :visible.sync="resetDialogVisible"
      width="30%"
    >
      <span
        >确认重置账号 {{ resetName }} 昵称 {{ resetNickName }} 的用户吗？</span
      >
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="resetUser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<style scoped lang="less">
.el-table {
  margin-top: 10px;
}
</style>

<script>
export default {
  data() {
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.addForm.pwd) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    const validatePhone = (rule, value, callback) => {
      // 定义一个正则来验证手机号是否是有效的
      const phoneReg = /^1[3456789]\d{9}$/
      if (!value){
        return callback()
      }
      else if( phoneReg.test(value)) {
        return callback()
      }
      return callback(new Error('请输入有效的手机号'))
    }
    const validateEmail = (rule, value, callback) => {
      // 定义一个正则来验证邮箱是否是有效的
      const emailReg = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/
      if (!value){
        return callback()
      }
      else if (emailReg.test(value)) {
        return callback()
      }
      return callback(new Error('请输入有效的手机号'))
    }
    return {
      userList: [],
      queryInfo: {
        name: '',
        pnum: 1,
        psize: 2,
      },
      total: 0,
      addDialogVisible: false,
      editDialogVisible: false,
      delDialogVisible: false,
      resetDialogVisible: false,
      addForm: {},
      editForm: {},
      delId: 0,
      delName: '',
      delNickName: '',
      resetId: 0,
      resetName: '',
      resetNickName: '',
      roles: [],
      addFormRules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 2, max: 6, message: '长度在 2 到 6 个字符', trigger: 'blur' },
        ],
        nick_name: [
          { required: true, message: '请输入昵称', trigger: 'blur' },
          { min: 2, max: 6, message: '长度在 2 到 6 个字符', trigger: 'blur' },
        ],
        pwd: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 3,
            max: 12,
            message: '长度在 3 到 12 个字符',
            trigger: 'blur',
          },
        ],
        real_pwd: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          {
            validator: validatePass2,
            trigger: 'blur',
          },
        ],
        phone: [{ validator: validatePhone, trigger: 'blur' }],
        email: [{ validator: validateEmail, trigger: 'blur' }],
        // phone: [
        //   // { required: true, message: "请输入电话", trigger: "blur" },
        //   {
        //     pattern: /^1[3456789]\d{9}$/,
        //     message: '请输入正确的电话号码',
        //     trigger: 'blur',
        //   },
        // ],
        // email: [
        //   // { required: true, message: "请输入邮箱", trigger: "blur" },
        //   {
        //     pattern: /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
        //     message: '请输入正确的邮箱',
        //     trigger: 'blur',
        //     required: false,
        //   },
        // ],
      },
      editFormRules: {
        phone: [
          // { required: true, message: "请输入电话", trigger: "blur" },
          {
            pattern: /^(1[3456789]\d{9})?$/,
            message: '请输入正确的电话号码',
            trigger: 'blur',
            required: false,
          },
        ],
        email: [
          // { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            pattern: /^(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)?$/,
            message: '请输入正确的邮箱',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  created() {
    this.getUserList()
    this.getRole()
  },
  methods: {
    async getUserList() {
      const { data: res } = await this.$axios.get('/user/userlist', {
        params: this.queryInfo,
      })
      if (res.status !== 200) return this.$message.error(res.msg)
      this.total = res.data.totalPage
      this.userList = res.data.users
    },
    handleSizeChange(val) {
      this.queryInfo.psize = val
      this.getUserList()
      console.log(val)
    },
    handleCurrentChange(val) {
      this.queryInfo.pnum = val
      this.getUserList()
      console.log(val)
    },
    searchUser() {
      this.queryInfo.pnum = 1
      this.getUserList()
    },
    addFormClose() {
      this.$refs.addFormRef.resetFields()
      this.addDialogVisible = false
    },
    addUser() {
      this.$refs.addFormRef.validate(async (valid) => {
        if (!valid) return
        const { data: res } = await this.$axios.post(
          '/user/user',
          this.$qs.stringify(this.addForm)
        )
        if (res.status !== 200) return this.$msg.error(res.msg)
        this.$msg.success(res.msg)
        this.addDialogVisible = false
        this.$refs.addFormRef.resetFields()
        this.getUserList()
      })
    },
    async showEdit(row) {
      // 获取实时数据
      const { data: res } = await this.$axios.get('/user/user', {
        params: { id: row.id },
      })
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.editForm = res.data
      this.editDialogVisible = true
    },
    editUser() {
      this.$refs.editFormRef.validate(async (valid) => {
        if (!valid) return
        const { data: res } = await this.$axios.put(
          '/user/user',
          this.$qs.stringify(this.editForm)
        )
        if (res.status != 200) return this.$msg.error(res.msg)
        this.$msg.success(res.msg)
        this.editDialogVisible = false
        this.getUserList()
      })
    },
    showDel(row) {
      this.delId = row.id
      this.delName = row.name
      this.delNickName = row.nick_name
      this.delDialogVisible = true
    },
    async delUser() {
      const { data: res } = await this.$axios.delete('/user/user', {
        data: { id: this.delId },
      })
      if (res.status !== 200) return this.$msg.error(res.msg)
      console.log(res)
      this.$msg.success(res.msg)
      this.delDialogVisible = false
      this.getUserList()
    },
    showReset(row) {
      this.resetId = row.id
      this.resetName = row.name
      this.resetNickName = row.nick_name
      this.resetDialogVisible = true
    },
    async resetUser() {
      const { data: res } = await this.$axios.get('/user/reset', {
        params: { id: this.resetId },
      })
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.$msg.success(res.msg)
      this.resetDialogVisible = false
    },
    async getRole() {
      const { data: res } = await this.$axios.get('/role')
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.roles = res.data
      console.log(res)
    },
  },
}
</script>