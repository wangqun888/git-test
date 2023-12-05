<template>
    <div>
      <p>input 元素：</p>
      <input v-model="message" placeholder="编辑我……">
      <p>输入消息是: {{ message }}</p>

      <p>textarea 元素：</p>
      <textarea v-model="message2" placeholder="多行文本输入……"></textarea>
      <p>textarea 表单消息是:</p>
      <p style="white-space: pre">{{ message2 }}</p>
      <p>单个复选框：</p>
      <input type="checkbox" id="checkbox" v-model="checked">
      <label for="checkbox">{{ checked }}</label>

      <p>多个复选框：</p>
      <input type="checkbox" id="runoob" value="Runoob" v-model="checkedNames">
      <label for="runoob">Runoob</label>
      <input type="checkbox" id="google" value="Google" v-model="checkedNames">
      <label for="google">Google</label>
      <input type="checkbox" id="taobao" value="Taobao" v-model="checkedNames">
      <label for="taobao">taobao</label>
      <span>选择的值为: {{ checkedNames }}</span><br>
        <input type="radio" id="runoob" value="Runoob" v-model="picked">
        <label for="runoob">Runoob</label>
        <br>
        <input type="radio" id="google" value="Google" v-model="picked">
        <label for="google">Google</label>
        <br>
        <span>选中值为: {{ picked }}</span>
        <br>
        <select v-model="selected" name="site">
            <option v-for="option in options" :value="option.value">
              {{ option.text }}
    </option>
        </select>
        <div id="output">
            选择的网站是: {{selected}}
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      message2: '菜鸟教程\r\nhttps://www.runoob.com',
      checked : false,
      checkedNames: [],
      picked : 'Runoob',
      selected: '',
      options: [
        { text: 'Runoob', value: 'www.runoob.com' },
        { text: 'Google', value: 'www.google.com' },
        { text: 'Taobao', value: 'www.taobao.com' }
      ]
    }
  }
 }
</script>