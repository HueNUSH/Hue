<template>
  <v-container fluid class="pl-20 pr-31 py-16">
    <h1>Schedule</h1>
    <div class="pt-4">
      <vc-calendar class="custom-calendar max-w-full" :masks="masks" :attributes="attributes" disable-page-swipe
        is-expanded>
        <template v-slot:day-content="{ day, attributes }">
          <span> {{day.day}}</span>
          <p v-for="attr in attributes"
              :key="attr.key"
              class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1"
              :class="attr.customData.class">
            {{attr.customData.title}}    
          </p>
          <!-- <div class="flex flex-col h-full z-10 overflow-hidden">
          <span class="day-label text-sm text-gray-900">{{ day.day }}</span>
          <div class="flex-grow overflow-y-auto overflow-x-auto">
            <p
              v-for="attr in attributes"
              :key="attr.key"
              class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1"
              :class="attr.customData.class"
            >
              
            </p>
          </div>
        </div> -->
        </template>
      </vc-calendar>
    </div>

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
          title: 'Test text.',
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
  background-color: #f1f5f8;
  padding: 10px 0;
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
  height: 60px;
  min-width: 60px;
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
