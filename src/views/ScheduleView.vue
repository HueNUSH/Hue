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
                        <h2>Day 1 Schedule: Chemistry</h2>
                        <h3>13/03/23</h3>
                        
                        <p></p>
                        <p>Today we will be covering three chapters. Your trainers for today will be Leemen, Yu Xin and James</p>
                        <p>0900 - 1000 Lesson 1: The Elements</p>
                        <p>1010 - 1120 Lesson 2: Atoms</p>
                        <p>1130 - 1300 Lesson 3: Compounds</p>
                    </v-card>
                    <p></p>
                    <v-card class="pa-6">
                        <h2>Day 1 Schedule: Python</h2>
                        <h3>13/03/23</h3>
                        
                        <p></p>
                        <p>Today we will be covering three chapters. Your trainers for today will be Justin and Zhi Yuan</p>
                        <p>0900 - 1015 Lesson 1: Introduction and Operators</p>
                        <p>1030 - 1130 Lesson 2: Variables</p>
                        <p>1145 - 1245 Lesson 3: Types and Conditionals</p>
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