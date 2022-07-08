<template>
  <v-container class="pa-6" max-width="80rem" fluid>
    <v-card
      class="px-12 py-6"
      max-width="80rem"
      elevation="0"
    >
      <router-link to="/modules" class="links">
        < My modules
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

    <div class="pa-14" id="unit-grid">
      <b class="text-dark-primary">Units • {{ module.unitsCompleted }}/{{ module.units.length }} completed </b>
      <p/>

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
            :to="'/modules/' + $route.params.module_id + '/' + index"
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
        class="mt-16 pb-4"
        max-width="33rem"
      >
        <v-card-title>
          About this module
        </v-card-title>
        <v-card-text>
          {{ module.moduleAbout }}
        </v-card-text>

        <br/>
        <router-link
          class="learn-arrow ma-4 links"
          :to="'/modules/' + $route.params.module_id + '/about'"
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

export default Vue.extend({
  name: "ModuleUnits",
  data: () => ({
    module: Modules
  }),
  async created() {
    await fetch("http://0.0.0.0:8000/modules/get_module/?" + new URLSearchParams({
      "module_id": this.$route.params.module_id
    }), {
      method: "GET",
    }).then(
      response => response.json().then(
        data => {
          this.module = JSON.parse(JSON.stringify(data.data[0]));
          }
      )
    );
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
