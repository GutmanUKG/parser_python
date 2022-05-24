<template>
  <div>

      <div class="wrapper_cards">
    <div class="item" v-for="(item, id) in CARDS" :key="id">
      <router-link
          :to="{name: 'detail_card_page', params: {id: id, date: item}}">

      <img :src="item.img_paths[0]" alt="">
      <h2>
        {{item.name}}
      </h2>
      <div class="price">
        {{item.price * 6.91 + ' Теньге'}}
      </div>
      </router-link>
    </div>
  </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "card_list",
  props: {
    data: {
      type: Object,
    }
  },
  methods: {
    ...mapActions("cardStore", ["GET_PRODUCTS_FROM_API"]),
  },
  mounted() {
    this.GET_PRODUCTS_FROM_API().then((response) => {
      if (response.data) {
        // this.loading = false;
        if (response.data.length > 0) {
          // this.errored = false;
        }
      }
    });
  },
  computed: {
    ...mapGetters("cardStore", [
        "CARDS"

    ]),
  }
}
</script>

<style lang="scss" >
  .wrapper_cards{
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: center;
    .item{
      padding: 20px;
      box-sizing: border-box;
      border-radius: 3px;
      background: #c2c2c2;
      flex: 0 0 calc(25% - 30px);
      width: calc(25% - 30px);
      img{
        width: 100%;
        height: 400px;
        object-fit: cover;
      }
      a{
        text-decoration: none;
        color: #000;
        .price{
          color: #000;
          font-weight: 500;
        }
      }
    }
  }
</style>
