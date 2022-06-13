<template>
  <v-container fluid class="pl-20 pr-31 py-16">
    <h1>Schedule</h1>

    <v-row class="mt-4">
      <v-col cols="1">
        <v-btn
          icon
          @click="$refs.calendar.prev()"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-col>

      <v-col cols="3">
        <v-select
          v-model="select"
          :items="items"
          item-text="test"
          background-color="white"
          outlined
        ></v-select>
      </v-col>

      <v-col cols="3">
        <v-select
          v-model="type"
          :items="types"
          background-color="white"
          outlined
        ></v-select>
      </v-col>

      <v-col cols="1">
        <v-btn
          icon
          @click="$refs.calendar.next()"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <v-sheet height="600">
      <v-calendar
        ref="calendar"
        v-model="value"
        :weekdays="weekday"
        :type="type.toLowerCase()"
      ></v-calendar>
    </v-sheet>

  </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    name: "Schedule",
    data: () => ({
      type: "month",
      types: ["Month", "Week", "Day", "4Day"],
      value: "",
      weekday: [0, 1, 2, 3, 4, 5, 6],
      select: "All Modules",
      items: ["All Modules", "Module 1", "Module 2", "Module 3"],
    }),
  });
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
