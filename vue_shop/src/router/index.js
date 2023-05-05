import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginComponent from '../components/LoginComponent.vue'
import HomeComponent from '../components/HomeComponent.vue'
import WelcomeComponent from '../components/WelcomeComponent.vue'
import UserComponent from '../components/user/UserComponent.vue'
import MenuComponent from '../components/power/MenuComponent.vue'
import RoleComponent from '../components/power/RoleComponent.vue'
import CateComponent from '../components/goods/CateComponent.vue'
import AttrComponent from '../components/goods/AttrComponent.vue'
import GoodsComponent from '../components/goods/GoodsComponent.vue'
import AddComponent from '../components/goods/AddComponent.vue'
import OrderComponent from '../components/order/OrderComponent.vue'
import DataComponent from '../components/data/DataComponent.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: LoginComponent
  },
  {
    path: '/home',
    component: HomeComponent,
    redirect: '/welcome',
    children: [
      {
        path: '/welcome',
        component: WelcomeComponent
      },
      {
        path: '/user_list',
        component: UserComponent
      },
      {
        path: '/menu_list',
        component: MenuComponent
      },
      {
        path: '/role_list',
        component: RoleComponent
      },
      {
        path: '/cate_list',
        component: CateComponent
      },
      {
        path: '/attr_list',
        component: AttrComponent
      },
      {
        path: '/goods_list',
        component: GoodsComponent
      },
      {
        path: '/add_goods',
        component: AddComponent
      },
      {
        path: '/order_list',
        component: OrderComponent
      },
      {
        path: '/data_list',
        component: DataComponent
      }
    ]
  },
]

const router = new VueRouter({
  routes
})

export default router

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})