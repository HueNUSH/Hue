<template>
  <v-container fluid class="pb-6" max-width="80rem">
    <div class="pa-14" id="unit-grid">
       <v-card
      class="px-8 py-6 text-font-size-16"
      max-width="80rem"
      elevation="0"
    >
      <router-link to="/modules" class="links">
        &lt; My modules
      </router-link> <br/>

      <v-row>
        <v-col cols="auto" class="d-flex align-center">
          <v-sheet
            class="rounded-circle d-flex align-center justify-center"
            color="orange"
            :height="64"
            :width="64"
          >
            <v-icon x-large>
              {{ module.moduleIcon }}
            </v-icon>
          </v-sheet>
        </v-col>

        <v-col class="pl-4 mt-3">
          <h1 class="card-title">{{ module.moduleName }}</h1>
          <p class="text-dark-tertiary">Academic Week</p>
        </v-col>
      </v-row>

    </v-card>

        <p></p>
      <!-- <b class="text-dark-primary text-font-size-16 pb-3"></b> -->
      <h2 class="text-dark-primary text-display-semibold text-font-size-16 pb-3" style="margin-top: 5px;">
      Units • {{ module.unitsCompleted }}/{{ module.units.length }} completed
      </h2>
      <p></p>

      <v-row>
        <v-col
          cols="12"
          lg="4"
          md="6"
          v-for="(unit, index) in module.units"
          :key="index"
        >
          <router-link
            class="unit-card"
            :to="'/modules/' + $route.params.module_id + '/' + index + '/about'"
          >
            <v-card
              class="pa-4"
              elevation="0"
            >
              <h2>
                {{ unit.unitName }}
              </h2>
              <p class="card-subtitle">
                <b>{{ unit.sectionsCompleted }}/{{ unit.sections.length }}</b> sections completed
              </p>
              <br/>
              <b class="learn-arrow">Learn →</b>
            </v-card>
          </router-link>
        </v-col>
      </v-row>

      <v-card
        id="module-about"
        class="mt-16 pb-4 text-font-size-16"
        max-width="33rem"
      >
        <v-card-title>
          About this module
        </v-card-title>
        <v-card-text>
          {{ module.moduleAbout.slice(0, 200) }}...
        </v-card-text>

        <br/>
        <router-link
          class="learn-arrow ma-4 links"
          :to="{
            path: '/modules/' + $route.params.module_id + '/about',
          }"
        >
          View full description →
        </router-link>
      </v-card>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {Modules} from "@/types/modules";
import NotFound from "@/views/NotFound.vue";

export default Vue.extend({
  name: "ModuleUnits",
  data: () => ({
    module: {} as Modules,
    userId: "",
  }),
  methods: {
    async populateGeneralModule(moduleId: string) {
      await fetch("https://nushigh.school/chokola/modules/get_module?" + new URLSearchParams({
        "module_id": moduleId
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.module = JSON.parse(JSON.stringify(data.data));
          }
        )
      );
    },

    async populateUserModule(userId: string, moduleId: string) {
      await fetch("https://nushigh.school/chokola/users/get_user_module?" + new URLSearchParams({
        "userId": userId,
        "moduleId": moduleId
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.module = JSON.parse(JSON.stringify(data.data));
          }
        )
      );
    }
  },
  async created() {
    const userId = this.$cookies.get("userId");

    if (userId === null) {
      await this.populateGeneralModule(this.$route.params.module_id);
    }
    else {
      await fetch("https://nushigh.school/chokola/users/user_exists?" + new URLSearchParams({
        "userId": userId,
      }), {
          headers: {
            "accept": "application/json",
          }
        }
      ).then(
        response => response.json().then(
          data => {
            if (data.data.exists) {
              this.userId = userId;
              this.populateUserModule(this.userId, this.$route.params.module_id);
            }
            else {
              this.populateGeneralModule(this.$route.params.module_id);
            }
          }
        )
      );
    }
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
