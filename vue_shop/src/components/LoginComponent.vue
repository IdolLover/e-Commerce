<template>
  <div class="login_container">
    <div class="login_box">
      <div class="logo">
        <img src="../assets/logo.png" alt="" />
      </div>
      <el-form
        ref="userRef"
        :rules="userRules"
        :model="userForm"
        label-width="0px"
        class="form_style"
      >
        <el-form-item prop="name">
          <el-input
            v-model="userForm.name"
            prefix-icon="el-icon-user-solid"
            placeholder="用户名"
          ></el-input>
        </el-form-item>
        <el-form-item prop="pwd">
          <el-input
            show-password
            v-model="userForm.pwd"
            prefix-icon="el-icon-lock"
            placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-form-item class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userForm: {
        name: "",
        pwd: "",
      },
      userRules: {
        name: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 2, max: 6, message: "长度在 2 到 6 个字符", trigger: "blur" },
        ],
        pwd: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 3,
            max: 12,
            message: "长度在 3 到 12 个字符",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    resetForm() {
      this.$refs.userRef.resetFields();
    },
    login() {
      this.$refs.userRef.validate(async (valid) => {
        if (!valid) return;
        const { data: res } = await this.$axios.post(
          "/user/login",
          this.$qs.stringify(this.userForm)
        );
        console.log(res);
        if (res.status === 200) {
          // 登录成功
          window.sessionStorage.setItem("token", res.data.token);
          this.$msg.success(res.msg);
          // 跳转成功页面
          this.$router.push("/home");
        } else {
          this.$msg.error(res.msg);
        }
      });
    },
  },
};
</script>

<style lang='less' scoped>
.login_container {
  background-image: url("../assets/background.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  width: 100%;
  height: 100%;
}
.login_box {
  width: 450px;
  height: 300px;
  border-radius: 15px;
  
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.login_box::before {
  /* 使用伪元素创建一个位于盒子上面的图层 */
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #fff;
  /* 设置伪元素的背景颜色为白色，并设置透明度为0.5 */
  opacity: 0.6;
}
.logo {
  height: 80px;
  width: 200px;
  border: 1px solid #eee;
  border-radius: 10%;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 10px #ddd;
  img {
    height: 100%;
    width: 100%;
  }
}
.form_style {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 10%;
  box-sizing: border-box;
}
.btns {
  display: flex;
  justify-content: flex-end;
}
</style>