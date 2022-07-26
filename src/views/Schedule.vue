<template>
  <v-container fluid class="pl-20 pr-31 py-16">
    <h1>Schedule</h1>

    <v-row class="d-flex align-start fill-height">
      <v-col cols="8" class="pa-14">
        <vc-calendar class="custom-calendar max-w-full" :masks="masks" :attributes="attributes" disable-page-swipe
          is-expanded>
          <template v-slot:day-content="{ day, attributes }">
            <span> {{ day.day }}</span>
            <p v-for="attr in attributes" :key="attr.key" class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1">
              {{ attr.customData.title }}
            </p>
          </template>
        </vc-calendar>
      </v-col>
      <v-col cols="3" class="pa-14">
        <h1>Lectures Timings for Chemistry</h1>
        <p></p>
        <h3>We will conduct lectures every XXX at XXX</h3>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
// @ts-ignore  i love abusing this :)
import VCalendar from 'v-calendar';

const month = new Date().getMonth();
const year = new Date().getFullYear();

Vue.use(VCalendar, {
  componentPrefix: 'vc',
});

export default Vue.extend({
  name: "Schedule",

  data: () => ({
    masks: {
      weekdays: 'WWW',
    },
    attributes: [
      {
        key: 1,
        customData: {
          title: 'Lecture 1000-1200.',
          class: 'bg-red-600 text-white',
        },
        dates: new Date(year, month, 1),
      },
    ],
  }),

});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";

::v-deep .vc-header {
  background-color: $c-primary-background;
  padding: 10px 0;
}

::v-deep .vc-title {
  color: $c-text-light-primary;
}

::v-deep .vc-svg-icon path {
  fill: $c-text-light-primary  !important;
}

::v-deep .vc-svg-icon {
  fill: $c-primary-foreground;
}

::v-deep.vc-weeks {
  padding: 0;
}

::v-deep .vc-weekday {
  background-color: #f8fafc;
  border-bottom: #eaeaea;
  border-top: #eaeaea;
  padding: 5px 0;
}

::v-deep .vc-day {
  padding: 0 5px 3px 5px;
  text-align: left;
  min-height: 90px;
  height: 90px;
  min-width: 60px;
  width: 125px;
  background-color: white;

  & .weekday-1,
  & .weekday-7 {
    background-color: #eff8ff;
  }

  &:not(.on-bottom) {
    border-bottom: 1px solid #b8c2cc;

    &.weekday-1 {
      border-bottom: 1px solid #b8c2cc;
    }
  }

  &:not(.on-right) {
    border-right: 1px solid #b8c2cc;
  }
}

::v-deep .vc-day-dots {
  margin-bottom: 5px;
}
</style>
