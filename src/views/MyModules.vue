<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    <h1>Welcome back, {{ user.name }}!</h1>
    <p class="text-dark-tertiary text-font-size-16">Academic Week</p>
    <h2 class="text-dark-primary text-display-semibold text-font-size-16 pb-3" style="margin-top: 75px;">
      My modules
    </h2>
    <div style="max-width: 80rem">
      <v-row>
        <v-col cols="12" lg="4" md="6" v-for="(module, index) in modules" :key="index">
          <router-link class="unit-card" :to="'/modules/' + module._id" :module="module">
            <v-card class="pa-4 fill-height d-flex flex-column" elevation="0">
              <v-row>
                <v-col cols="auto" class="d-flex flex-column">
                  <v-sheet
                    class="rounded-circle d-flex align-center justify-center align-self-baseline"
                    :color="
                      module.moduleIconBackgroundColor === 'orange'
                        ? '#FBDE94'
                        : module.moduleIconBackgroundColor === 'pink'
                        ? '#FFC8F9'
                        : module.moduleIconBackgroundColor === 'green'
                        ? '#C5F4B5'
                        : '#B6EDFE'
                    "
                    :height="40"
                    :width="40"
                  >
                    <v-icon>
                      {{ module.moduleIcon }}
                    </v-icon>
                  </v-sheet>


                  <h3 class="text-dark-primary text-display-semibold text-font-size-22">
                    {{ module.moduleName }}
                  </h3>
                  <p class="text-dark-tertiary text-font-size-14">
                    <b>{{ module.unitsCompleted }}/{{ module.units.length }}</b> sections completed
                  </p>
                </v-col>
              </v-row>

              <p class="learn-arrow text-semibold text-font-size-16">View units →</p>
            </v-card>
          </router-link>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {Modules} from "@/types/modules";

export default Vue.extend({
  name: "MyModules",
  data: () => ({
    user: {
      name: "Lustin Jim"
    },
    modules: [] as Array<Modules>
  }),
  methods: {
    populateMethods() {
      fetch("http://nushigh.school/chokola/modules/get_modules", {
        method: "GET",
        headers: {
          "accept": "application/json",
        }
      }).then(
        response => response.json().then(
          data => {
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            for (const moduleKey in data.data[0]) {
              const module: Modules = JSON.parse(JSON.stringify(data.data[0][parseInt(moduleKey)]));
              this.modules.push(module);
            }
          }
        )
      );
    }
  },
  created() {
    this.populateMethods();
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
