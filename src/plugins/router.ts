import Vue from "vue";
import VueRouter, {RouteConfig} from "vue-router";
import MyModules from "@/views/MyModules.vue";
import Announcements from "@/views/Announcements.vue";
import Schedule from "@/views/Schedule.vue";
import ModuleAbout from "@/views/ModuleAbout.vue";
import ModuleUnits from "@/views/ModuleUnits.vue";
import UnitSections from "@/views/UnitSections.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/modules",
    component: MyModules,
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
    path: "/modules/:module_id/about",
    component: ModuleAbout,
  },
  {
    path: "/modules/:module_id",
    component: ModuleUnits,
  },
  {
    path: "/modules/:module_id/:unit_no",
    component: UnitSections,
  },
];

export default new VueRouter({
  mode: 'history',
  routes,
});
