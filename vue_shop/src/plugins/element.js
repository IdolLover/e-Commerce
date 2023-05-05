import Vue from 'vue'
import { Button,Form,FormItem,Input,Message,Container,Header,Aside,Main,
    Submenu,Menu,MenuItemGroup,MenuItem,Breadcrumb,BreadcrumbItem,Card,
    Row, Col, Table, TableColumn,Pagination,Dialog,Tag, Option, Select,
    MessageBox, Tree, Cascader, Tabs, TabPane, Alert, Step, Steps, Checkbox, 
    CheckboxGroup, Upload, Timeline, TimelineItem } from 'element-ui'

import TreeTable from 'vue-table-with-tree-grid'
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css' // import styles
import 'quill/dist/quill.snow.css' // for snow theme
import 'quill/dist/quill.bubble.css' // for bubble theme

Vue.component('tree-table', TreeTable)
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)

Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)

Vue.use(Submenu)
Vue.use(Menu)
Vue.use(MenuItemGroup)
Vue.use(MenuItem)

Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)
Vue.use(Card)
Vue.use(Row)
Vue.use(Col)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Pagination)

Vue.use(Dialog)
Vue.use(Tag)
Vue.use(Option)
Vue.use(Select)

Vue.use(Tree)
Vue.use(Cascader)
Vue.use(Tabs)
Vue.use(TabPane)
Vue.use(Alert)

Vue.use(Step)
Vue.use(Steps)
Vue.use(Checkbox)
Vue.use(CheckboxGroup)
Vue.use(Upload)

Vue.use(Timeline)
Vue.use(TimelineItem)
Vue.prototype.$msg = Message
Vue.prototype.$confirm = MessageBox.confirm
Vue.use(VueQuillEditor)