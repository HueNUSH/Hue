<template>
  <v-app>
    <v-layout row justify-center style="">
      <v-app-bar app class="hidden-xs-only" fixed>
        <router-link to="/">
          <v-row>
            <v-img color="white" class="mx-2" src="@/assets/hue_logo.svg" fill="white" contain max-height="30" max-width="50" />
            <h3 style="color:white!important" class="pt-1">Learning Space</h3>
          </v-row>

        </router-link>
        <v-toolbar-items class="flex align-center justify-center" style="margin-right: 0px; margin-left: -36px;">

          <v-btn v-for="item in mainRoutes" :to="item.route" :key="item.name" :title="item.name"
            style="margin-right: 16px; height:36px !important" text auto-height depressed rounded>{{
              item.name
            }}</v-btn>

          <v-btn v-if="debug" style="margin-right: 16px; height:36px !important" to="/admin/user-list" text auto-height depressed rounded>Users</v-btn>
        </v-toolbar-items>
        <!-- <v-switch v-model="debug" inset color="white" class="align-center pr-5"
          label="Admin Toggle"></v-switch>
        
        <v-btn outlined auto-height class="mr-3" style="color:white !important; text-transform: unset !important; border-width: 2px;"
          to="/login" key="login"><b>Log In</b></v-btn> -->

      </v-app-bar>
      <v-app-bar app dark class="hidden-sm-and-up" fixed>
        <router-link to="/">
          <v-row>
            <v-img color="white" class="mx-2" src="@/assets/hue_logo.svg" fill="white" contain max-height="30" max-width="50" />
          </v-row>

        </router-link>
        <v-spacer></v-spacer>
        <!-- <v-switch v-model="debug" inset color="white" class="align-center pr-5"
          label="Admin Toggle"></v-switch>
        <v-btn outlined auto-height style="color:white !important; text-transform: unset !important; border-width: 2px;"
          to="/login" key="login"><b>Log In</b></v-btn> -->
        <v-app-bar-nav-icon @click="dialog = true"></v-app-bar-nav-icon>
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-top-transition"
          class="d-flex align-center fill-height">

          <v-card class="d-flex align-center fill-height" style="border-radius: 0%;">
            <v-col class="fill-height">
              <v-flex style="text-align: right;margin-right: 15px; margin-top: 15px;">
                <v-btn icon color="black" @click="dialog = false"> <v-icon
                    color="black">mdi-chevron-triple-up</v-icon></v-btn>
              </v-flex>

              <v-list rounded class="justify-center" style="margin: auto;">
                <v-list-item-group color="primary">
                  <v-list-item v-for="item in mainRoutes" :key="item.name" :to="item.route" @click="dialog = false">
                    <v-icon v-if="item.icon" style="margin-right: 15px; color:inherit">{{ item.icon }}</v-icon>
                    <v-list-tile-content style="align-items: center;justify-content: center;">
                      <v-list-tile-title style="justify-content: center" :title="item.name">{{
                        item.name
                      }}</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-item>

                  <v-list-item v-if="debug" to="/admin/user-list" @click="dialog = false">
                    <v-icon style="margin-right: 15px; color:inherit">mdi-account</v-icon>
                    <v-list-tile-content style="align-items: center;justify-content: center;">
                      <v-list-tile-title style="justify-content: center" title="Users">
                        Users
                      </v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-item>


                </v-list-item-group>
              </v-list>

            </v-col>

          </v-card>
        </v-dialog>

      </v-app-bar>
      <v-col>
        <v-main class="pt-16 pt-sm-16 pt-xs-16 pt-md-16 pt-lg-16 pt-xl-16">
          <router-view />
        </v-main>
        
      </v-col>
    </v-layout>
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
    dialog: false,
    debug: false,
    notFound: false,
    construction: false,
  }),
  computed: {
    mainRoutes(): Array<{
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
