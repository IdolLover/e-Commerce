<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>数据统计</el-breadcrumb-item>
      <el-breadcrumb-item>商品统计</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
      <div id="main" style="width: 600px;height:400px;"></div>
    </el-card>
  </div>
</template>
<script>
// import echarts from 'echarts';
import * as echarts from 'echarts'
export default {
  async mounted() {
    const { data: resp } = await this.$axios.get('/cate_group_level')
    if (resp.status !== 200) return this.$msg.error(resp.msg)

    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('main'))
    // 指定图表的配置项和数据
    var option = {
      title: {
        text: 'ECharts'
      },
      tooltip: {},
      legend: {
        data: [resp.data.name]
      },
      xAxis: {
        data: resp.data.xAxis
      },
      yAxis: {},
      series: [
        {
          name: resp.data.name,
          type: 'bar',
          data: resp.data.series_data
        }
      ]
    }

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option)
  }
}
</script>