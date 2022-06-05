import Vue from "vue";
import VueRouter, {RouteConfig} from "vue-router";
import Home from "@/views/Home.vue";
import Announcements from "@/views/Announcements.vue";
import Schedule from "@/views/Schedule.vue";
import Modules from "@/views/Modules.vue";
import Unit from "@/views/Unit.vue";
import Info from "@/views/Info.vue";
import Subchapter from "@/views/Subchapter.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/announcements",
    component: Announcements,
  },
  {
    path: "/modules/announcements/:module_id",
    component: Announcements,
  },
  {
    path: "/schedule",
    component: Schedule,
  },
  {
    path: "/modules/schedule/:module_id",
    component: Schedule,
  },
  {
    path: "/modules/info/:module_id",
    component: Info,
  },
  {
    path: "/modules/:module_id",
    component: Modules,
  },
  {
    path: "/modules/:module_id/:unit_no",
    component: Unit,
  },
  {
    path: "/modules/:module_id/:unit_no/:subchapter_no",
    component: Subchapter,
  },
];

export default new VueRouter({
  mode: 'history',
  routes,
});
