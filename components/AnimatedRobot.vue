<script setup>
import { ref } from 'vue'

const showVideo = ref(false)
</script>

<template>
  <div class="cursor-pointer" @click.stop="showVideo = true">
    <img 
      v-if="!showVideo" 
      src="/bp_behavior_lego.png" 
      class="h-40 w-auto object-contain" 
    />
    <video 
      v-else 
      autoplay 
      muted 
      loop 
      playsinline 
      class="h-40 w-auto object-contain" 
      style="clip-path: inset(40px 40px 30px 40px);"
    >
      <source src="/dab_dance.mp4" type="video/mp4">
    </video>
  </div>
</template>
