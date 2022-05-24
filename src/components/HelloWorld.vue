<template>
  <div class="container">
    <div>Header</div>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'HelloWorld',
  components: {},
  props: {
    msg: String
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .container{
    max-width: 1366px;
    width: 100%;
    margin: 0 auto;
  }
</style>
