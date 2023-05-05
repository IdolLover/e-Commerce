module.exports = {
  devServer: {
    proxy: {
      '/': { // 将其他请求代理到后端 Flask 服务器
        ws: false,
        target: 'http://localhost:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/': ''
        }, 
      },
    }
  }
};
