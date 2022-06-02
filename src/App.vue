<template>
  <v-app style="background-color: #FBEFE7">
    <v-app-bar
      app
      color="#55342A"
      clipped-left
      dark
    >
      <v-app-bar-nav-icon @click="mini = !mini"></v-app-bar-nav-icon>
      <v-toolbar-title>
        Welcome to Hue
      </v-toolbar-title>

      <v-spacer></v-spacer>
    </v-app-bar>


    <v-navigation-drawer
      :mini-variant="mini"
      permanent
      app
      clipped
      color="#EFDDCF">

      <v-list
        class="mt-12"
        dense
        nav>
        <router-link v-for="item in routes"
                     :to="item.route"
                     style="text-decoration: none; color: inherit;"
                     :key="item.name">
          <v-list-item link class="mt-3">
            <v-list-item-icon>
              <v-icon style="color: #55342A">{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>
                {{ item.name }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "App",
  data: () => ({
    mini: true,
    user: {
    }
  }),
  computed: {
    routes(): Array<{
      name: string;
      route: string;
      icon: string;
    }> {
      // Add routes here to correspond to router.ts
      if(this.$route.path.startsWith("/modules") && this.$route.params.module_id != null) {
        return [
          {
            name: "Home",
            route: "/",
            icon: "mdi-home",
          },
          {
            name: "Info",
            route: "/modules/info/" + this.$route.params.module_id,
            icon: "mdi-information-outline",
          },
          {
            name: "Units",
            route: "/modules/" + this.$route.params.module_id,
            icon: "mdi-format-list-numbered",
          },
          {
            name: "Announcements",
            route: "/modules/announcements/" + this.$route.params.module_id,
            icon: "mdi-bullhorn",
          },
          {
            name: "Schedule",
            route: "/modules/schedule/" + this.$route.params.module_id,
            icon: "mdi-calendar-blank",
          },
        ];
      }
      return [
        {
          name: "Home",
          route: "/",
          icon: "mdi-home",
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
  }
});
</script>
