<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <img src="../assets/logo.png" alt="" />
        <span>电子后台管理系统</span>
      </div>
      <!-- <el-button type="primary" plain @click="test">测试</el-button> -->
      <el-button type="primary" plain @click="logout">退出</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu
          :default-active="activePath"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#303133"
          text-color="#fff"
          active-text-color="#409EFF"
          unique-opened
          router
        >
          <el-submenu :index="item.id+' '" v-for="item in menuList" :key="item.id">
            <template slot="title">
              <i :class="iconObj[item.id]"></i>
              <span>{{item.name}}</span>
            </template>
            <el-menu-item :index="subItem.path" v-for="subItem in item.children" 
            :key="subItem.id" @click="saveActivePath">
              <i :class="iconObj[subItem.id]"></i>
              <span>{{subItem.name}}</span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      menuList: [],
      iconObj: {
        '2':"el-icon-user",
        '3':"el-icon-s-tools",
        '4':"el-icon-s-shop",
        '5':"el-icon-s-order",
        '6':"el-icon-s-data",
        '21': 'el-icon-user',
        '31': 'el-icon-setting',
        '32': 'el-icon-setting',
        '41': 'el-icon-goods',
        '42': 'el-icon-goods',
        '43': 'el-icon-goods',
        '51':"el-icon-s-order",
        '61':"el-icon-s-data",
      },
      activePath: ''
    };
  },
  created() {
    this.getMenulist()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    logout() {
      window.sessionStorage.clear();
      this.$router.push("login");
    },
    test() {
      // const {data:res} = this.$axios.get('/user/test')
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    async getMenulist() {
      const {data:res} = await this.$axios.get('/menu')
      this.menuList = res.data
      // console.log(res)
    },
    saveActivePath(path) {
      window.sessionStorage.setItem('activePath', path.index)
      this.activePath = path.index
    }
  },
};
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
}
.el-header {
  display: flex;
  background-color: #409eff;
  align-items: center;
  justify-content: space-between;
  color: #fff;
  font-size: 20px;
  img {
    height: 60px;
    width: 180px;
  }
  div {
    display: flex;
    align-items: center;
  }
}
.el-aside {
  background-color: #303133;
}
.el-main {
  background-color: #e4e7ed;
}
</style>
