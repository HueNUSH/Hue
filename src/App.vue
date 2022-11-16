<template>
  <v-app @not-found="notFound = true;">
    <v-app-bar
      permanent
      app
      flat
      clipped
      v-if="!construction"
    >

      <v-toolbar-title>
        <span style="margin-left: 64px">Hue</span>
      </v-toolbar-title>
      <!-- <v-spacer></v-spacer> -->
      <v-toolbar-items class="flex align-center justify-center" style="margin-right: 64px">
        <v-btn v-for="item in routes"
               :to="item.route"
               :key="item.name"
               style="margin-right: 16px"
               text
               auto-height
               depressed
               rounded
        >
          {{item.name}}
        </v-btn>
      </v-toolbar-items>
      <!-- <v-spacer></v-spacer> -->
    </v-app-bar>

    <v-main>
      <NotFound v-if="notFound"/>
      <router-view v-else @not-found="(bool) => this.notFound = bool"/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import NotFound from "@/views/NotFound.vue";
import ComingSoon from "@/views/ComingSoon.vue";
//Vue.prototype.$backendLink = "http://localhost:8000";
Vue.prototype.$backendLink = "https://huelearning.space";

Vue.prototype.$moduleExists = function (moduleId: string): Promise<boolean> {
  return new Promise<boolean>(resolve => {
    fetch(Vue.prototype.$backendLink + "/chokola/modules/module_exists?" + new URLSearchParams({
      "moduleId": moduleId,
    }),{
      method: "GET",
      headers: {
        "accept": "application/json",
      }
    }).then(
      response => response.json().then(
        data => {
          resolve(data.data.exists);
        }
      )
    );
  });
};

export default Vue.extend({
  name: "App",
  components: {
    NotFound,
    ComingSoon,
  },
  data: ()=> ({
    notFound: false,
    construction: false,
  }),
  computed: {
    routes(): Array<{
      name: string;
      route: string;
      icon: string;
    }> {
      return [
        {
          name: "My Modules",
          route: "/modules",
          icon: "mdi-grid-large",
        },
        {
          name: "Announcements",
          route: "/announcements",
          icon: "mdi-bullhorn",
        },
        {
          name: "Schedule",
          route: "/schedule",
          icon: "mdi-calendar-blank",
        },
      ];
    },
  },
  watch: {
    $route (to, from) {
      this.notFound = false;
    }
  }
});
</script>

<style lang="scss" scoped>
@import 'styles/variables.scss';
@import "styles/global.scss";
.v-app-bar a {
  text-decoration: none;
}
.v-list a {
  text-decoration: none;
}
::v-deep .v-btn__content {
  color: $c-text-light-tertiary;
}
::v-deep .v-btn {
  color: $c-primary-background !important;
  opacity: 1 !important;
}
::v-deep .v-btn--active::before, .v-btn--active:hover::before, .v-btn--active  {
  opacity: 1 !important;
  color: $c-primary-accent !important;
}
::v-deep .v-btn-toggle > .v-btn.v-btn {
  opacity: 0 !important;
}
::v-deep .v-btn:focus::before {
  opacity: 1 !important;
}
;;v-deep .v-btn::before {
    opacity: 0 !important;
    color: $c-primary-background !important;
  }
;;v-deep .v-btn:hover::before {
    color: $c-primary-accent !important;
    opacity: 0.34 !important;
  }
::v-deep .v-toolbar__title {
  color: $c-text-light-primary;
}
::v-deep .v-toolbar__items  .v-btn{
  border-radius: 5px;
  height: 60% !important;
  text-transform: unset !important;
}
::v-deep .v-toolbar__content, .v-toolbar__extension {
  align-items: center;
  display: flex;
  padding: 0 24px;
}
</style>
