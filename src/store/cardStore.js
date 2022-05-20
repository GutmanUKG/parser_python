import axios from "axios";



const cardStore = {
    namespaced: true,
    state: {
        posts: {}
    },
    getters: {
        CARDS(state){
            return state.posts
        },
        COUNT_POSTS(state){
            return state.posts.length
        }
    },
    mutations: {
        SET_PRODUCT_TO_STATE:(state, posts)=>{
            state.posts = posts;
        },
        SET_CART:(state,posts)=>{
            state.posts.push(posts)
        },
    },
    actions: {
        GET_PRODUCTS_FROM_API({commit}){
              return axios('http://localhost:8080/result.json', {
                method: "GET"
              })
                  .then((posts)=>{
                    commit('SET_PRODUCT_TO_STATE',posts.data);
                    return posts;
                  })
                  .catch((error)=>{
                    console.log(error)
                    return error
                  })
            },
        ADD_TO_CART({commit}, posts){
            commit('SET_CART', posts)
        },
    }
}
export default cardStore
