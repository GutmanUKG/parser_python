<template>
  <div class="container">
    <Card_list/>
  </div>
</template>

<script>

import Card_list from "@/components/card_list";
export default {
  name: 'HelloWorld',
  components: {Card_list},
  props: {
    msg: String
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .container{
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
  }
</style>
