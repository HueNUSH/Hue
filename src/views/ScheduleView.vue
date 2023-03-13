<template>
    <v-container flex fluid class="pb-16 pt-16">

        <v-container>
            <v-row>
                <v-col cols=10>
                    <h1>Schedule</h1>
                    <br />
                    <!-- <div>
                        <v-sheet class="hidden-xs-only" flex fluid height="600">
                            <v-calendar ref="calendar"></v-calendar>
                        </v-sheet>

                        <v-sheet class="hidden-sm-and-up" flex fluid>
                            <v-calendar ref="calendar"></v-calendar>
                        </v-sheet>
                    </div> -->
                </v-col>
                <v-col cols=10>
                    <v-card class="pa-6">
                        <h2>Day 2 Schedule: Chemistry</h2>
                        <h3>14/03/23</h3>
                        
                        <p></p>
                        <p>Today we will be covering three chapters. Your trainers for today will be Pin Rui, Leemen and Mattias</p>
                        <p>0900 - 0945 Lesson 4: The Periodic Table</p>
                        <p>1000 - 1115 Lesson 5: Metals</p>
                        <p>1130 - 1230 Lesson 6: Non-metals</p>
                    </v-card>
                    <p></p>
                    <v-card class="pa-6">
                        <h2>Day 2 Schedule: Python</h2>
                        <h3>14/03/23</h3>
                        
                        <p></p>
                        <p>Today we will be covering three chapters. Your trainer for today will be Zhi Yuan</p>
                        <p>0900 - 1000 Lesson 4: Functions</p>
                        <p>1015 - 1130 Lesson 5: Loops & Lists</p>
                        <p>1145 - 1245 Lesson 6: Modules</p>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>


    </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    name: "App",
    components: {
    }
})
</script>

<style lang="scss" scoped>
@import '../styles/variables.scss';
@import "../styles/global.scss";

.v-text-field {
    color: $c-primary-foreground !important
}

.v-application .primary {
    color: $c-primary-foreground !important
}

::v-deep .v-btn__content {
    color: darkgrey;
}

::v-deep .v-btn {
    opacity: 0.9 !important;
}
</style>