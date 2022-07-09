import Vue from "vue";
import VueRouter, {RouteConfig} from "vue-router";
import MyModules from "@/views/MyModules.vue";
import Announcements from "@/views/Announcements.vue";
import Schedule from "@/views/Schedule.vue";
import ModuleAbout from "@/views/ModuleAbout.vue";
import ModuleUnits from "@/views/ModuleUnits.vue";
import UnitSections from "@/views/UnitSections.vue";
import UnitAbout from "@/views/UnitAbout.vue";
import UnitContent from "@/views/UnitContent.vue";
import NotFound from "@/views/NotFound.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    redirect: "/modules",
  },
  {
    path: "/modules",
    component: MyModules,
  },
  {
    path: "/announcements",
    component: Announcements,
  },
  {
    path: "/schedule",
    component: Schedule,
  },
  {
    path: "/modules/:module_id/about",
    component: ModuleAbout,
  },
  {
    path: "/modules/:module_id",
    component: ModuleUnits,
    props: true,
  },
  {
    path: "/modules/:module_id/:unit_no",
    component: UnitSections,
    children: [
      {
        path: "/modules/:module_id/:unit_no/about",
        component: UnitAbout,
      },

      {
        path: "/modules/:module_id/:unit_no/:section",
        component: UnitContent,
      },
    ]
  },
  {
    path: "/:pathMatch(.*)*",
    component: NotFound,
  },
];

export default new VueRouter({
  mode: "history",
  routes,
});
