<template>
  <v-app>
    <v-navigation-drawer
      permanent
      app
      clipped>

      <v-list
        class="mt-12"
        dense
        nav>
        <router-link v-for="item in routes"
                     :to="item.route"
                     :key="item.name">
          <v-list-item link class="mt-3">
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
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
    user: {
    }
  }),
  computed: {
    routes(): Array<{
      name: string;
      route: string;
      icon: string;
    }> {
      // Archived for implementing Unit page later.

      // if(this.$route.path.startsWith("/modules") && this.$route.params.module_id != null) {
      //   return [
      //     {
      //       name: "Home",
      //       route: "/modules",
      //       icon: "mdi-home",
      //     },
      //     {
      //       name: "Info",
      //       route: "/modules/info/" + this.$route.params.module_id,
      //       icon: "mdi-information-outline",
      //     },
      //     {
      //       name: "Units",
      //       route: "/modules/" + this.$route.params.module_id,
      //       icon: "mdi-format-list-numbered",
      //     },
      //     {
      //       name: "Announcements",
      //       route: "/modules/announcements/" + this.$route.params.module_id,
      //       icon: "mdi-bullhorn",
      //     },
      //     {
      //       name: "Schedule",
      //       route: "/modules/schedule/" + this.$route.params.module_id,
      //       icon: "mdi-calendar-blank",
      //     },
      //   ];
      // }
      return [
        {
          name: "My modules",
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
  }
});
</script>

<style lang="scss" scoped>
@import 'styles/variables.scss';
@import "styles/global.scss";

.v-list a {
  text-decoration: none;
}

.v-list-item__icon .v-icon {
  color: $c-text-light-tertiary;
}

.v-list-item__content {
  color: $c-text-light-primary;
}
</style>
