<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    <h1>Welcome back, {{ user.name }}!</h1>
    <p class="text-dark-tertiary text-font-size-16">Academic Week</p>

    <h2 class="text-dark-primary text-display-semibold text-font-size-16" style="margin-top: 75px;">
      My modules
    </h2>
    <div style="max-width: 80rem">
      <v-row>
        <v-col cols="12" lg="4" md="6" v-for="(module, index) in modules" :key="index">
          <router-link class="unit-card" :to="'/modules/' + module.module_id">
            <v-card class="pa-4 fill-height d-flex flex-column" elevation="0">
              <v-row>
                <v-col cols="auto" class="d-flex align-center">
                  <v-sheet
                    class="rounded-circle d-flex align-center justify-center"
                    :color="
                      module.module_icon_background_color === 'orange'
                        ? '#FBDE94'
                        : module.module_icon_background_color === 'pink'
                        ? '#FFC8F9'
                        : module.module_icon_background_color === 'green'
                        ? '#C5F4B5'
                        : '#B6EDFE'
                    "
                    :height="40"
                    :width="40"
                  >
                    <v-icon>
                      {{ module.module_icon }}
                    </v-icon>
                  </v-sheet>
                </v-col>
              </v-row>
              <h3 class="text-dark-primary text-display-semibold text-font-size-22">
                {{ module.module_title }}
              </h3>

              <p class="text-dark-tertiary text-font-size-14">
                <b>{{ module.units_completed }}/{{ module.total_units }}</b> sections completed
              </p>

              <v-spacer />

              <b class="learn-arrow">View units →</b>
            </v-card>
          </router-link>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "MyModules",
  data: () => ({
    user: {
      name: "Lustin Jim"
    }
  }),
  computed: {
    modules(): Array<{
      module_icon: string;
      module_icon_background_color: string;
      module_id: number;
      module_title: string;
      units_completed: number;
      total_units: number;
    }> {
      return [
        {
          module_icon: "mdi-flask-empty-outline",
          module_icon_background_color: "orange",
          module_id: 1,
          module_title: "Introduction to Chemistry",
          units_completed: 3,
          total_units: 3
        },
        {
          module_icon: "mdi-flash-outline",
          module_icon_background_color: "pink",
          module_id: 2,
          module_title: "Physics",
          units_completed: 0,
          total_units: 10
        },
        {
          module_icon: "mdi-microscope",
          module_icon_background_color: "green",
          module_id: 3,
          module_title: "Biology",
          units_completed: 5,
          total_units: 10
        },
        {
          module_icon: "mdi-calculator-variant",
          module_icon_background_color: "blue",
          module_id: 4,
          module_title: "Math",
          units_completed: 2,
          total_units: 2
        }
      ];
    }
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
