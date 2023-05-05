<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>商品管理</el-breadcrumb-item>
      <el-breadcrumb-item>商品分类</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <el-row>
        <el-col :span="2">
          <el-button
            type="primary"
            icon="el-icon-circle-plus-outline"
            @click="showAddCateDialog()"
            >新增分类</el-button
          >
        </el-col>
      </el-row>
      <el-row>
        <tree-table
          :data="cateList"
          :columns="columns"
          :selection-type="false"
          :expand-type="false"
          class="tree-table"
          border
          :show-index="true"
        >
          <template slot="level" slot-scope="scope">
            <el-tag v-if="scope.row.level === 1">一级分类</el-tag>
            <el-tag v-else-if="scope.row.level === 2" type="success"
              >二级分类</el-tag
            >
            <el-tag v-else type="warning">三级分类</el-tag>
          </template>
          <template slot="opt">
            <el-button size="mini" type="primary" icon="el-icon-edit"
              >编辑</el-button
            >
            <el-button size="mini" type="danger" icon="el-icon-delete"
              >删除</el-button
            >
          </template>
        </tree-table>
      </el-row>
    </el-card>
    <el-dialog
      title="增加分类"
      :visible.sync="addCateDialogVisible"
      width="30%"
      @close="closeCateDialog"
    >
      <el-form
        :model="addCateForm"
        :rules="addCateRules"
        ref="addCateRef"
        label-width="80px"
      >
        <el-form-item label="分类名称" prop="name">
          <el-input v-model="addCateForm.name"></el-input>
        </el-form-item>
        <el-form-item label="父类节点">
          <el-cascader
            v-model="selectKeys"
            :options="catePidlist"
            :props="{
              expandTrigger: 'hover',
              label: 'name',
              value: 'id',
              checkStrictly: true,
            }"
            @change="chanageSeletor"
            clearable
            separator=" > "
          ></el-cascader>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="addCate">确定</el-button>
          <el-button @click="closeCateDialog">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      cateList: [],
      columns: [
        { label: '分类名称', prop: 'name' },
        { label: '分类等级', type: 'template', template: 'level' },
        { label: '操作', type: 'template', template: 'opt' },
      ],
      addCateDialogVisible: false,
      addCateForm: {
        name: '',
        pid: 0,
        level: 1,
      },
      addCateRules: {
        name: [{ required: true, message: '请输入分类名称', trigger: 'blur' }],
      },
      catePidlist: [],
      selectKeys: [],
    }
  },
  created() {
    this.getCateList()
  },
  methods: {
    async getCateList() {
      const { data: res } = await this.$axios.get('/category_list')
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.cateList = res.data.data
    },
    showAddCateDialog() {
      this.getCatePidList()
      this.addCateDialogVisible = true
    },
    async addCate() {
      const { data: res } = await this.$axios.post(
        'category',
        this.$qs.stringify(this.addCateForm)
      )
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.$msg.success(res.msg)
      this.getCateList()
      this.closeCateDialog()
    },
    async getCatePidList() {
      const { data: res } = await this.$axios.get('/category_list', {
        params: { level: 2 },
      })
      this.catePidlist = res.data.data
    },
    chanageSeletor() {
      if (this.selectKeys.length > 0) {
        this.addCateForm.pid = this.selectKeys[this.selectKeys.length - 1]
        this.addCateForm.level = this.selectKeys.length + 1
      } else {
        this.addCateForm.pid = 0
        this.addCateForm.level = 1
      }
    },
    closeCateDialog() {
      this.$refs.addCateRef.resetFields()
      this.selectKeys = []
      this.addCateForm.level = 1
      this.addCateForm.pid = 0
      this.addCateDialogVisible = false
    },
  },
}
</script>
<style lang="less" scoped>
.tree-table {
  margin-top: 15px;
}
</style>