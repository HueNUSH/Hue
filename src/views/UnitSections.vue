<template>
  <v-container fluid class="px-12 py-6">
    <router-link :to="'/modules/' + $route.params.module_id">
      < Back to Module
    </router-link>

    <p> Sections of a unit </p>
    <p> Module id: {{ $route.params.module_id }}</p>
    <p> Unit no: {{ $route.params.unit_no}} </p>
  </v-container>
</template>

<script>
export default {
  name: "UnitSections"
}
</script>
