<template>
  <v-app>
    <v-container fluid class="px-12 py-6 text-font-size-16">
      <div d-flex>
        <div class="pa-14" style="display:inline-block;vertical-align: top;">
          <v-card elevation="12" width="256">
            <v-navigation-drawer floating permanent>

              <v-list dense rounded class="py-6">

                <v-list-item :key="'About'"
                  :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/about'">
                  <v-list-item-icon>
                    <v-icon>mdi-information</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>About</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>


                <v-list-item>
                  <v-divider></v-divider>
                </v-list-item>

                <v-list-item v-for="item in routes" :key="item.name" :to="item.route">
                  <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                  </v-list-item-icon>

                  <v-list-item-content>
                    <v-list-item-title>{{ item.name }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-navigation-drawer>
          </v-card>
        </div>

        <div class="pa-14" style="display:inline-block;vertical-align: top;width:70%">
          <router-link :to="'/modules/' + $route.params.module_id" class="links">
            &lt; Back to Module
          </router-link>
          <!-- 
    <h1>Sections of a unit</h1>
    <p>Module id: {{ $route.params.module_id }}</p>
    <p>Unit no: {{ $route.params.unit_no }}</p>
    <v-btn :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/about'">
      About this unit
    </v-btn> -->
          <v-main class="py-6" fluid full-width>
            <router-view />
          </v-main>

        </div>

      </div>
    </v-container>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue"
export default Vue.extend({
  name: "UnitSections",
  computed: {
    routes(): Array<{
      name: string;
      route: string;
      icon: string;
    }> {
      return [
        {
          name: "Test PDF",
          route: '/modules/' + this.$route.params.module_id + '/' + this.$route.params.unit_no + '/pdf',
          icon: "mdi-bullhorn",
        },
        {
          name: "Test PPTX",
          route: '/modules/' + this.$route.params.module_id + '/' + this.$route.params.unit_no + '/pptx',
          icon: "mdi-bullhorn",
        },
        {
          name: "Test MP4",
          route: '/modules/' + this.$route.params.module_id + '/' + this.$route.params.unit_no + '/mp4',
          icon: "mdi-bullhorn",
        },
      ];
    },
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
::v-deep .v-list-item{
    color: $c-primary-accent !important;
  opacity: 1 !important;
}
::v-deep .v-list-item--active:before, .v-list-item--active:hover:before, .v-list-item:focus:before {
    opacity: 0.2 !important;
}
</style>