<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>商品管理</el-breadcrumb-item>
      <el-breadcrumb-item>商品列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <el-row>
        <el-col :span="8">
          <el-input
            v-model="qname"
            placeholder="请输入搜索名称"
            clearable
            @clear="getGoodsList"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getGoodsList"
            ></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button class="btn" type="primary" icon="el-icon-plus" @click="addGoodsPage">增加商品</el-button>
        </el-col>
      </el-row>
      <el-table border :data="goodsList">
        <el-table-column type="index"></el-table-column>
        <el-table-column label="商品名称" prop="name"></el-table-column>
        <el-table-column
          label="商品价格(元)"
          prop="price"
          width="100px"
        ></el-table-column>
        <el-table-column
          label="商品库存"
          prop="number"
          width="80px"
        ></el-table-column>
        <el-table-column label="操作" width="200px">
          <template slot-scope="scope">
            <el-button size="mini" type="success" icon="el-icon-edit"
              >编辑</el-button
            >
            <el-button
              size="mini"
              type="danger"
              icon="el-icon-delete"
              @click="removeGoods(scope.row.id)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      goodsList: [],
      qname: '',
    }
  },
  created() {
    this.getGoodsList()
  },
  methods: {
    async getGoodsList() {
      const { data: resp } = await this.$axios.get('/goods_list', {
        params: { name: this.qname },
      })
      if (resp.status !== 200) return this.$msg.error(resp.msg)
      this.$msg.success(resp.msg)
      this.goodsList = resp.data
    },
    removeGoods(gid) {
      this.$confirm('此操作将永久此商品数据, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          console.log(gid)
          const { data: resp } = await this.$axios.delete('/goods', {
            data: { id: gid },
          })
          if (resp.status !== 200) return this.$msg.error(resp.msg)
          this.$msg.success(resp.msg)
          this.getGoodsList()
        })
        .catch(() => {
          this.$msg({
            type: 'info',
            message: '已取消删除',
          })
        })
    },
    addGoodsPage() {
      this.$router.push('/add_goods')
    }
  },
}
</script>

<style lang="less" scoped>
.btn {
  margin-left: 5px;
}
.el-table {
  margin-top: 10px;
}
</style>
