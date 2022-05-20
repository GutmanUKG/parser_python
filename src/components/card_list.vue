<template>
  <div class="wrapper_cards">
    <div class="item" v-for="(item, id) in CARDS" :key="id">
      <img :src="item.img_paths[0]" alt="">
      <h2>
        {{item.name}}
      </h2>
      <div class="price">
        {{item.price}}
      </div>

    </div>

  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "card_list",
  methods: {
    ...mapActions("cardStore", ["GET_PRODUCTS_FROM_API"]),
  },
  mounted() {
    this.GET_PRODUCTS_FROM_API().then((response) => {
      if (response.data) {
        this.loading = false;
        if (response.data.length > 0) {
          this.errored = false;
        }
      }
    });
  },
  computed: {
    ...mapGetters("cardStore", ["CARDS"]),
  }
}
</script>

<style lang="scss" >
  .wrapper_cards{
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    .item{
      padding: 20px;
      box-sizing: border-box;
      border-radius: 3px;
      background: #c2c2c2;
      flex: 0 0 25%;
      width: 25%;
      img{
        width: 100%;
      }
    }
  }
</style>
