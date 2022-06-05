<template>
  <v-container class="pa-6" max-width="80rem" fluid>
    <v-card class="px-12 py-6" max-width="80rem">
      <router-link to="/modules" class="back-link">
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
              {{ module_icon }}
            </v-icon>
          </v-sheet>
        </v-col>

        <v-col class="pl-4 mt-3">
          <h1 class="card-title">{{ module_title }}</h1>
          <p class="card-subtitle">{{ module_subtitle }}</p>
        </v-col>
      </v-row>

    </v-card>

    <div class="pa-15">
      <p>Units - {{ completed_units }}/{{ total_units }} completed</p>

      <v-btn :to="'/modules/' + $route.params.module_id + '/about'">
        About this module
      </v-btn>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "ModuleUnits",
  data: () => ({
    // Hard coded for now, get from data base in future
    module_icon: "mdi-flask-empty-outline",
    module_title: "Module Title",
    module_subtitle: "Module Subtitle",
    completed_units: 6,
    total_units: 6,
  }),
  computed: {
    units(): Array<{
      unit_title: string;
      sections_completed: number;
      total_sections: number;
    }> {
      return [
        {
          unit_title: "Unit 1",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_title: "Unit 2",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_title: "Unit 3",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_title: "Unit 4",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_title: "Unit 5",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_title: "Unit 6",
          sections_completed: 3,
          total_sections: 3,
        },
      ];
    },
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
