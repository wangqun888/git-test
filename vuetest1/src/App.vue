<template>
  <div>
    <HelloPeter msg="Hello Wang"></HelloPeter>
  </div>
  <div >
    <HelloWorld msg="传入文本!"></HelloWorld>
  </div>
  <div>
    <Input></Input>
  </div>
</template>

<script setup>
import HelloWorld from './components/HelloWorld.vue'
import HelloPeter from './components/HelloPeter.vue'
import Input from './components/input/input.vue'
</script>

<style>
</style>