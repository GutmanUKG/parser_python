<template>
  <div class="container">
    <h1>
      {{date.name}}
    </h1>
    <div class="content">
      <div class="col-6">
        <div class="imgs">
          <img v-for="(img, id) in date.img_paths" :src="img" alt="" :key="id">
        </div>
      </div>
      <div class="col-6">
        <div class="descr">
          {{date.description}}
        </div>
        <p class="price">
          {{date.price * 6.91 + ' Tеньге'}}
        </p>
        <router-link to="/">Назад</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "card_detail_page",
  props: {
    date: {}
  },
}
</script>

<style scoped lang="scss">
  .container{
    max-width: 1366px;
    width: 100%;
    margin: 0 auto;
    h1{
      text-align: left;
    }
    .content{
      display: flex;
    }
    .col-6{
      flex: 0 0 calc(50% - 30px);
      .imgs{
        display: flex;
        gap: 30px;
        flex-wrap: wrap;
        width: 100%;
        img{
          max-width: calc(50% - 30px);
          width: 100%;
          object-fit: cover;
          height: 400px;
        }
      }
    }
    .col-6{
      flex: 0 0 calc(50% - 30px);
      text-align: left;
      .descr{
        font-size: 20px;
      }
      .price{
        font-weight: 900;
      }
    }
  }
</style>