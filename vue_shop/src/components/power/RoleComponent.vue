<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>权限管理</el-breadcrumb-item>
      <el-breadcrumb-item>角色列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <el-row>
        <el-col :span="2">
          <el-button type="primary" icon="el-icon-circle-plus-outline"
            >新增角色</el-button
          >
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-table :data="roleList" border style="width: 80%">
            <el-table-column type="expand">
              <template slot-scope="scope">
                <el-row
                  :class="['rcenter', 'bottom', i === 0 ? 'top' : '']"
                  v-for="(m, i) in scope.row.menu"
                  :key="m.id"
                >
                  <el-col :span="10">
                    <el-tag closable @click="removeMenu(scope.row, m.id)">{{
                      m.name
                    }}</el-tag>
                    <i class="el-icon-caret-right"></i>
                  </el-col>
                  <el-col :span="14">
                    <el-tag
                      closable
                      @click="removeMenu(scope.row, sm.id)"
                      v-for="sm in m.children"
                      :key="sm.id"
                      type="success"
                    >
                      {{ sm.name }}
                    </el-tag>
                  </el-col>
                </el-row>
              </template>
            </el-table-column>
            <el-table-column type="index"></el-table-column>
            <el-table-column prop="id" label="ID"></el-table-column>
            <el-table-column prop="name" label="角色名称"></el-table-column>
            <el-table-column prop="desc" label="角色详情"></el-table-column>
            <el-table-column prop="level" label="操作" width="300px">
              <template slot-scope="scope">
                <el-button size="mini" type="success" icon="el-icon-edit">
                  修改
                </el-button>
                <el-button size="mini" type="danger" icon="el-icon-delete">
                  删除
                </el-button>
                <el-button
                  size="mini"
                  type="warning"
                  icon="el-icon-setting"
                  @click="showMenuDialog(scope.row)"
                >
                  分配权限
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-col>
      </el-row>
    </el-card>
    <el-dialog 
      title="分配权限" 
      :visible.sync="menuDialogVisible" 
      width="40%"
      :before-close="dialogClose"
    >
      <span>
        <el-tree
          :default-checked-keys="keyList"
          node-key="id"
          show-checkbox
          default-expand-all
          :data="menuList"
          :props="menuProps"
          ref="treeRef"
        ></el-tree>
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogClose()">取 消</el-button>
        <el-button type="primary" @click="editMenu()"
          >确 定</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      roleList: [],
      menuDialogVisible: false,
      menuProps: {
        label: 'name',
        children: 'children',
      },
      menuList: [],
      keyList: [],
      rid: 0,
    }
  },
  created() {
    this.getRoleList()
    this.getMenuList()
  },
  methods: {
    getKeys(menu) {
      menu.forEach((item) => {
        item.children.forEach((i) => {
          this.keyList.push(i.id)
        })
      })
    },
    async getMenuList() {
      const { data: res } = await this.$axios.get('/menu')
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.menuList = res.data
    },
    async getRoleList() {
      const { data: res } = await this.$axios.get('/role')
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.roleList = res.data
      // console.log(res.data)
    },
    showMenuDialog(row) {
      this.rid = row.id
      this.getMenuList()
      this.menuDialogVisible = true
      this.getKeys(row.menu)
      console.log(row.menu)
      console.log(this.keyList)
    },
    removeMenu(row, mid) {
      this.$confirm('此操作将永久删除该权限, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          const { data: resp } = await this.$axios.get(
            `/del_menu/${row.id}/${mid}`
          )
          if (resp.status !== 200) return this.$msg(resp.msg)
          this.$msg({
            type: 'success',
            message: '删除成功!',
          })
          row.menu = resp.data
        })
        .catch(() => {
          this.$msg({
            type: 'info',
            message: '已取消删除',
          })
        })
    },
    dialogClose() {
      this.keyList= []
      this.menuDialogVisible = false
    },
    async editMenu() {
      const mids = [
        ...this.$refs.treeRef.getCheckedKeys(),
        ...this.$refs.treeRef.getHalfCheckedKeys()
      ]
      // console.log(mids)
      const midsStr = mids.join(',')
      const {data:res} = await this.$axios.post(`/set_menu/${this.rid}`,this.$qs.stringify({mids:midsStr}))
      if(res.status!==200) return this.$msg.error(res.msg)
      this.$msg.success(res.msg)
      this.getRoleList()
      this.dialogClose()
    },
  },
}
</script>

<style>
.top {
  border-top: 1px solid #eee;
}
.bottom {
  border-bottom: 1px solid #eee;
}
.el-tag {
  margin: 10px;
}
.rcenter {
  padding-left: 80px;
  display: flex;
  align-items: center;
}
</style>