<template>
  <div :style="{ color: activeColor, fontSize: fontSize + 'px' }">
    {{ msg }}
  </div>
</template>

<script>
export default {
  props: {
    msg: String
  },
  data() {
    return {
        activeColor: 'blue',
        fontSize: 30
    }
  }
}
</script>

<style>
h1 {
  color: red;
}
h2 {
  color: blue;
}
</style>