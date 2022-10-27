<template>
    <v-container fluid class="px-12 py-6">
        <div align="center">
            <br />
        <h1>Hue is Coming Soon!</h1>
        <br />
        <p>The website is currently under construction by our coding team...</p>
        <p>Be sure to attend the onboarding session on 17 November!</p>
        <flip-countdown :deadline="deadline1"
        @timeElapsed="timeElapsedHandler"></flip-countdown>

        <h3>For any pressing queries, please direct them to <u>admin@huelearning.space</u></h3>
    
    </div>
        

        
    </v-container>
</template>

<script>
import FlipCountdown from "vue2-flip-countdown";
const fmt = "YYYY-MM-DD HH:mm:ss";
export default {
    components: {
        FlipCountdown
    },
    data(){
        return {deadline1:'2022-11-17 16:00:00'}
    },
    methods: {
    timeElapsedHandler: function () {
      // console.warn('Count Down Elapsed!!!')
    }
  }
}
</script>