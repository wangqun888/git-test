<template>
  <h1>{{ msg }}</h1>
  <button @click="count++">计数器: {{ count }}</button>
  <!--p>编辑components/HelloWorld.vue以测试热模块更换。</p-->
</template>

<script>
export default {
  props: {
    msg: String
  },
  data() {
    return {
      count: 0
    }
  }
}
</script>
<style>
h1 {
  color: red;
}
</style>
