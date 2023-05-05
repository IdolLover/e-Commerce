<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>订单管理</el-breadcrumb-item>
      <el-breadcrumb-item>订单列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <el-row>
        <el-col :span="8">
          <el-input
            v-model="qid"
            placeholder="请输入搜索名称"
            clearable
            @clear="getOrderList"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getOrderList"
            ></el-button>
          </el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-table :data="orderList" border>
          <el-table-column type="index"></el-table-column>
          <el-table-column prop="id" label="id"></el-table-column>
          <el-table-column prop="uname" label="订单用户"></el-table-column>
          <el-table-column prop="price" label="金额"></el-table-column>
          <el-table-column label="是否支付">
            <template slot-scope="scope">
              <el-tag v-if="scope.row.pay_status == 0" type="danger"
                >未支付</el-tag
              >
              <el-tag v-else type="success">已支付</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="is_send" label="是否发件">
            <template slot-scope="scope">
              <el-tag v-if="scope.row.is_send == 0" type="danger"
                >未发件</el-tag
              >
              <el-tag v-else type="success">已发件</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" type="primary" icon="el-icon-s-tools"
                >地址</el-button
              >
              <el-button
                size="mini"
                type="success"
                icon="el-icon-location"
                @click="showExpress(scope.row.id)"
                >物流</el-button
              >
            </template>
          </el-table-column>
        </el-table>
      </el-row>
    </el-card>
    <el-dialog title="物流信息" :visible.sync="expressVisible">
      <el-timeline :reverse="reverse">
        <el-timeline-item
          v-for="(activity, index) in expressList"
          :key="index"
          :timestamp="activity.update_time"
          >{{ activity.content }}</el-timeline-item
        >
      </el-timeline>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      qid: '',
      orderList: [],
      expressVisible: false,
      expressList: [],
      reverse: false
    }
  },
  created() {
    this.getOrderList()
  },
  methods: {
    async getOrderList() {
      console.log(this.qid)
      if (!this.qid || this.qid.trim() === '') {
        const { data: resp } = await this.$axios.get('/order_list')
        if (resp.status !== 200) return this.$msg.error(resp.msg)
        this.$msg.success(resp.msg)
        this.orderList = resp.data
      } else {
        const { data: resp } = await this.$axios.get('/order_list', {
          params: { id: this.qid },
        })
        if (resp.status !== 200) return this.$msg.error(resp.msg)
        this.$msg.success(resp.msg)
        this.orderList = []
        this.orderList.push(resp.data)
      }
      // console.log(this.orderList)
    },
    showExpress(oid) {
      this.expressVisible = true
      this.getExpressList(oid)
      // console.log(oid)
    },
    async getExpressList(oid) {
      const { data: resp } = await this.$axios.get('/express', {
        params: { oid: oid },
      })
      if (resp.status !== 200) return this.$msg.error(resp.msg)
      console.log(resp.data)
      this.expressList = resp.data
    },
  },
}
</script>
<style>
.el-table {
  margin-top: 10px;
}
</style>