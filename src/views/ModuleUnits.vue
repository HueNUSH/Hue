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

    <div class="pa-15" id="unit-grid">
      <b id="completed-units">Units • {{ completed_units }}/{{ total_units }} completed </b>
      <p/>

      <v-row>
        <v-col
          cols="12"
          lg="4"
          md="6"
          v-for="(unit, index) in units"
          :key="index"
        >
          <router-link
            class="unit-card"
            :to="'/modules/' + $route.params.module_id + '/' + unit.unit_no"
          >
            <v-card
              class="pa-4"
              elevation="0"
            >
              <h2>
                {{ unit.unit_title }}
              </h2>
              <p class="card-subtitle">
                <b>{{ unit.sections_completed }}/{{ unit.total_sections }}</b> sections completed
              </p>
              <br/>
              <p class="learn-arrow">Learn →</p>
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
          {{ module_about }}
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

export default Vue.extend({
  name: "ModuleUnits",
  data: () => ({
    // Hard coded for now, get from data base in future
    module_icon: "mdi-flask-empty-outline",
    module_title: "Module Title",
    module_subtitle: "Module Subtitle",
    completed_units: 6,
    total_units: 6,
    module_about: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ac nibh non " +
      "\n felis ultricies sodales a at enim. In quis quam fermentum, congue neque sed, molestie " +
      "\n velit. Ut ultrices elit odio, tincidunt volutpat tortor pulvinar ut. Vivamus sed metus " +
      "\n non nulla scelerisque ultrices vitae at tellus.",
  }),
  computed: {
    units(): Array<{
      unit_no: number;
      unit_title: string;
      sections_completed: number;
      total_sections: number;
    }> {
      return [
        {
          unit_no: 1,
          unit_title: "Unit 1",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_no: 2,
          unit_title: "Unit 2",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_no: 3,
          unit_title: "Unit 3",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_no: 4,
          unit_title: "Unit 4",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_no: 5,
          unit_title: "Unit 5",
          sections_completed: 3,
          total_sections: 3,
        },
        {
          unit_no: 6,
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
