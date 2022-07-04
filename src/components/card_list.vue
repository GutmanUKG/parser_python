<template>
  <div class="d-flex flex-wrap justify-content-center gap-5">
     <div class="card col-3" v-for="(item,id) in CARDS" :key="id" >
    <img :src="item.img_paths[0]" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ item.name }}</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's
        content.</p>
      <div class="price">
        {{ item.price * 6.91 + ' Теньге' }}
      </div>
      <router-link :to="{name: 'detail_card_page', params: {en_name: item.en_name, date: item}}" class="btn btn-outline-primary">
        Go somewhere
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

<style lang="scss">
.wrapper_cards {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;

  .item {
    padding: 20px;
    box-sizing: border-box;
    border-radius: 3px;
    background: #c2c2c2;
    flex: 0 0 calc(25% - 30px);
    width: calc(25% - 30px);

    img {
      width: 100%;
      height: 400px;
      object-fit: cover;
    }

    a {
      text-decoration: none;
      color: #000;

      .price {
        color: #000;
        font-weight: 500;
      }
    }
  }
}
</style>
